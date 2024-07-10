import pddl.core as pddl_core

from AIPlanning.logic import *
from AIPlanning.actions import *
from AIPlanning.requirements import * 

class Problem:
    def create(self, domain:pddl_core.Domain, 
               set_light:float, set_humidity:float, set_inside_temp:float, set_water_level:float, 
               set_outside_temp:float, 
               set_is_raining:bool, 
               set_force_light:bool, set_force_window:bool, set_force_cooler:bool, # set_force_water:bool, 
               light_on_state:bool, windows_open_state:bool, air_cooler_on_state:bool, # water_spender_on_state:bool
               ) -> pddl_core.Problem:
        
        # sensor values and weather api
        init = {
                EqualTo(light, NumericValue(set_light)), 
                EqualTo(humidity, NumericValue(set_humidity)),
                EqualTo(inside_temp, NumericValue(set_inside_temp)),
                EqualTo(water_level, NumericValue(set_water_level)),
                EqualTo(outside_temp, NumericValue(set_outside_temp))
            }
        init.add(is_raining) if set_is_raining else init.add(Not(is_raining))

        # user inputs
        init.add(force_light) if set_force_light else init.add(Not(force_light))
        init.add(force_window) if set_force_window else init.add(Not(force_window))
        init.add(force_cooler) if set_force_cooler else init.add(Not(force_cooler))
        # init.add(force_water) if set_force_water else init.add(Not(force_water))

        # current state
        init.add(light_on) if light_on_state else init.add(Not(light_on))
        init.add(windows_open) if windows_open_state else init.add(Not(windows_open))
        init.add(air_cooler_on) if air_cooler_on_state else init.add(Not(air_cooler_on))
        # init.add(water_spender_on) if water_spender_on_state else init.add(Not(water_spender_on))

        init.add(z_end_predicate)


        problem = pddl_core.Problem(
            "pleasant_office_room",
            domain=domain,
            requirements=requirements,
            init=init,
            goal=light_action_done|window_action_done|water_action_done|cooler_action_done|no_action_possible
        )
      
        return problem
