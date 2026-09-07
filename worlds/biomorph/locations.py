from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification

region_locations = {"Opening": [301],
	"Core's Lab Revisit": list(range(302, 309)),
	"Blightmoor": list(range(1, 11)) + [401],
	"Blightmoor Underground": [11, 12, 13]}
	
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
	"Mezzo: Abandoned Delivery Bay Arena": 401}

def subset_location_name_to_id(region_name):
	locations = region_locations[region_name]
	lnti = location_name_to_id
	subset = {x: lnti[x] for x in lnti if lnti[x] in locations}
	return subset
	
def create_regions_function(world):
	for region_name in region_locations:
		print(region_name, type(region_name))
		region = Region(region_name, world.player, world.multiworld)
		world.multiworld.regions += [region]
		region.add_locations(subset_location_name_to_id(region_name), BiomorphLocation)
		
class BiomorphLocation(Location):
	game = "Biomorph"