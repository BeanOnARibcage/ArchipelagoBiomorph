from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
import copy

item_name_to_id = {"Wall Jump": 109,
	"Fubirang Biomorph": 215,
	"Scarbyttle Biomorph": 236,
	"Tracking Center Blueprint": 300,
	"Chip Imprinter Blueprint": 304,
	"Laboratory Blueprint": 315,
	"Restorer's Shop Blueprint": 316,
	"Ferrox Field": 400,
	"The Executioner": 409,
	"The Bruisers": 418,
	"Little Helper": 430,
	"Blood-Colored Glasses": 500,
	"Torothshoe Magnet": 501,
	"Combat Diskette": 504,
	"Phase 3 Accelerator": 531,
	"Spearsliver": 540,
	"Scargato (Sao)": 600,
	"Scargato (Pounio)": 610,
	"Scargato (Fluffy)": 621,
	"Scargato (Mia)": 629,
	"Blightmoor's Ballad": 700,
	"Life is a Skyway": 703,
	"Raw Materials": 801,
	"Logic Block": 802,
	"S.A.F.E. Kit": 803,
	"Vital Module": 804,
	"Attack Module": 805,
	"Laurentium": 808,
	"Ferrosculating Fluxograph": 820,
	"S.A.F.E. Scanner": 859,
	"Letter-Tapper Relic": 1,
	"Memento Socket": 2}

# id: [quantity, classification, first_is_progression (default False)]
# filler = 0, progression = 1, useful = 2	
item_id_to_info = {109: [1, 1],
	215: [1, 2, True],
	236: [2, 2],
	300: [2, 1],
	304: [1, 2],
	315: [1, 0],
	316: [1, 1],
	400: [1, 2],
	409: [1, 2],
	418: [1, 1],
	430: [1, 2],
	500: [1, 0],
	501: [1, 2],
	504: [1, 2],
	531: [1, 2],
	540: [1, 2],
	600: [1, 0],
	610: [1, 0],
	621: [1, 0],
	629: [1, 0],
	700: [1, 0],
	703: [1, 0],
	801: [3, 2],
	802: [4, 2],
	803: [1, 1],
	804: [1, 2],
	805: [1, 2],
	808: [0, 0],
	820: [1, 1],
	859: [1, 2],
	1: [1, 0, True],
	2: [2, 2]}
	
# starting_weapons = [x for x in item_name_to_id if item_name_to_id[x] // 100 in (2, 4) and \
# 	item_name_to_id[x] not in (400, 430)]
starting_weapons = ["Scarbyttle Biomorph"]
chargeless_weapons = ("The Bruisers", "Fubirang Biomorph")

def create_items_function(world):
	items = []
	for item_name in item_name_to_id:
		item_id = item_name_to_id[item_name]
		info = item_id_to_info[item_id]
		quantity = info[0]
		classification = ItemClassification(info[1])
		first_is_progression = len(info) > 2 and info[2] == True
		if item_name == world.starting_weapon:
			quantity -= 1
			first_is_progression = False
		if first_is_progression:
			items += [BiomorphItem(item_name, ItemClassification.progression, item_id, world.player)]
			for _ in range(quantity - 1):
				items += [BiomorphItem(item_name, classification, item_id, world.player)]
		else:
			for _ in range(quantity):
				items += [BiomorphItem(item_name, classification, item_id, world.player)]
	world.multiworld.itempool += items
	
def place_starting_weapon(world):
	name = world.starting_weapon
	item = BiomorphItem(name, ItemClassification.progression, item_name_to_id[name], world.player)
	location = world.get_location("Core's Lab: Starting Weapon")
	location.place_locked_item(item)
	
class BiomorphItem(Item):
	game = "Biomorph"		