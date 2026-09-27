from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
import rule_builder.rules as rb
from .items import chargeless_weapons

def connect_regions(world):
	wall_jump = rb.Has("Wall Jump")
		
	opening = world.get_region("Opening")
	blightmoor = world.get_region("Blightmoor")
	opening.connect(blightmoor, "Title Drop")
	
	blightmoor_underground = world.get_region("Blightmoor Underground")
	blightmoor.connect(blightmoor_underground, "Over the Underground Wall", wall_jump)
	
	lab_revisit = world.get_region("Core's Lab Revisit")
	blightmoor.connect(lab_revisit, "Boat Ride", wall_jump)
	
	skyway = world.get_region("Mezzo Skyway")
	blightmoor.connect(skyway, "Door to Mezzo Skyway",
		rb.HasAll("Ferrosculating Fluxograph", "Tracking Center Blueprint", "S.A.F.E. Kit"))
	
	skyway_lower_right = world.get_region("Mezzo Skyway Lower Right")
	skyway.connect(skyway_lower_right, "Skyway Lower Right Wall Climb", wall_jump)
	
	goal = world.get_region("Goal Region")
	skyway_lower_right.connect(goal, "Dunes Upper Left Entrance")
	skyway.connect(goal, "Dunes Entrance", rb.HasAny(*chargeless_weapons))
	
	biomorphs = world.get_region("Biomorph Unlocks")
	opening.connect(biomorphs, "Defeat First Toroth")
	
def location_logic(world):
	wall_jump = rb.Has("Wall Jump")
	
	lab_scargato = world.get_location("Core's Lab: Scargato")
	world.set_rule(lab_scargato, wall_jump)
	
	harlo_roof_scargato = world.get_location("Blightmoor: Scargato on Harlo's Roof")
	world.set_rule(harlo_roof_scargato, wall_jump)
	
	boyd_1 = world.get_location("Blightmoor: Boyd (return the wrench)")
	world.set_rule(boyd_1, rb.Has("Ferrosculating Fluxograph"))
	
	boyd_2 = world.get_location("Blightmoor: Boyd (tracking center 1)")
	world.set_rule(boyd_2, rb.Has("Tracking Center Blueprint") & rb.CanReachLocation(boyd_1.name))
	
	boyd_3 = world.get_location("Blightmoor: Boyd (upgrade the safe)")
	world.set_rule(boyd_3, rb.Has("S.A.F.E. Kit") & rb.CanReachLocation(boyd_2.name))
	
	boyd_4 = world.get_location("Blightmoor: Boyd (tracking center 2)")
	world.set_rule(boyd_4, rb.Has("Tracking Center Blueprint", 2))
	
	marle = world.get_location("Blightmoor: Marle Kertar (build the shop)")
	world.set_rule(marle, rb.Has("Restorer's Shop Blueprint"))
	
	meed = world.get_location("Blightmoor: Meed (get the blueprint)")
	world.set_rule(meed, rb.Has("Letter-Tapper Relic") & rb.CanReachRegion("Mezzo Skyway"))
	
	will_blightmoor = world.get_location("Blightmoor: Will")
	world.set_rule(will_blightmoor, rb.CanReachLocation("Mezzo: Will"))
	
	mezzo_boss = world.get_location("Mezzo: Gorgerzer Reward")
	world.set_rule(mezzo_boss, rb.HasAny(*chargeless_weapons))
	
	fubirang_1 = world.get_location("Biomorphs: 6 Fubirangs")
	world.set_rule(fubirang_1, rb.Has("Fubirang Progress", 6))
	
	scarbyttle_1 = world.get_location("Biomorphs: 6 Scarbyttles")
	world.set_rule(scarbyttle_1, rb.Has("Scarbyttle Progress", 6))
	
	scarbyttle_2 = world.get_location("Biomorphs: 12 Scarbyttles")
	world.set_rule(scarbyttle_2, rb.Has("Scarbyttle Progress", 12))
	
	secret_highway = world.get_location("Mezzo: Secret Highway Arena")
	world.set_rule(secret_highway, rb.HasAny(*chargeless_weapons))
	
	world.set_completion_rule(rb.Has("Goal"))