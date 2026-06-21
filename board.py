from effects import Node


class City:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.node = None

    def add_node(self, node_index: int):
        '''
        Add visual node for city
        '''
        self.node = node_index

class Connection:
    def __init__(self, start_city: City, end_city: City, distance: int, num_tracks: int):
        self.start_city = start_city
        self.end_city = end_city
        self.distance = distance
        self.nodes: list[list[int]] = [[]] * num_tracks

        for i in range(num_tracks):
            self.nodes[i] = [None] * distance

    def add_nodes_index(self, node_indices: list[int], track_index=0):
        '''
        Add visual nodes in order from start city to end city
        '''
        self.nodes[track_index] = node_indices

    def set_node(self, node_index: int, connection_index: int, track_index=0):
        self.nodes[track_index][connection_index] = node_index

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

# In specific order as found in "drawing.svg"
connections = (
    Connection(SEATTLE, VANCOUVER, 1, 2),            #  0
    Connection(SEATTLE, PORTLAND, 1, 2),             #  1
    Connection(SAN_FRANCISCO, PORTLAND , 5, 2),      #  2
    Connection(LOS_ANGELES, SAN_FRANCISCO, 3, 2),    #  3
    Connection(LOS_ANGELES, EL_PASO, 6, 1),          #  4
    Connection(VANCOUVER, CALGARY, 3, 1),            #  5
    Connection(SEATTLE, CALGARY, 4, 1),              #  6
    Connection(SEATTLE, HELENA, 6, 1),               #  7
    Connection(PORTLAND, SALT_LAKE_CITY, 6, 1),      #  8
    Connection(SAN_FRANCISCO, SALT_LAKE_CITY, 5, 2), #  9
    Connection(LAS_VEGAS, SALT_LAKE_CITY, 3, 1),     # 10
    Connection(LOS_ANGELES, LAS_VEGAS, 2, 1),        # 11
    Connection(LOS_ANGELES, PHOENIX, 3, 1),          # 12
    Connection(PHOENIX, EL_PASO, 3, 1),              # 13
    Connection(PHOENIX, SANTA_FE, 3, 1),             # 14
    Connection(PHOENIX, DENVER, 5, 1),               # 15
    Connection(SALT_LAKE_CITY, DENVER, 3, 2),        # 16
    Connection(SALT_LAKE_CITY, HELENA, 3, 1),        # 17
    Connection(CALGARY, HELENA, 4, 1),               # 18
    Connection(CALGARY, WINNIPEG, 6, 1),             # 19
    Connection(HELENA, WINNIPEG, 4, 1),              # 20
    Connection(HELENA, DULUTH, 6, 1),                # 21
    Connection(HELENA, OMAHA, 5, 1),                 # 22
    Connection(DENVER, HELENA, 4, 1),                # 23
    Connection(DENVER, OMAHA, 4, 1),                 # 24
    Connection(DENVER, KANSAS_CITY, 4, 2),           # 25
    Connection(DENVER, OKLAHOMA_CITY, 4, 1),         # 26
    Connection(SANTA_FE, DENVER, 2, 1),              # 27
    Connection(SANTA_FE, OKLAHOMA_CITY, 3, 1),       # 28
    Connection(EL_PASO, SANTA_FE, 2, 1),             # 29
    Connection(EL_PASO, OKLAHOMA_CITY, 5, 1),        # 30
    Connection(EL_PASO, DALLAS, 4, 1),               # 31
    Connection(EL_PASO, HOUSTON, 6, 1),              # 32
    Connection(HOUSTON, DALLAS, 1, 2),               # 33
    Connection(DALLAS, OKLAHOMA_CITY, 2, 2),         # 34
    Connection(OKLAHOMA_CITY, KANSAS_CITY, 2, 2),    # 35
    Connection(OMAHA, KANSAS_CITY, 1, 2),            # 36
    Connection(OMAHA, DULUTH, 2, 2),                 # 37
    Connection(WINNIPEG, DULUTH, 4, 1),              # 38
    Connection(WINNIPEG, SAULT_ST_MARIE, 6, 1),      # 39
    Connection(DULUTH, SAULT_ST_MARIE, 3, 1),        # 40
    Connection(DULUTH, TORONTO, 6, 1),               # 41
    Connection(DULUTH, CHICAGO, 3, 1),               # 42
    Connection(OMAHA, CHICAGO, 4, 1),                # 43
    Connection(KANSAS_CITY, ST_LOUIS, 2, 2),         # 44
    Connection(OKLAHOMA_CITY, LITTLE_ROCK, 2, 1),    # 45
    Connection(DALLAS, LITTLE_ROCK, 2, 1),           # 46
    Connection(HOUSTON, NEW_ORLEANS, 2, 1),          # 47
    Connection(LITTLE_ROCK, NEW_ORLEANS, 3, 1),      # 48
    Connection(LITTLE_ROCK, ST_LOUIS, 2, 1),         # 49
    Connection(ST_LOUIS, CHICAGO, 2, 2),             # 50
    Connection(CHICAGO, TORONTO, 4, 1),              # 51
    Connection(SAULT_ST_MARIE, TORONTO, 2, 1),       # 52
    Connection(SAULT_ST_MARIE, MONTREAL, 5, 1),      # 53
    Connection(TORONTO, MONTREAL, 3, 1),             # 54
    Connection(MONTREAL, BOSTON, 2, 2),              # 55
    Connection(PITTSBURGH, TORONTO, 2, 1),           # 56
    Connection(NEW_YORK, MONTREAL, 3, 1),            # 57
    Connection(NEW_YORK, BOSTON, 2, 2),              # 58
    Connection(CHICAGO, PITTSBURGH, 3, 2),           # 59
    Connection(PITTSBURGH, NEW_YORK, 2, 2),          # 60
    Connection(ST_LOUIS, PITTSBURGH, 5, 1),          # 61
    Connection(NASHVILLE, PITTSBURGH, 4, 1),         # 62
    Connection(RALEIGH, PITTSBURGH, 2, 1),           # 63
    Connection(PITTSBURGH, WASHINGTON, 2, 1),        # 64
    Connection(WASHINGTON, NEW_YORK, 2, 2),          # 65
    Connection(ST_LOUIS, NASHVILLE, 2, 1),           # 66
    Connection(NASHVILLE, RALEIGH, 3, 1),            # 67
    Connection(RALEIGH, WASHINGTON, 2, 2),           # 68
    Connection(LITTLE_ROCK, NASHVILLE, 3, 1),        # 69
    Connection(NASHVILLE, ATLANTA, 1, 1),            # 70
    Connection(ATLANTA, RALEIGH, 2, 2),              # 71
    Connection(RALEIGH, CHARLESTON, 2, 1),           # 72
    Connection(NEW_ORLEANS, ATLANTA, 4, 2),          # 73
    Connection(ATLANTA, MIAMI, 5, 1),                # 74
    Connection(CHARLESTON, MIAMI, 4, 1),             # 75
    Connection(NEW_ORLEANS, MIAMI, 6, 1),            # 76
    Connection(ATLANTA, CHARLESTON, 2, 1),           # 77
)