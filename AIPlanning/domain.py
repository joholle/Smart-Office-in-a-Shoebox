import pddl.core as pddl_core

from AIPlanning.logic import *
import AIPlanning.actions as actions
from AIPlanning.requirements import *

import importlib
import json

class Domain:
    def __init__(self):
        self.core = self.create()

    def create(self) -> pddl_core.Domain:
        domain = pddl_core.Domain("office_room",
                requirements=requirements,
                predicates=[light_on, windows_open, air_cooler_on, #water_spender_on,
                            is_raining,
                            light_action_done, window_action_done, cooler_action_done, #water_action_done,  
                            no_action_possible,
                            z_end_predicate],
                functions={light: None, humidity: None, inside_temp: None, water_level: None,
                           outside_temp: None,
                           force_light: None, force_window: None, force_cooler: None, #force_water: None
                           },
                actions=[actions.turn_on_light, actions.force_on_light, actions.force_off_light,
                         actions.open_window, actions.close_window, actions.force_close_window, actions.force_open_window,
                         actions.turn_on_cooler, actions.turn_off_cooler, actions.force_turn_on_cooler, actions.force_turn_off_cooler,
                         actions.no_action]
                )

        return domain
    
    def set_thresholds(self, light, humidity, temperature, water_level):
        # print("threshholds: " + str(light) + " " + str(humidity) + " " + str(temperature) + " " + str(water_level))
        # LIGHT_THRESHOLD = light
        # HUMIDITY_THRESHOLD = humidity
        # TEMPERATURE_THRESHOLD = temperature
        # WATER_LEVEL_THRESHOLD = water_level

        thresholds = {
            "LIGHT_THRESHOLD": light,
            "HUMIDITY_THRESHOLD": humidity,
            "TEMPERATURE_THRESHOLD": temperature,
            "WATER_LEVEL_THRESHOLD": water_level
        }

        with open("AIPlanning/THRESHOLDS.json", "w") as json_file:
            json.dump(thresholds, json_file)

        importlib.reload(actions)

