from pddl.logic.functions import (
    EqualTo,
    GreaterThan,
    LesserThan,
    NumericValue,
)
from pddl.logic.base import Not
from pddl.action import Action

from AIPlanning.logic import *

# light actions
turn_on_light = Action(
    "turn_on_light",
    parameters=[],
    precondition=LesserThan(light, NumericValue(200)) & Not(light_on) & EqualTo(force_light, NumericValue(1)),
    effect=light_on&light_action_done
)
force_on_light = Action(
    "force_on_light",
    parameters=[],
    precondition=Not(light_on) & EqualTo(force_light, NumericValue(2)),
    effect=light_on&light_action_done
)
force_off_light = Action(
    "force_off_light",
    parameters=[],
    precondition=light_on & EqualTo(force_light, NumericValue(0)),
    effect=Not(light_on)&light_action_done
)
# window actions
open_window = Action(
    "open_window",
    parameters=[],
    precondition=(GreaterThan(humidity, NumericValue(10)) | GreaterThan(inside_temp, NumericValue(10))) & Not(is_raining) & GreaterThan(inside_temp, outside_temp) & Not(windows_open)  & EqualTo(force_window, NumericValue(1)),
    effect=windows_open&window_action_done
)
close_window = Action(
    "close_window",
    parameters=[],
    precondition=(LesserThan(humidity, NumericValue(10))&LesserThan(inside_temp, NumericValue(10))&windows_open)|(GreaterThan(water_level, NumericValue(0))&is_raining&windows_open)|(LesserThan(inside_temp, outside_temp)&windows_open) & EqualTo(force_window, NumericValue(1)),
    effect=Not(windows_open)&window_action_done
)
force_open_window = Action(
    "force_open_window",
    parameters=[],
    precondition=Not(windows_open) & EqualTo(force_window, NumericValue(2)),
    effect=windows_open&window_action_done
)
force_close_window = Action(
    "force_close_window",
    parameters=[],
    precondition=windows_open & EqualTo(force_window, NumericValue(0)),
    effect=Not(windows_open)&window_action_done
)
# cooler actions
turn_on_cooler = Action(
    "turn_on_cooler",
    parameters=[],
    precondition=GreaterThan(inside_temp, NumericValue(10))&LesserThan(inside_temp, outside_temp)&Not(air_cooler_on) & EqualTo(force_cooler, NumericValue(1)),
    effect=air_cooler_on&cooler_action_done
)
turn_off_cooler = Action(
    "turn_off_cooler",
    parameters=[],
    precondition=(LesserThan(inside_temp, NumericValue(10))|GreaterThan(inside_temp, outside_temp))&air_cooler_on & EqualTo(force_cooler, NumericValue(1)),
    effect=Not(air_cooler_on)&cooler_action_done
)
force_turn_on_cooler = Action(
    "force_turn_on_cooler",
    parameters=[],
    precondition=Not(air_cooler_on) & EqualTo(force_cooler, NumericValue(2)),
    effect=air_cooler_on&cooler_action_done
)
force_turn_off_cooler = Action(
    "force_turn_off_cooler",
    parameters=[],
    precondition=air_cooler_on & EqualTo(force_cooler, NumericValue(0)),
    effect=Not(air_cooler_on)&cooler_action_done
)
# water actions
# fill_up_water = Action(
#     "fill_up_water",
#     parameters=[],
#     precondition=EqualTo(water_level, NumericValue(0))&Not(water_spender_on),
#     effect=water_spender_on&water_action_done
# )
# stop_water = Action(
#     "stop_water",
#     parameters=[],
#     precondition=GreaterThan(water_level, NumericValue(10))&water_spender_on,
#     effect=Not(water_spender_on)&water_action_done
# )
# force_fill_up_water = Action(
#     "stop_water",
#     parameters=[],
#     precondition=Not(water_spender_on)&force_water,
#     effect=water_spender_on&water_action_done
# )


# no action (negation of all preconditions)
no_action = Action(
    "no_action",
    parameters=[],
    precondition=Not(
        # no light action possible
        (LesserThan(light, NumericValue(200)) & Not(light_on) & EqualTo(force_light, NumericValue(1))) |
        (Not(light_on) & EqualTo(force_light, NumericValue(2))) |
        (light_on & EqualTo(force_light, NumericValue(0))) |

        # no window action possible
        ((GreaterThan(humidity, NumericValue(10)) | GreaterThan(inside_temp, NumericValue(10))) & Not(is_raining) & GreaterThan(inside_temp, outside_temp) & Not(windows_open)  & EqualTo(force_window, NumericValue(1))) |
        ((LesserThan(humidity, NumericValue(10))&LesserThan(inside_temp, NumericValue(10))&windows_open)|(GreaterThan(water_level, NumericValue(0))&is_raining&windows_open)|(LesserThan(inside_temp, outside_temp)&windows_open) & EqualTo(force_window, NumericValue(1))) |
        (Not(windows_open) & EqualTo(force_window, NumericValue(2))) |
        (windows_open & EqualTo(force_window, NumericValue(0))) |

        # no cooler action possible
        (GreaterThan(inside_temp, NumericValue(10))&LesserThan(inside_temp, outside_temp)&Not(air_cooler_on) & EqualTo(force_cooler, NumericValue(1))) |
        ((LesserThan(inside_temp, NumericValue(10))|GreaterThan(inside_temp, outside_temp))&air_cooler_on & EqualTo(force_cooler, NumericValue(1))) |
        (Not(air_cooler_on) & EqualTo(force_cooler, NumericValue(2))) |
        (air_cooler_on & EqualTo(force_cooler, NumericValue(0))) #|

        # no water action possible
       # (EqualTo(water_level, NumericValue(0))&Not(water_spender_on)) |
       # (GreaterThan(water_level, NumericValue(10))&water_spender_on) |
       # (Not(water_spender_on)&force_water)
    ),
    effect=no_action_possible
)