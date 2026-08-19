from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification

class BiomorphWorld(World):
	"""Biomorph is a Metroidvania where you can turn into the enemies you defeat."""
	
	game = "Biomorph"
	
	#web is for later
	
	#options is for later but soon
	
	location_name_to_id = {"Item left of toroth": 1, "Ferrox Analysis arena": 2, 
		"Item past arena": 3, "Secret room past aberror": 4, "Item above aberror": 5}
	item_name_to_id = {"Raw Materials": 1, "Laurentium": 2, "Vital Module": 3,
		"Logic Block": 4, "Torothshoe Magnet": 5}
	origin_region_name = "Opening"
	
	def create_regions(self):
		opening = Region("Opening", self.player, self.multiworld)
		self.multiworld.regions += [opening]
		opening.add_locations(location_name_to_id, BiomorphLocation)
		
	def set_rules(self):
		pass
		
	def create_items(self):
		raw_materials = BiomorphItem("Raw Materials", ItemClassification.filler, 1, self.player)
		laurentium = BiomorphItem("Laurentium", ItemClassification.filler, 2, self.player)
		vital_module = BiomorphItem("Vital Module", ItemClassification.useful, 3, self.player)
		logic_block = BiomorphItem("Logic Block", ItemClassification.filler, 4, self.player)
		torothshoe_magnet = BiomorphItem("Torothshoe Magnet", ItemClassification.useful, 5, self.player)
		self.multiworld.itempool += [raw_materials, laurentium, vital_module, logic_block, torothshoe_magnet] 
		#Remember not to add the starting weapon to the itempool, once it's randomized
		
	def create_item(self, name):
		return BiomorphItem(name, ItemClassification.filler, item_name_to_id[name], self.player)
		
	def get_filler_item_name(self):
		return "Laurentium"
		
	def fill_slot_data(self):
		pass
		
class BiomorphLocation(Location):
	game = "Biomorph"
	
class BiomorphItem(Item):
	game = "Biomorph"