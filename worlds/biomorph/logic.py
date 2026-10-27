from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
import rule_builder.rules as rb
from .items import chargeless_weapons

# cached rules
wall_jump = rb.Has("Wall Jump")
arena_logic = rb.HasAny(*chargeless_weapons)

def connect_regions(world):		
	opening = world.get_region("Opening")
	blightmoor = world.get_region("Blightmoor")
	opening.connect(blightmoor, "Title Drop")
	
	blightmoor_underground = world.get_region("Blightmoor Underground")
	blightmoor.connect(blightmoor_underground, "Over the Underground Wall", wall_jump)
	
	salm_1 = world.get_region("Salm & Alma's Shop 1")
	blightmoor.connect(salm_1, "Open Salm & Alma's Shop", rb.Has("Salm & Alma's Shop Blueprint") &
		rb.CanReachLocation("Dunes: Salm Kertar (return the ring)"))
	
	lab_revisit = world.get_region("Core's Lab Revisit")
	blightmoor.connect(lab_revisit, "Boat Ride", wall_jump)
	
	skyway = world.get_region("Mezzo Skyway")
	blightmoor.connect(skyway, "Door to Mezzo Skyway",
		rb.HasAll("Ferrosculating Fluxograph", "Tracking Center Blueprint", "S.A.F.E. Kit"))
	
	skyway_lower_right = world.get_region("Mezzo Skyway Lower Right")
	skyway.connect(skyway_lower_right, "Skyway Lower Right Wall Climb", wall_jump)
	
	dunes_entrance_1 = world.get_region("Dunes of Time (entrance 1)")
	skyway.connect(dunes_entrance_1, "Dunes of Time Entrance", arena_logic)
	
	dunes_entrance_2 = world.get_region("Dunes of Time (entrance 2)")
	dunes_entrance_1.connect(dunes_entrance_2, "Dunes Entrance Light Puzzle")
	
	dunes_main = world.get_region("Dunes of Time (main area)")
	dunes_entrance_2.connect(dunes_main, "Dunes Crystal Into Main Room")
	dunes_main.connect(dunes_entrance_2, "Dunes Crystal Backwards From Main Room",
		rb.Has("Toroth Biomorph"))
	
	dunes_above = world.get_region("Dunes of Time (above gate)")
	dunes_access_card = rb.Has("Old Military Access Card")
	dunes_main.connect(dunes_above, "Dunes Access Gate", dunes_access_card)
	dunes_above.connect(dunes_main, "Dunes Access Gate backwards", dunes_access_card)
	dunes_above.connect(skyway_lower_right, "Dunes to Skyway Upper Passage", wall_jump)
	skyway_lower_right.connect(dunes_above, "Skyway to Dunes Upper Passage", wall_jump)
	
	dunes_ferrox = world.get_region("Dunes of Time (past Ferrox Nook)")
	dunes_above.connect(dunes_ferrox, "Clear Ferrox Nook", arena_logic)
	
	dunes_miratos = world.get_region("Dunes of Time (past Miratos)")
	dunes_ferrox.connect(dunes_miratos, "Defeat Miratos", arena_logic)
	
	dunes_ferrox.connect(dunes_main, "Up Into Dunes Main Room")
	
	goal = world.get_region("Goal Region")
	dunes_above.connect(goal, "Athenaeum Door", rb.Has("Generator", 3))
	
	biomorphs = world.get_region("Biomorph Unlocks")
	opening.connect(biomorphs, "Defeat First Toroth")
	
def location_logic(world):
	lab_scargato = world.get_location("Core's Lab: Scargato")
	world.set_rule(lab_scargato, wall_jump)
	
	harlo_roof_scargato = world.get_location("Blightmoor: Scargato on Harlo's Roof")
	world.set_rule(harlo_roof_scargato, wall_jump)
	
	temp_rule = rb.True_()
	
	boyd_1 = world.get_location("Blightmoor: Boyd (return the wrench)")
	temp_rule &= rb.Has("Ferrosculating Fluxograph")
	world.set_rule(boyd_1, temp_rule)
	
	boyd_2 = world.get_location("Blightmoor: Boyd (tracking center 1)")
	temp_rule &= rb.Has("Tracking Center Blueprint")
	world.set_rule(boyd_2, temp_rule)
	
	boyd_3 = world.get_location("Blightmoor: Boyd (upgrade the safe)")
	temp_rule &= rb.Has("S.A.F.E. Kit")
	world.set_rule(boyd_3, temp_rule)
	
	boyd_4 = world.get_location("Blightmoor: Boyd (tracking center 2)")
	temp_rule &= rb.Has("Tracking Center Blueprint", 2)
	world.set_rule(boyd_4, temp_rule)
	
	del temp_rule
	
	mémé_1 = world.get_location("Blightmoor: Mémé (5 scargatos)")
	world.set_rule(mémé_1, rb.HasGroup("Scargato", 5))
	
	marle = world.get_location("Blightmoor: Marle Kertar (build the shop)")
	world.set_rule(marle, rb.Has("Restorer's Shop Blueprint"))
	
	meed = world.get_location("Blightmoor: Meed (get the blueprint)")
	world.set_rule(meed, rb.Has("Letter-Tapper Relic") & rb.CanReachRegion("Mezzo Skyway"))
	
	salm = world.get_location("Blightmoor: Salm Kertar (get the blueprint)")
	world.set_rule(salm, rb.CanReachLocation("Dunes: Salm Kertar (return the ring)"))
	
	will_blightmoor = world.get_location("Blightmoor: Will")
	world.set_rule(will_blightmoor, rb.CanReachLocation("Mezzo: Will"))
	
	skipio = world.get_location("Blightmoor: Skipio (deliver the lock)")
	world.set_rule(skipio, rb.Has("Half of a Locking Mechanism"))
	
	mezzo_boss = world.get_location("Mezzo: Gorgerzer Reward")
	world.set_rule(mezzo_boss, arena_logic)
	
	secret_highway = world.get_location("Mezzo: Secret Highway Arena")
	world.set_rule(secret_highway, arena_logic)
	
	entrance_crystal = world.get_location("Dunes: Entrance Crystal Wall")
	world.set_rule(entrance_crystal, rb.Has("Toroth Biomorph"))
	
	nook = world.get_location("Dunes: Main Room Wall Jump Nook")
	world.set_rule(nook, wall_jump)
	
	restless_sands = world.get_location("Dunes: Restless Sands Arena")
	world.set_rule(restless_sands, arena_logic)
	
	alma_ring = world.get_location("Dunes: Alma's Ring")
	world.set_rule(alma_ring, rb.CanReachLocation("Dunes: Restless Sands Arena"))
	
	salm_dunes = world.get_location("Dunes: Salm Kertar (return the ring)")
	world.set_rule(salm_dunes, rb.Has("Trading Guild Ring"))
	
	sorios_scargato = world.get_location("Dunes: Scargato Before Salm")
	world.set_rule(sorios_scargato, rb.Has("Sorios Biomorph"))
	
	salm_spikes = world.get_location("Dunes: Across Spikes Above Salm")
	world.set_rule(salm_spikes, rb.HasAll("Wall Jump", "Scarbyttle Biomorph"))
	
	spike_maze = world.get_location("Dunes: Spike Maze Scargato")
	world.set_rule(spike_maze, wall_jump)
	
	# Mind's Desire Arena has a Klerek you can biomorph in it
	light_puzzle = world.get_location("Dunes: Light Puzzle Near Miratos")
	world.set_rule(light_puzzle, wall_jump)
	
	klerek_10 = world.get_location("Klerek 10")
	world.set_rule(klerek_10, wall_jump)
	
	def biomorph_location_logic(monster, monster_plural, thresholds):
		for n in thresholds:
			loc = world.get_location(f"Biomorphs: {n} {monster_plural}")
			world.set_rule(loc, rb.Has(f"{monster} Progress", n))
			
	biomorph_location_logic("Fubirang", "Fubirangs", (6,))
	biomorph_location_logic("Scarbyttle", "Scarbyttles", (6, 12))
	biomorph_location_logic("Toroth", "Toroths", (5, 10, 14))
	biomorph_location_logic("Sorios", "Sorios", (3, 5, 8))
	biomorph_location_logic("Klerek", "Klereks", (4, 7))
	
	world.set_completion_rule(rb.Has("Goal"))