from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
from .items import BiomorphItem

region_locations = {"Opening": [301],
	"Core's Lab Revisit": list(range(302, 309)),
	"Blightmoor": list(range(1, 11)) + list(range(47, 56)) + [59, 401, 415],
	"Blightmoor Underground": [11, 12, 13],
	"Mezzo Skyway": list(range(402, 415)),
	"Mezzo Skyway Lower Right": [416, 417, 418],
	"Goal Region": [],
	"Biomorph Unlocks": list(range(2000, 2006))}
	
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
	"Blightmoor: Marle Kertar (build the shop)": 52,
	"Blightmoor: Meed (get the blueprint)": 53,
	"Blightmoor: Boyd (tracking center 2)": 54,
	"Blightmoor: Will": 59,
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
	"Biomorphs: 6 Fubirangs": 2000,
	"Biomorphs: 6 Scarbyttles": 2003,
	"Biomorphs: 12 Scarbyttles": 2004}

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
	{"Mezzo Skyway": {"Fubirang": [1, 2, 3, 4, 5, 8, 9, 10, 11, 12],
		"Scarbyttle": [1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16]},
	"Mezzo Skyway Lower Right": {"Scarbyttle": [10, 11]}}
	
def create_events(world):
	for region_name in monster_locations:
		region = world.get_region(region_name)
		for monster_name in monster_locations[region_name]:
			for monster_number in monster_locations[region_name][monster_name]:
				region.add_event(monster_name + " " + str(monster_number), \
					monster_name + " Progress", None, BiomorphLocation, BiomorphItem)
				print("Adding event")
	goal_region = world.get_region("Goal Region")
	goal_region.add_event("Enter the Dunes", "Goal", None, BiomorphLocation, BiomorphItem)
		
class BiomorphLocation(Location):
	game = "Biomorph"