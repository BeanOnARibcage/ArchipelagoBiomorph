from worlds.AutoWorld import World
from BaseClasses import Item, Location, Region, ItemClassification
import rule_builder.rules as rb

def connect_regions(world):
	opening = world.get_region("Opening")
	blightmoor = world.get_region("Blightmoor")
	opening.connect(blightmoor, "Title Drop")
	
	blightmoor_underground = world.get_region("Blightmoor Underground")
	blightmoor.connect(blightmoor_underground, "Over the Underground Wall",
		rb.Has("Wall Jump"))
	
	lab_revisit = world.get_region("Core's Lab Revisit")
	blightmoor.connect(lab_revisit, "Boat Ride", rb.Has("Wall Jump"))
	
def location_logic(world):
	lab_scargato = world.get_location("Core's Lab: Scargato")
	world.set_rule(lab_scargato, rb.Has("Wall Jump"))
	
	harlo_roof_scargato = world.get_location("Blightmoor: Scargato on Harlo's Roof")
	world.set_rule(harlo_roof_scargato, rb.Has("Wall Jump"))
	
	boyd_1 = world.get_location("Blightmoor: Boyd (return the wrench)")
	world.set_rule(boyd_1, rb.Has("Ferrosculating Fluxograph"))
	
	boyd_2 = world.get_location("Blightmoor: Boyd (tracking center 1)")
	world.set_rule(boyd_2, rb.Has("Tracking Center Blueprint") & rb.CanReachLocation(boyd_1.name))
	
	boyd_3 = world.get_location("Blightmoor: Boyd (upgrade the safe)")
	world.set_rule(boyd_3, rb.Has("S.A.F.E. Kit") & rb.CanReachLocation(boyd_2.name))
	
	world.set_completion_rule(rb.CanReachLocation(boyd_3.name))