from pddl.logic import Predicate
from pddl.logic.functions import (
    NumericFunction,
)

# define predicates
light_on = Predicate("light_on")
windows_open = Predicate("windows_open")
air_cooler_on = Predicate("air_cooler_on")
water_spender_on = Predicate("water_spender_on")

force_light = Predicate("force_light")
force_window = Predicate("force_window")
force_cooler = Predicate("force_cooler")
force_water = Predicate("force_water")

is_raining = Predicate("is_raining")

light_action_done = Predicate("light_action_done")
window_action_done = Predicate("window_action_done")
water_action_done = Predicate("water_action_done")
cooler_action_done = Predicate("cooler_action_done")

no_action_possible = Predicate("no_action_possible")

# define functions
light = NumericFunction("light")
humidity = NumericFunction("humidity")
inside_temp = NumericFunction("inside_temp")
water_level = NumericFunction("water_level")

outside_temp = NumericFunction("outside_temp")

