from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
from .locations import location_name_to_id as lnid, create_regions_function, BiomorphLocation, \
	location_groups
from .items import item_name_to_id as inid, create_items_function, starting_weapons, \
	place_starting_weapon, BiomorphItem, get_classification, chargeless_weapons, item_groups
from .logic import connect_regions, location_logic
from .options import BiomorphOptions

class BiomorphWorld(World):
	"""Biomorph is a Metroidvania where you can turn into the enemies you defeat."""
	
	game = "Biomorph"
	
	#web is for later
	
	options_dataclass = BiomorphOptions
	options: BiomorphOptions
	
	origin_region_name = "Opening"
	starting_weapon: str
	
	item_name_to_id = inid
	location_name_to_id = lnid
	
	item_name_groups = item_groups
	location_name_groups = location_groups
	
	def generate_early(self):
		sw_option = self.options.starting_weapon
		if sw_option == "any":
			self.starting_weapon = self.random.choice(starting_weapons)
		elif sw_option == "chargeless":
			self.starting_weapon = self.random.choice(chargeless_weapons)
		else:
			self.starting_weapon = sw_option.get_option_name(sw_option.value)
	
	def create_regions(self):
		create_regions_function(self)
		
	def set_rules(self):
		connect_regions(self)
		location_logic(self)
		
	def create_items(self):
		create_items_function(self)
		
	def pre_fill(self):
		place_starting_weapon(self)
		
	def fill_slot_data(self):
		id = self.item_name_to_id[self.starting_weapon]
		shop_option = self.options.reduce_shop_prices.value
		return {"starting_weapon": id, "reduce_shop_prices": shop_option}
		
	def create_item(self, name):
		return BiomorphItem(name, get_classification(name), item_name_to_id[name], self.player)
		
	def get_filler_item_name(self):
		return "Laurentium"