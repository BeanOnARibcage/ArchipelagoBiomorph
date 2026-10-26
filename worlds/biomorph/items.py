from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
import copy

def get_classification(item_name):
	item_id = item_name_to_id[item_name]
	return ItemClassification(item_id_to_info[item_id][1])

# name: id, quantity, classification, first_is_progression (default False)
# filler = 0, progression = 1, useful = 2, progression_deprioritized_skip_balancing = 25
item_name_to_info = {"Wall Jump": (109, 1, 1),
	"Fubirang Biomorph": (215, 1, 2, True),
	"Klerek Biomorph": (224, 2, 2, True),
	"Scarbyttle Biomorph": (236, 2, 2, True),
	"Sorios Biomorph": (245, 3, 2, True),
	"Toroth Biomorph": (257, 3, 2, True),
	"Tracking Center Blueprint": (300, 2, 1),
	"Chip Imprinter Blueprint": (304, 1, 2),
	"Apartment Blueprint": (312, 1, 0),
	"Laboratory Blueprint": (315, 1, 0),
	"Restorer's Shop Blueprint": (316, 1, 2, True),
	"Salm & Alma's Shop Blueprint": (319, 1, 1),
	"Ferrox Field": (400, 1, 2),
	"The Executioner": (409, 1, 2),
	"Shadow Sting": (412, 1, 2),
	"Pain Legion": (415, 1, 2),
	"The Bruisers": (418, 1, 1),
	"Little Helper": (430, 1, 2),
	"Ferrox Specter": (433, 1, 2),
	"Blood-Colored Glasses": (500, 1, 0),
	"Torothshoe Magnet": (501, 1, 2),
	"Combat Diskette": (504, 1, 2),
	"Transfigure Piece": (510, 1, 2),
	"Positive Solenoid": (516, 1, 2),
	"Monster Fang": (522, 1, 2),
	"Phase 3 Accelerator": (531, 1, 2),
	"Spearsliver": (540, 1, 2),
	"Scargato (Sao)": (600, 1, 25),
	"Scargato (Yuri)": (603, 1, 25),
	"Scargato (Bella)": (604, 1, 25),
	"Scargato (Capitaine)": (605, 1, 25),
	"Scargato (Pounio)": (610, 1, 25),
	"Scargato (Fluffy)": (621, 1, 25),
	"Scargato (Mia)": (629, 1, 25),
	"Blightmoor's Ballad": (700, 1, 0),
	"Sands of Sadness": (701, 1, 0),
	"Life is a Skyway": (703, 1, 0),
	"Raw Materials": (801, 7, 2),
	"Logic Block": (802, 7, 2),
	"S.A.F.E. Kit": (803, 1, 1),
	"Vital Module": (804, 1, 2),
	"Attack Module": (805, 1, 2),
	"Laurentium": (808, 2, 0),
	"Old Military Access Card": (809, 1, 1),
	"Ferrosculating Fluxograph": (820, 1, 1),
	"Half of a Locking Mechanism": (827, 1, 1),
	"Letter to Lucius": (828, 1, 0),
	"Trading Guild Ring": (829, 1, 1),
	"S.A.F.E. Scanner": (859, 1, 2),
	"Letter-Tapper Relic": (1, 2, 0, True),
	"Memento Socket": (2, 4, 2)}

item_name_to_id = {x: y[0] for x, y in item_name_to_info.items()}
	
starting_weapons = [x for x in item_name_to_id if item_name_to_id[x] // 100 in (2, 4) and \
	item_name_to_id[x] not in (400, 430)]
chargeless_weapons = ("The Bruisers", "Fubirang Biomorph", "Klerek Biomorph", "Toroth Biomorph")

item_groups = {"Ability": {x for x in item_name_to_id if item_name_to_id[x] // 100 == 1},
				"Biomorph": {x for x in item_name_to_id if item_name_to_id[x] // 100 == 2},
				"Blueprint": {x for x in item_name_to_id if item_name_to_id[x] // 100 == 3},
				"Chip": {x for x in item_name_to_id if item_name_to_id[x] // 100 == 4},
				"Memento": {x for x in item_name_to_id if item_name_to_id[x] // 100 == 5},
				"Scargato": {x for x in item_name_to_id if item_name_to_id[x] // 100 == 6},
				"Other": {x for x in item_name_to_id if item_name_to_id[x] // 100 in (7, 8, 0)}}
item_groups["Weapon"] = set.union(item_groups["Chip"], item_groups["Biomorph"])

def create_items_function(world):
	items = []
	for item_name in item_name_to_info:
		info = item_name_to_info[item_name]
		item_id = info[0]
		quantity = info[1]
		classification = ItemClassification(info[2])
		first_is_progression = len(info) > 3 and info[3] == True
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