import pddl.core as pddl_core

from AIPlanning.logic import *
from AIPlanning.actions import *
from AIPlanning.requirements import * 

class Domain:
    def create(self) -> pddl_core.Domain:        
        domain = pddl_core.Domain("office_room",
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

        return domain