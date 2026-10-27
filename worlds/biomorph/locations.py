from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
from .items import BiomorphItem

region_locations = {"Opening": [301],
	"Core's Lab Revisit": list(range(302, 309)),
	"Blightmoor": list(range(1, 11)) + list(range(47, 56)) + [59, 60, 61, 401, 415],
	"Blightmoor Underground": [11, 12, 13],
	"Salm & Alma's Shop 1": [23, 24, 25, 26],
	"Mezzo Skyway": list(range(402, 415)),
	"Mezzo Skyway Lower Right": [416, 417, 418],
	"Dunes of Time (entrance 1)": [103],
	"Dunes of Time (entrance 2)": [],
	"Dunes of Time (main area)": [101, 102] + list(range(104, 113)),
	"Dunes of Time (above gate)": list(range(113, 116)),
	"Dunes of Time (past Ferrox Nook)": list(range(116, 123)) + [126, 127],
	"Dunes of Time (past Miratos)": [123, 124, 125],
	"Goal Region": [],
	"Biomorph Unlocks": list(range(2000, 20015))}
	
location_name_to_id = {"Core's Lab: Starting Weapon": 301,
	"Core's Lab: Item Left of Toroth": 302,
	"Core's Lab: Ferrox Analysis Arena": 303,
	"Core's Lab: Item Past Arena": 304,
	"Core's Lab: Item Past Breakable Wall": 305,
	"Core's Lab: Item Above Aberror": 307,
	"Core's Lab: Scargato": 308,
	"Blightmoor: Scargato on Harlo's Roof": 1,
	"Blightmoor: Scargato on the Kertars' Roof": 2,
	"Blightmoor: Slar Kertar 1": 3,
	"Blightmoor: Slar Kertar 2": 4,
	"Blightmoor: Slar Kertar 3": 5,
	"Blightmoor: Slar Kertar 4": 6,
	"Blightmoor: Slar Kertar 5": 7,
	"Blightmoor: Boyd (return the wrench)": 8,
	"Blightmoor: Boyd (tracking center 1)": 9,
	"Blightmoor: Boyd (upgrade the safe)": 10,
	"Blightmoor: Asrar 1": 11,
	"Blightmoor: Asrar 2": 12,
	"Blightmoor: Asrar 3": 13,
	"Blightmoor: Salm Kertar 1": 23,
	"Blightmoor: Salm Kertar 2": 24,
	"Blightmoor: Salm Kertar 3": 25,
	"Blightmoor: Salm Kertar 4": 26,
	"Blightmoor: Mémé (5 scargatos)": 47,
	"Blightmoor: Marle Kertar (build the shop)": 52,
	"Blightmoor: Meed (get the blueprint)": 53,
	"Blightmoor: Boyd (tracking center 2)": 54,
	"Blightmoor: Will": 59,
	"Blightmoor: Salm Kertar (get the blueprint)": 60,
	"Blightmoor: Skipio (deliver the lock)": 61,
	"Mezzo: Abandoned Delivery Bay Arena": 401,
	"Mezzo: Breakable Wall Near First Fubirang": 402,
	"Mezzo: Scargato Through Narrow Passage": 404,
	"Mezzo: Will": 405,
	"Mezzo: Marle's Blueprint": 406,
	"Mezzo: Corner Near Lifts and Spikes": 407,
	"Mezzo: Corner Behind Fubirang": 408,
	"Mezzo: Letter-Tapper for Meed": 410,
	"Mezzo: Breakable Wall Behind Florox": 411,
	"Mezzo: Gorgerzer Reward": 413,
	"Mezzo: Hidden Area Above Floroxes": 417,
	"Mezzo: Secret Highway Arena": 418,
	"Dunes: Main Room Crystal Wall": 101,
	"Dunes: Entrance Crystal Wall": 103,
	"Dunes: Main Room Wall Jump Nook": 104,
	"Dunes: Restless Sands Arena": 106,
	"Dunes: Alma's Ring": 107,
	"Dunes: Scargato Before Salm": 109,
	"Dunes: Across Spikes Above Salm": 110,
	"Dunes: Salm Kertar (return the ring)": 111,
	"Dunes: Spike Maze Scargato": 112,
	"Dunes: Will": 114,
	"Dunes: Passage Near Hidden SAFE": 115,
	"Dunes: Ferrox Nook Arena": 116,
	"Dunes: Laser Chimney": 118,
	"Dunes: Scargato Above Busko": 119,
	"Dunes: Mind's Desire Arena": 120,
	"Dunes: Busko (start quest)": 121,
	"Dunes: Item Near Water": 122,
	"Dunes: Miratos Reward": 123,
	"Dunes: Light Puzzle Near Miratos": 125,
	"Dunes: Laser Circuit Hidden Cave": 126,
	"Dunes: Hidden Cave Under First Generator": 127,
	"Biomorphs: 6 Fubirangs": 2000,
	"Biomorphs: 6 Scarbyttles": 2003,
	"Biomorphs: 12 Scarbyttles": 2004,
	"Biomorphs: 5 Toroths": 2006,
	"Biomorphs: 10 Toroths": 2007,
	"Biomorphs: 14 Toroths": 2008,
	"Biomorphs: 3 Sorios": 2009,
	"Biomorphs: 5 Sorios": 2010,
	"Biomorphs: 8 Sorios": 2011,
	"Biomorphs: 4 Klereks": 2012,
	"Biomorphs: 7 Klereks": 2013}

categories = ("Core's Lab", "Blightmoor", "Mezzo", "Dunes", "Biomorphs")
def category_locations(category):
	return {x for x in location_name_to_id if x.startswith(category)}	
location_groups = {category: category_locations(category) for category in categories}

def subset_location_name_to_id(region_name):
	locations = region_locations[region_name]
	lnti = location_name_to_id
	subset = {x: lnti[x] for x in lnti if lnti[x] in locations}
	return subset
	
def create_regions_function(world):
	for region_name in region_locations:
		region = Region(region_name, world.player, world.multiworld)
		world.multiworld.regions += [region]
		region.add_locations(subset_location_name_to_id(region_name), BiomorphLocation)
	create_events(world)
		
monster_locations = \
	{"Opening": {"Toroth": [1]},
	"Core's Lab Revisit": {"Toroth": [2, 3]},
	"Mezzo Skyway": {"Fubirang": [1, 2, 3, 4, 5, 8, 9, 10, 11, 12],
		"Scarbyttle": [1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16]},
	"Mezzo Skyway Lower Right": {"Scarbyttle": [10, 11]},
	"Dunes of Time (entrance 1)": {"Klerek": [1],
		"Sorios": [1]},
	"Dunes of Time (entrance 2)": {"Toroth": [4]},
	"Dunes of Time (main area)": {"Toroth": [5, 6],
		"Sorios": [2, 3, 4]},
	"Dunes of Time (above gate)": {"Toroth": [7],
		"Klerek": [2, 3]},
	"Dunes of Time (past Ferrox Nook)": {"Toroth": [8, 9, 10, 12, 13, 14],
		"Klerek": [4, 5, 6, 7, 8, 9],
		"Sorios": [5, 6, 7, 8]},
	"Dunes of Time (past Miratos)": {"Toroth": [11],
		"Klerek": [10]}}
	
def create_events(world):
	for region_name in monster_locations:
		region = world.get_region(region_name)
		for monster_name in monster_locations[region_name]:
			for monster_number in monster_locations[region_name][monster_name]:
				region.add_event(monster_name + " " + str(monster_number), \
					monster_name + " Progress", None, BiomorphLocation, BiomorphItem)
	dunes_3 = world.get_region("Dunes of Time (past Ferrox Nook)")
	dunes_4 = world.get_region("Dunes of Time (past Miratos)")
	dunes_3.add_event("Generator 1", "Generator", None, BiomorphLocation, BiomorphItem)
	dunes_3.add_event("Generator 2", "Generator", None, BiomorphLocation, BiomorphItem)
	dunes_4.add_event("Generator 3", "Generator", None, BiomorphLocation, BiomorphItem)
	goal_region = world.get_region("Goal Region")
	goal_region.add_event("Open the Athenaeum", "Goal", None, BiomorphLocation, BiomorphItem)
		
class BiomorphLocation(Location):
	game = "Biomorph"