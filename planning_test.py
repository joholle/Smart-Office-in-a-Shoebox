from AIPlanning.planner import Planner
import time

planner = Planner()

internal_state = {  "light_on" : True,
                    "windows_open" : True,
                    "air_cooler_on" : True,
                    "water_spender_on" : True
                    }

def update_state(action):
    match action:
        case "turn_on_light":
            internal_state["light_on"] = True
        case "force_on_light":
            internal_state["light_on"] = True
        case "force_off_light":
            internal_state["light_on"] = False

        case "open_window":
            internal_state["windows_open"] = True
        case "close_window":
            internal_state["windows_open"] = False
        case "force_open_window":
            internal_state["windows_open"] = True
        case "force_close_window":
            internal_state["windows_open"] = False

        case "turn_on_cooler":
            internal_state["air_cooler_on"] = True
        case "turn_off_cooler":
            internal_state["air_cooler_on"] = False
        case "force_turn_on_cooler":
            internal_state["air_cooler_on"] = True
        case "force_turn_off_cooler":
            internal_state["air_cooler_on"] = False

        case "fill_up_water":
            internal_state["water_spender_on"] = True
        case "stop_water":
            internal_state["water_spender_on"] = False
        case "force_fill_up_water":
            internal_state["water_spender_on"] = True



while True:
    # get sensor data

    # get weather api data

    # get user input

    planner.update_problem(set_light=5, set_humidity=15, set_inside_temp=15, set_water_level=5, set_outside_temp=5,
                        set_is_raining=False,
                        set_force_light=False, set_force_window=False, set_force_cooler=False, set_force_water=False,
                        light_on_state=internal_state["light_on"], windows_open_state=internal_state["windows_open"], air_cooler_on_state=internal_state["air_cooler_on"], water_spender_on_state=internal_state["water_spender_on"]
                        )

    action = planner.solve()[0]

    print(action)

    update_state(action)

    print(internal_state)

    time.sleep(3)

    

    

