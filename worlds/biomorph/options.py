from Options import PerGameCommonOptions, Choice
from dataclasses import dataclass

class ReduceShopPrices(Choice):
	"""Whether to reduce some or all shop
	prices to 20% of their normal value.
	Choosing early will only reduce the
	prices of shop items that you could
	gain access to before getting out of
	Blightmoor."""
	
	option_none = 0
	option_early = 1
	option_all = 2
	
	default = option_early
	display_name = "Reduce Shop Prices"

class StartingWeapon(Choice):
	"""Choose any to have a completely random
	starting weapon, choose chargeless to have
	a random starting weapon limited to only
	the ones that can't run out of charges, 
	or choose a specific starting weapon.
	Use weights for a custom weapon pool."""

	option_any = 0
	option_chargeless = 1
	option_the_bruisers = 2
	option_the_executioner = 3
	option_pain_legion = 4
	option_shadow_sting = 5
	option_ferrox_specter = 6
	option_fubirang_biomorph = 7
	option_scarbyttle_biomorph = 8
	option_toroth_biomorph = 9
	option_sorios_biomorph = 10
	option_klerek_biomorph = 11
	
	default = option_any
	display_name = "Starting Weapon"
	

@dataclass
class BiomorphOptions(PerGameCommonOptions):
	starting_weapon: StartingWeapon
	reduce_shop_prices: ReduceShopPrices