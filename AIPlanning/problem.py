import pddl.core as pddl_core

from AIPlanning.logic import *
from AIPlanning.actions import *
from AIPlanning.requirements import * 

class Problem:
    def create(self, domain:pddl_core.Domain, 
               set_light:float, set_humidity:float, set_inside_temp:float, set_water_level:float, 
               set_outside_temp:float, 
               set_is_raining:bool, 
               set_force_light:int, set_force_window:int, set_force_cooler:int, # set_force_water:int, 
               light_on_state:bool, windows_open_state:bool, air_cooler_on_state:bool, # water_spender_on_state:bool
               ) -> pddl_core.Problem:
        
        # sensor values and weather api
        init = {
                # sensor data
                EqualTo(light, NumericValue(set_light)), 
                EqualTo(humidity, NumericValue(set_humidity)),
                EqualTo(inside_temp, NumericValue(set_inside_temp)),
                EqualTo(water_level, NumericValue(set_water_level)),
                # weather api
                EqualTo(outside_temp, NumericValue(set_outside_temp)),

                # user inputs
                EqualTo(force_light, NumericValue(set_force_light)), 
                EqualTo(force_window, NumericValue(set_force_window)),
                EqualTo(force_cooler, NumericValue(set_force_cooler))
            }
        # weather api
        init.add(is_raining) if set_is_raining else init.add(Not(is_raining))

        # current state
        init.add(light_on) if light_on_state else init.add(Not(light_on))
        init.add(windows_open) if windows_open_state else init.add(Not(windows_open))
        init.add(air_cooler_on) if air_cooler_on_state else init.add(Not(air_cooler_on))

        init.add(z_end_predicate)


        problem = pddl_core.Problem(
            "pleasant_office_room",
            domain=domain,
            requirements=requirements,
            init=init,
            goal=light_action_done|window_action_done|cooler_action_done|no_action_possible
        )
      
        return problem
