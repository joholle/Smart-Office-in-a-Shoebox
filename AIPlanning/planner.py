from pddl.logic import Predicate
from pddl.logic.functions import (
    EqualTo,
    GreaterEqualThan,
    GreaterThan,
    Increase,
    LesserEqualThan,
    LesserThan,
    NumericFunction,
    NumericValue,
)
from pddl.logic.base import And, Not
from pddl.core import Domain, Problem
from pddl.action import Action
from pddl.formatter import domain_to_string, problem_to_string
from pddl.requirements import Requirements

# set up variables and constants

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

# light actions
turn_on_light = Action(
    "turn_on_light",
    parameters=[],
    precondition=LesserThan(light, NumericValue(10)) & Not(light_on()),
    effect=light_on&light_action_done
)
force_on_light = Action(
    "force_on_light",
    parameters=[],
    precondition=Not(light_on) & force_light,
    effect=light_on&light_action_done
)
force_off_light = Action(
    "force_off_light",
    parameters=[],
    precondition=(light_on & force_light),
    effect=Not(light_on)&light_action_done
)
# window actions
open_window = Action(
    "open_window",
    parameters=[],
    precondition=(GreaterThan(humidity, NumericValue(10)) | GreaterThan(inside_temp, NumericValue(10))) & Not(is_raining) & GreaterThan(inside_temp, outside_temp) & Not(windows_open),
    effect=windows_open&window_action_done
)
close_window = Action(
    "close_window",
    parameters=[],
    precondition=(LesserThan(humidity, NumericValue(10))&LesserThan(inside_temp, NumericValue(10))&windows_open)|(is_raining&windows_open),
    effect=Not(windows_open)&window_action_done
)
force_open_window = Action(
    "force_open_window",
    parameters=[],
    precondition=Not(windows_open) & force_window,
    effect=windows_open&window_action_done
)
force_close_window = Action(
    "force_close_window",
    parameters=[],
    precondition=windows_open & force_window,
    effect=Not(windows_open)&window_action_done
)
# cooler actions
turn_on_cooler = Action(
    "turn_on_cooler",
    parameters=[],
    precondition=(LesserThan(inside_temp, NumericValue(10))|GreaterThan(inside_temp, outside_temp))&Not(air_cooler_on),
    effect=air_cooler_on&cooler_action_done
)
turn_off_cooler = Action(
    "turn_off_cooler",
    parameters=[],
    precondition=(GreaterThan(inside_temp, NumericValue(10))|LesserThan(inside_temp, outside_temp))&air_cooler_on,
    effect=Not(air_cooler_on)&cooler_action_done
)
force_turn_on_cooler = Action(
    "force_turn_on_cooler",
    parameters=[],
    precondition=Not(air_cooler_on)&force_cooler,
    effect=air_cooler_on&cooler_action_done
)
force_turn_off_cooler = Action(
    "force_turn_off_cooler",
    parameters=[],
    precondition=air_cooler_on&force_cooler,
    effect=Not(air_cooler_on)&cooler_action_done
)
# water actions
fill_up_water = Action(
    "fill_up_water",
    parameters=[],
    precondition=EqualTo(water_level, NumericValue(0))&Not(water_spender_on),
    effect=water_spender_on&water_action_done
)
stop_water = Action(
    "stop_water",
    parameters=[],
    precondition=GreaterThan(water_level, NumericValue(10))&water_spender_on,
    effect=Not(water_spender_on)&water_action_done
)
force_fill_up_water = Action(
    "stop_water",
    parameters=[],
    precondition=Not(water_spender_on)&force_water,
    effect=water_spender_on&water_action_done
)
# no action (negation of all preconditions)
no_action = Action(
    "no_action",
    parameters=[],
    precondition=Not(
        # no light action possible
        (LesserThan(light, NumericValue(10)) & Not(light_on())) |
        (Not(light_on) & force_light) |
        ((light_on & force_light)) |

        # no window action possible
        ((GreaterThan(humidity, NumericValue(10)) | GreaterThan(inside_temp, NumericValue(10))) & Not(is_raining) & GreaterThan(inside_temp, outside_temp) & Not(windows_open)) |
        ((LesserThan(humidity, NumericValue(10))&LesserThan(inside_temp, NumericValue(10))&windows_open)|(is_raining&windows_open)) |
        (Not(windows_open) & force_window) |
        (windows_open & force_window) |

        # no cooler action possible
        ((LesserThan(inside_temp, NumericValue(10))|GreaterThan(inside_temp, outside_temp))&Not(air_cooler_on)) |
        ((GreaterThan(inside_temp, NumericValue(10))|LesserThan(inside_temp, outside_temp))&air_cooler_on) |
        (Not(air_cooler_on)&force_cooler) |
        (air_cooler_on&force_cooler) |

        # no water action possible
        (EqualTo(water_level, NumericValue(0))&Not(water_spender_on)) |
        (GreaterThan(water_level, NumericValue(10))&water_spender_on) |
        (Not(water_spender_on)&force_water)
    ),
    effect=no_action_possible
)

# define the domain object.
requirements = [Requirements.STRIPS, Requirements.TYPING, Requirements.CONDITIONAL_EFFECTS, Requirements.NEG_PRECONDITION, Requirements.EQUALITY, Requirements.DIS_PRECONDITION, Requirements.FLUENTS]
domain = Domain("office_room",
                requirements=requirements,
                predicates=[light_on, windows_open, air_cooler_on, water_spender_on,
                            force_light, force_window, force_cooler, force_water,
                            is_raining,
                            light_action_done, window_action_done, water_action_done, cooler_action_done, 
                            no_action_possible],
                functions={light: None, humidity: None, inside_temp: None, water_level: None,
                           outside_temp: None},
                actions=[turn_on_light, force_on_light, force_off_light,
                         open_window, close_window, force_open_window, force_close_window,
                         turn_on_cooler, turn_off_cooler, force_turn_on_cooler, force_turn_off_cooler,
                         fill_up_water, stop_water, force_fill_up_water,
                         no_action]
                )

domain_file = open("domain.pddl", "w")
domain_file.write(domain_to_string(domain))
domain_file.close()


problem = Problem(
    "pleasant_office_room",
    domain=domain,
    requirements=requirements,
    init={
        # sensor values 
        EqualTo(light, NumericValue(5)), 
        EqualTo(humidity, NumericValue(5)),
        EqualTo(inside_temp, NumericValue(5)),
        EqualTo(water_level, NumericValue(5)),
        # weather api
        EqualTo(outside_temp, NumericValue(5)),
        # user inputs
        Not(force_light),
        Not(force_window),
        Not(force_cooler),
        Not(force_water),
        # current status
        light_on,
        windows_open,
        air_cooler_on,
        water_spender_on
    },
    goal=light_action_done|window_action_done|water_action_done|cooler_action_done|no_action_possible
)

problem_file = open("problem.pddl", "w")
problem_file.write(problem_to_string(problem))
problem_file.close()