from effects import Node


class City:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.node = None

    def add_node(self, node: Node):
        '''
        Add visual node for city
        '''
        self.node = node

class Connection:
    def __init__(self, start_city: City, end_city: City, distance: int, num_tracks: int):
        self.start_city = start_city
        self.end_city = end_city
        self.distance = distance
        self.nodes: list[list[Node]] = [[]] * num_tracks

        for i in range(num_tracks):
            self.nodes[i] = [None] * distance

    def add_nodes(self, nodes: list[Node], track_index=0):
        '''
        Add visual nodes in order from start city to end city
        '''
        self.nodes[track_index] = nodes

    def set_node(self, node: Node, connection_index, track_index=0):
        self.nodes[track_index][connection_index] = node

VANCOUVER         = City("Vancouver", 0)
SEATTLE           = City("Seattle", 1)
PORTLAND          = City("Portland", 2)
SAN_FRANCISCO     = City("San Francisco", 3)
LOS_ANGELES       = City("Los Angeles", 4)
CALGARY           = City("Calgary", 5)
HELENA            = City("Helena", 6)
SALT_LAKE_CITY    = City("Salt Lake City", 7)
LAS_VEGAS         = City("Las Vegas", 8)
PHOENIX           = City("Phoenix", 9)
WINNIPEG          = City("Winnipeg", 10)
DENVER            = City("Denver",  11)
SANTA_FE          = City("Santa Fe", 12)
EL_PASO           = City("El Paso", 13)
DULUTH            = City("Duluth", 14)
OMAHA             = City("Omaha", 15)
KANSAS_CITY       = City("Kansas City", 16)
OKLAHOMA_CITY     = City("Oklahoma City", 17)
DALLAS            = City("Dallas", 18)
HOUSTON           = City("Houston", 19)
SAULT_ST_MARIE    = City("Sault St Marie", 20)
CHICAGO           = City("Chicago", 21)
ST_LOUIS          = City("Saint Louis", 22)
LITTLE_ROCK       = City("Little Rock", 23)
NEW_ORLEANS       = City("New Orleans", 24)
TORONTO           = City("Toronto", 25)
PITTSBURGH        = City("Pittsburgh", 26)
NASHVILLE         = City("Nashville", 27)
MONTREAL          = City("Montreal", 28)
BOSTON            = City("Boston", 29)
NEW_YORK          = City("New York", 30)
WASHINGTON        = City("Washington", 31)
RALEIGH           = City("Raleigh", 32)
ATLANTA           = City("Atlanta", 33)
CHARLESTON        = City("Charleston", 34)
MIAMI             = City("Miami", 35)

cities: tuple[City] = (
    VANCOUVER,
    SEATTLE,
    PORTLAND,
    SAN_FRANCISCO,
    LOS_ANGELES,
    CALGARY,
    HELENA,
    SALT_LAKE_CITY,
    LAS_VEGAS,
    PHOENIX,
    WINNIPEG,
    DENVER,
    SANTA_FE,
    EL_PASO,
    DULUTH,
    OMAHA,
    KANSAS_CITY,
    OKLAHOMA_CITY,
    DALLAS,
    HOUSTON,
    SAULT_ST_MARIE,
    CHICAGO,
    ST_LOUIS,
    LITTLE_ROCK,
    NEW_ORLEANS,
    TORONTO,
    PITTSBURGH,
    NASHVILLE,
    MONTREAL,
    BOSTON,
    NEW_YORK,
    WASHINGTON,
    RALEIGH,
    ATLANTA,
    CHARLESTON,
    MIAMI
)

# In specific order as found in "Board - Routes.jpg"
connections = (
    Connection(SEATTLE, VANCOUVER, 1, 2),
    Connection(SEATTLE, PORTLAND, 1, 2),
    Connection(PORTLAND, SAN_FRANCISCO, 5, 2),
    Connection(LOS_ANGELES, SAN_FRANCISCO, 3, 2),
    Connection(EL_PASO, LOS_ANGELES, 6, 1),
    Connection(VANCOUVER, CALGARY, 3, 1),
    Connection(CALGARY, SEATTLE, 4, 1),
    Connection(SEATTLE, HELENA, 6, 1),
    Connection(PORTLAND, SALT_LAKE_CITY, 6, 1),
    Connection(SAN_FRANCISCO, SALT_LAKE_CITY, 5, 2),
    Connection(SALT_LAKE_CITY, LAS_VEGAS, 3, 1),
    Connection(LAS_VEGAS, LOS_ANGELES, 2, 1),
    Connection(LOS_ANGELES, PHOENIX, 3, 1),
    Connection(EL_PASO, PHOENIX, 3, 1),
    Connection(PHOENIX, SANTA_FE, 3, 1),
    Connection(DENVER, PHOENIX, 5, 1),
    Connection(SALT_LAKE_CITY, DENVER, 3, 2),
    Connection(HELENA, SALT_LAKE_CITY, 3, 1),
    Connection(HELENA, CALGARY, 4, 1),
    Connection(CALGARY, WINNIPEG, 6, 1),
    Connection(WINNIPEG, HELENA, 4, 1),
    Connection(HELENA, DULUTH, 6, 1),
    Connection(OMAHA, HELENA, 5, 1),
    Connection(HELENA, DENVER, 4, 1),
    Connection(DENVER, OMAHA, 4, 1),
    Connection(DENVER, KANSAS_CITY, 4, 2),
    Connection(OKLAHOMA_CITY, DENVER, 4, 1),
    Connection(DENVER, SANTA_FE, 2, 1),
    Connection(SANTA_FE, OKLAHOMA_CITY, 3, 1),
    Connection(EL_PASO, SANTA_FE, 2, 1),
    Connection(EL_PASO, OKLAHOMA_CITY, 5, 1),
    Connection(DALLAS, EL_PASO, 4, 1),
    Connection(EL_PASO, HOUSTON, 6, 1),
    Connection(HOUSTON, DALLAS, 1, 2),
    Connection(DALLAS, OKLAHOMA_CITY, 2, 2),
    Connection(KANSAS_CITY, OKLAHOMA_CITY, 4, 2),
    Connection(OMAHA, KANSAS_CITY, 1, 2),
    Connection(DULUTH, OMAHA, 2, 2),
    Connection(DULUTH, WINNIPEG, 4, 1),
    Connection(WINNIPEG, SAULT_ST_MARIE, 6, 1),
    Connection(SAULT_ST_MARIE, DULUTH, 3, 1),
    Connection(DULUTH, TORONTO, 6, 1),
    Connection(CHICAGO, DULUTH, 3, 1),
    Connection(OMAHA, CHICAGO, 4, 1),
    Connection(KANSAS_CITY, ST_LOUIS, 2, 2),
    Connection(OKLAHOMA_CITY, LITTLE_ROCK, 2, 1),
    Connection(LITTLE_ROCK, DALLAS, 2, 1),
    Connection(NEW_ORLEANS, HOUSTON, 2, 1),
    Connection(LITTLE_ROCK, NEW_ORLEANS, 3, 1),
    Connection(ST_LOUIS, LITTLE_ROCK, 2, 1),
    Connection(ST_LOUIS, CHICAGO, 2, 2),
    Connection(CHICAGO, TORONTO, 4, 1),
    Connection(TORONTO, SAULT_ST_MARIE, 2, 1),
    Connection(SAULT_ST_MARIE, MONTREAL, 5, 1),
    Connection(MONTREAL, TORONTO, 3, 1),
    Connection(MONTREAL, BOSTON, 2, 2),
    Connection(TORONTO, PITTSBURGH, 2, 1),
    Connection(NEW_YORK, MONTREAL, 3, 1),
    Connection(BOSTON, NEW_YORK, 2, 2),
    Connection(PITTSBURGH, CHICAGO, 3, 2),
    Connection(PITTSBURGH, NEW_YORK, 2, 2),
    Connection(ST_LOUIS, PITTSBURGH, 5, 1),
    Connection(NASHVILLE, PITTSBURGH, 4, 1),
    Connection(RALEIGH, PITTSBURGH, 2, 1),
    Connection(PITTSBURGH, WASHINGTON, 2, 1),
    Connection(NEW_YORK, WASHINGTON, 2, 2),
    Connection(NASHVILLE, ST_LOUIS, 2, 1),
    Connection(RALEIGH, NASHVILLE, 3, 1),
    Connection(WASHINGTON, RALEIGH, 2, 2),
    Connection(LITTLE_ROCK, NASHVILLE, 3, 1),
    Connection(NASHVILLE, ATLANTA, 1, 1),
    Connection(RALEIGH, ATLANTA, 2, 2),
    Connection(RALEIGH, CHARLESTON, 2, 1),
    Connection(ATLANTA, NEW_ORLEANS, 4, 2),
    Connection(ATLANTA, MIAMI, 5, 1),
    Connection(CHARLESTON, MIAMI, 4, 1),
    Connection(MIAMI, NEW_ORLEANS, 6, 1),
    Connection(ATLANTA, CHARLESTON, 2, 1),
)