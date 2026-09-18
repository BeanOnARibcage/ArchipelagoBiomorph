from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
from .locations import location_name_to_id as lnid, create_regions_function, BiomorphLocation
from .items import item_name_to_id as inid, create_items_function, starting_weapons, \
	place_starting_weapon, BiomorphItem
from .logic import connect_regions, location_logic

class BiomorphWorld(World):
	"""Biomorph is a Metroidvania where you can turn into the enemies you defeat."""
	
	game = "Biomorph"
	
	#web is for later
	
	#options is for later but soon
	
	origin_region_name = "Opening"
	starting_weapon = ""
	
	item_name_to_id = inid
	location_name_to_id = lnid
	
	def generate_early(self):
		self.starting_weapon = self.multiworld.random.choice(starting_weapons)
	
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
		return {"starting_weapon": id}
		
	def create_item(self, name):
		return BiomorphItem(name, ItemClassification.filler, item_name_to_id[name], self.player)
		
	def get_filler_item_name(self):
		return "Laurentium"