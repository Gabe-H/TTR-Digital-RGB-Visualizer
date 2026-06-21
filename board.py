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

class Route:
    def __init__(self, start_city: City, end_city: City, distance, num_tracks):
        self.start_city = start_city
        self.end_city = end_city
        self.distance = distance

    def add_nodes(self, nodes: list[Node], track_index=0):
        '''
        Add visual nodes in order from start city to end city
        '''
        self.nodes[track_index] = nodes

VANCOUVER = City("Vancouver", 0)
SEATTLE = City("Seattle", 1)
PORTLAND = City("Portland", 2)
SAN_FRANCISCO = City("San Francisco", 3)
LOS_ANGELES = City("Los Angeles", 4)
CALGARY = City("Calgary", 5)
HELENA = City("Helena", 6)
SALT_LAKE_CITY = City("Salt Lake City", 7)
LAS_VEGAS = City("Las Vegas", 8)
PHOENIX = City("Phoenix", 9)
WINNIPEG = City("Winnipeg", 10)
DENVER = City("Denver",  11)
SANTA_FE = City("Santa Fe", 12)
EL_PASO = City("El Paso", 13)
DULUTH = City("Duluth", 14)
OMAHA = City("Omaha", 15)
KANSAS_CITY = City("Kansas City", 16)
OKLAHOMA_CITY = City("Oklahoma City", 17)
DALLAS = City("Dallas", 18)
HOUSTON = City("Houston", 19)
SAULT_ST_MARIE = City("Sault St. Marie", 20)
CHICAGO = City("Chicago", 21)
ST_LOUIS = City("St Louis", 22)
LITTLE_ROCK = City("Little Rock", 23)
NEW_ORLEANS = City("New Orleans", 24)
TORONTO = City("Toronto", 25)
PITTSBURGH = City("Pittsburgh", 26)
NASHVILLE = City("Nashville", 27)
MONTREAL = City("Montreal", 28)
BOSTON = City("Boston", 29)
NEW_YORK = City("New York", 30)
WASHINGTON = City("Washington", 31)
RALEIGH = City("Raleigh", 32)
ATLANTA = City("Atlanta", 33)
CHARLESTON = City("Charleston", 34)
MIAMI = City("Miami", 35)

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
route: list[Route] = (
    Route(SEATTLE, VANCOUVER, 1, 2),
    Route(SEATTLE, PORTLAND, 1, 2),
    Route(PORTLAND, SAN_FRANCISCO, 5, 2),
    Route(LOS_ANGELES, SAN_FRANCISCO, 3, 2),
    Route(EL_PASO, LOS_ANGELES, 6, 1),
    Route(VANCOUVER, CALGARY, 3, 1),
    Route(CALGARY, SEATTLE, 4, 1),
    Route(SEATTLE, HELENA, 6, 1),
    Route(PORTLAND, SALT_LAKE_CITY, 6, 1),
    Route(SAN_FRANCISCO, SALT_LAKE_CITY, 5, 2),
    Route(SALT_LAKE_CITY, LAS_VEGAS, 3, 1),
    Route(LAS_VEGAS, LOS_ANGELES, 2, 1),
    Route(LOS_ANGELES, PHOENIX, 3, 1),
    Route(EL_PASO, PHOENIX, 3, 1),
    Route(PHOENIX, SANTA_FE, 3, 1),
    Route(DENVER, PHOENIX, 5, 1),
    Route(SALT_LAKE_CITY, DENVER, 3, 2),
    Route(HELENA, SALT_LAKE_CITY, 3, 1),
    Route(HELENA, CALGARY, 4, 1),
    Route(CALGARY, WINNIPEG, 6, 1),
    Route(WINNIPEG, HELENA, 4, 1),
    Route(HELENA, DULUTH, 6, 1),
    Route(OMAHA, HELENA, 5, 1),
    Route(HELENA, DENVER, 4, 1),
    Route(DENVER, OMAHA, 4, 1),
    Route(DENVER, KANSAS_CITY, 4, 2),
    Route(OKLAHOMA_CITY, DENVER, 4, 1),
    Route(DENVER, SANTA_FE, 2, 1),
    Route(SANTA_FE, OKLAHOMA_CITY, 3, 1),
    Route(EL_PASO, SANTA_FE, 2, 1),
    Route(EL_PASO, OKLAHOMA_CITY, 5, 1),
    Route(DALLAS, EL_PASO, 4, 1),
    Route(EL_PASO, HOUSTON, 6, 1),
    Route(HOUSTON, DALLAS, 1, 2),
    Route(DALLAS, OKLAHOMA_CITY, 2, 2),
    Route(KANSAS_CITY, OKLAHOMA_CITY, 4, 2),
    Route(OMAHA, KANSAS_CITY, 1, 2),
    Route(DULUTH, OMAHA, 2, 2),
    Route(DULUTH, WINNIPEG, 4, 1),
    Route(WINNIPEG, SAULT_ST_MARIE, 6, 1),
    Route(SAULT_ST_MARIE, DULUTH, 3, 1),
    Route(DULUTH, TORONTO, 6, 1),
    Route(CHICAGO, DULUTH, 3, 1),
    Route(OMAHA, CHICAGO, 4, 1),
    Route(KANSAS_CITY, ST_LOUIS, 2, 2),
    Route(OKLAHOMA_CITY, LITTLE_ROCK, 2, 1),
    Route(LITTLE_ROCK, DALLAS, 2, 1),
    Route(NEW_ORLEANS, HOUSTON, 2, 1),
    Route(LITTLE_ROCK, NEW_ORLEANS, 3, 1),
    Route(ST_LOUIS, LITTLE_ROCK, 2, 1),
    Route(ST_LOUIS, CHICAGO, 2, 2),
    Route(CHICAGO, TORONTO, 4, 1),
    Route(TORONTO, SAULT_ST_MARIE, 2, 1),
    Route(SAULT_ST_MARIE, MONTREAL, 5, 1),
    Route(MONTREAL, TORONTO, 3, 1),
    Route(MONTREAL, BOSTON, 2, 2),
    Route(TORONTO, PITTSBURGH, 2, 1),
    Route(NEW_YORK, MONTREAL, 3, 1),
    Route(BOSTON, NEW_YORK, 2, 2),
    Route(PITTSBURGH, CHICAGO, 3, 2),
    Route(PITTSBURGH, NEW_YORK, 2, 2),
    Route(ST_LOUIS, PITTSBURGH, 5, 1),
    Route(NASHVILLE, PITTSBURGH, 4, 1),
    Route(RALEIGH, PITTSBURGH, 2, 1),
    Route(PITTSBURGH, WASHINGTON, 2, 1),
    Route(NEW_YORK, WASHINGTON, 2, 2),
    Route(NASHVILLE, ST_LOUIS, 2, 1),
    Route(RALEIGH, NASHVILLE, 3, 1),
    Route(WASHINGTON, RALEIGH, 2, 2),
    Route(LITTLE_ROCK, NASHVILLE, 3, 1),
    Route(NASHVILLE, ATLANTA, 1, 1),
    Route(RALEIGH, ATLANTA, 2, 2),
    Route(RALEIGH, CHARLESTON, 2, 1),
    Route(ATLANTA, NEW_ORLEANS, 4, 2),
    Route(ATLANTA, MIAMI, 5, 1),
    Route(CHARLESTON, MIAMI, 4, 1),
    Route(MIAMI, NEW_ORLEANS, 6, 1),
    Route(ATLANTA, CHARLESTON, 2, 1),
)