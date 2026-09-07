from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification

item_name_to_id = {"Wall Jump": 109,
	"Tracking Center Blueprint": 300,
	"Ferrox Field": 400,
	"The Executioner": 409,
	"The Bruisers": 418,
	"Little Helper": 430,
	"Blood-Colored Glasses": 500,
	"Torothshoe Magnet": 501,
	"Combat Diskette": 504,
	"Phase 3 Accelerator": 531,
	"Sao": 600,
	"Fluffy": 621,
	"Mia": 629,
	"Raw Materials": 801,
	"Logic Block": 802,
	"S.A.F.E. Kit": 803,
	"Vital Module": 804,
	"Attack Module": 805,
	"Laurentium": 808,
	"Ferrosculating Fluxograph": 820,
	"Letter-Tapper Relic": 1,
	"Memento Socket": 2}

# id: [quantity, classification]
# filler = 0, progression = 1, useful = 2	
item_id_to_info = {109: [1, 1],
	300: [1, 1],
	400: [1, 2],
	409: [1, 2],
	418: [1, 2],
	430: [1, 2],
	500: [1, 0],
	501: [1, 2],
	504: [1, 2],
	531: [1, 2],
	600: [1, 0],
	621: [1, 0],
	629: [1, 0],
	801: [1, 0],
	802: [1, 0],
	803: [1, 1],
	804: [1, 2],
	805: [1, 2],
	808: [1, 0],
	820: [1, 1],
	1: [0, 0],
	2: [1, 2]}
	
starting_weapons = ("The Bruisers", "The Executioner")

def create_items_function(world):
	items = []
	for item_name in item_name_to_id:
		if item_name != world.starting_weapon:
			item_id = item_name_to_id[item_name]
			info = item_id_to_info[item_id]
			quantity = info[0]
			classification = ItemClassification(info[1])
			items += [BiomorphItem(item_name, classification, item_id, world.player)] * quantity
	world.multiworld.itempool += items
	
def place_starting_weapon(world):
	name = world.starting_weapon
	item = BiomorphItem(name, ItemClassification.progression, item_name_to_id[name], world.player)
	location = world.get_location("Core's Lab: Starting Weapon")
	location.place_locked_item(item)
	
class BiomorphItem(Item):
	game = "Biomorph"		