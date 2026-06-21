#!/usr/bin/env python3
"""
Extract rectangle centers and rotation angles from an Inkscape/SVG file.

Usage:
    python extract_rectangles.py drawing.svg
    python extract_rectangles.py drawing.svg output.csv

Notes:
- Ignores <image> elements automatically.
- Handles nested group transforms.
- Handles transform matrices, translate, scale, rotate, skewX, skewY.
- Reports coordinates in the SVG/viewBox coordinate system.
- SVG y-axis typically increases downward.
"""

import csv
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


SVG_NS = "{http://www.w3.org/2000/svg}"
INKSCAPE_NS = "{http://www.inkscape.org/namespaces/inkscape}"


def strip_ns(tag):
    """Remove XML namespace from a tag name."""
    return tag.split("}", 1)[-1] if "}" in tag else tag


def parse_float(value, default=0.0):
    """
    Parse SVG numbers like '12.3', '12.3px', or '12.3mm'.
    For this extractor, unit suffixes are ignored because SVG geometry
    is ultimately interpreted in the document coordinate system.
    """
    if value is None:
        return default

    match = re.search(r"[-+]?(?:\d+\.\d+|\d+|\.\d+)(?:[eE][-+]?\d+)?", value)
    if not match:
        return default
    return float(match.group(0))


def identity_matrix():
    # SVG affine matrix representation:
    # [ a c e ]
    # [ b d f ]
    # [ 0 0 1 ]
    return (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def multiply_matrices(m1, m2):
    """
    Compose two SVG affine matrices.

    Result = m1 @ m2
    """
    a1, b1, c1, d1, e1, f1 = m1
    a2, b2, c2, d2, e2, f2 = m2

    return (
        a1 * a2 + c1 * b2,
        b1 * a2 + d1 * b2,
        a1 * c2 + c1 * d2,
        b1 * c2 + d1 * d2,
        a1 * e2 + c1 * f2 + e1,
        b1 * e2 + d1 * f2 + f1,
    )


def apply_matrix(m, x, y):
    """Apply SVG affine matrix to a point."""
    a, b, c, d, e, f = m
    return (
        a * x + c * y + e,
        b * x + d * y + f,
    )


def parse_transform(transform):
    """
    Parse an SVG transform attribute into an affine matrix.

    SVG applies transform functions from left to right as written.
    """
    if not transform:
        return identity_matrix()

    result = identity_matrix()

    pattern = re.compile(r"([a-zA-Z]+)\s*\(([^)]*)\)")
    for name, args_text in pattern.findall(transform):
        args = [
            float(x)
            for x in re.findall(
                r"[-+]?(?:\d+\.\d+|\d+|\.\d+)(?:[eE][-+]?\d+)?",
                args_text,
            )
        ]

        name = name.lower()
        m = identity_matrix()

        if name == "matrix" and len(args) >= 6:
            m = tuple(args[:6])

        elif name == "translate":
            tx = args[0] if len(args) >= 1 else 0.0
            ty = args[1] if len(args) >= 2 else 0.0
            m = (1.0, 0.0, 0.0, 1.0, tx, ty)

        elif name == "scale":
            sx = args[0] if len(args) >= 1 else 1.0
            sy = args[1] if len(args) >= 2 else sx
            m = (sx, 0.0, 0.0, sy, 0.0, 0.0)

        elif name == "rotate":
            angle = math.radians(args[0] if len(args) >= 1 else 0.0)
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            rot = (cos_a, sin_a, -sin_a, cos_a, 0.0, 0.0)

            if len(args) >= 3:
                cx, cy = args[1], args[2]
                # rotate(angle, cx, cy) = translate(cx, cy) rotate(angle) translate(-cx, -cy)
                m = multiply_matrices(
                    multiply_matrices(
                        (1.0, 0.0, 0.0, 1.0, cx, cy),
                        rot,
                    ),
                    (1.0, 0.0, 0.0, 1.0, -cx, -cy),
                )
            else:
                m = rot

        elif name == "skewx":
            angle = math.radians(args[0] if args else 0.0)
            m = (1.0, 0.0, math.tan(angle), 1.0, 0.0, 0.0)

        elif name == "skewy":
            angle = math.radians(args[0] if args else 0.0)
            m = (1.0, math.tan(angle), 0.0, 1.0, 0.0, 0.0)

        result = multiply_matrices(result, m)

    return result


# def normalize_angle_degrees(angle):
#     """
#     Normalize angle to [-180, 180).
#     """
#     return ((angle + 180.0) % 360.0) - 180.0


# def angle_of_vector(dx, dy):
#     """
#     Return angle of vector in degrees, using SVG coordinate orientation.
#     Because SVG y increases downward, positive angles visually rotate clockwise.
#     """
#     return normalize_angle_degrees(math.degrees(math.atan2(dy, dx)))


# def rect_rotation_from_matrix(m):
#     """
#     Rotation of the rectangle's local x-axis after transformation.
#     """
#     a, b, c, d, e, f = m
#     return angle_of_vector(a, b)


# def extract_rectangles(svg_path):
#     tree = ET.parse(svg_path)
#     root = tree.getroot()

#     rows = []

#     def walk(element, parent_matrix):
#         element_transform = parse_transform(element.attrib.get("transform"))
#         current_matrix = multiply_matrices(parent_matrix, element_transform)

#         if strip_ns(element.tag) == "rect":
#             rect_id = element.attrib.get("id", "")
#             label = element.attrib.get(f"{INKSCAPE_NS}label", "")

#             x = parse_float(element.attrib.get("x"), 0.0)
#             y = parse_float(element.attrib.get("y"), 0.0)
#             width = parse_float(element.attrib.get("width"), 0.0)
#             height = parse_float(element.attrib.get("height"), 0.0)

#             local_cx = x + width / 2.0
#             local_cy = y + height / 2.0
#             center_x, center_y = apply_matrix(current_matrix, local_cx, local_cy)

#             rotation = rect_rotation_from_matrix(current_matrix)

#             # For tall rectangles, the long axis is the local y-axis.
#             # For wide rectangles, the long axis is the local x-axis.
#             if height > width:
#                 local_long_axis = apply_matrix(current_matrix, local_cx, local_cy + 1.0)
#                 long_axis_angle = angle_of_vector(
#                     local_long_axis[0] - center_x,
#                     local_long_axis[1] - center_y,
#                 )
#             else:
#                 local_long_axis = apply_matrix(current_matrix, local_cx + 1.0, local_cy)
#                 long_axis_angle = angle_of_vector(
#                     local_long_axis[0] - center_x,
#                     local_long_axis[1] - center_y,
#                 )

#             rows.append(
#                 {
#                     "id": rect_id,
#                     "label": label,
#                     "center_x": center_x,
#                     "center_y": center_y,
#                     "rotation_degrees": rotation,
#                     "long_axis_angle_degrees": long_axis_angle,
#                     "width": width,
#                     "height": height,
#                 }
#             )

#         for child in list(element):
#             walk(child, current_matrix)

#     walk(root, identity_matrix())
#     return rows

def extract_circles(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()

    rows = []

    def walk(element, parent_matrix):
        element_transform = parse_transform(element.attrib.get("transform"))
        current_matrix = multiply_matrices(parent_matrix, element_transform)

        if strip_ns(element.tag) == "circle":
            circle_id = element.attrib.get("id", "")
            label = element.attrib.get(f"{INKSCAPE_NS}label", "")

            cx = parse_float(element.attrib.get("cx"), 0.0)
            cy = parse_float(element.attrib.get("cy"), 0.0)
            r = parse_float(element.attrib.get("r"), 0.0)

            center_x, center_y = apply_matrix(current_matrix, cx, cy)

            rows.append({
                "id": circle_id,
                "center_x": center_x,
                "center_y": center_y
            })

        for child in list(element):
            walk(child, current_matrix)

    walk(root, identity_matrix())
    return rows


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python extract_circles.py drawing.svg")
        sys.exit(1)

    svg_path = Path(sys.argv[1])
    if not svg_path.exists():
        print(f"Error: file not found: {svg_path}")
        sys.exit(1)

    # output_path = Path(sys.argv[2]) if len(sys.argv) == 3 else svg_path.with_name(
    #     "rectangle_centers_rotations.csv"
    # )
    output_path = svg_path.with_name("circle_centers.csv")

    rows = extract_circles(svg_path)

    fieldnames = [
        "id",
        "label",
        "center_x",
        "center_y",
        "rotation_degrees",
        "long_axis_angle_degrees",
        "width",
        "height",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rectangles to {output_path}")


if __name__ == "__main__":
    main()