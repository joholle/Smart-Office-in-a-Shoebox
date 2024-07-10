from AIPlanning.planner import Planner

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



# while True:
#     # get sensor data

#     # get weather api data

#     # get user input

#     planner.update_problem(set_light=5, set_humidity=15, set_inside_temp=15, set_water_level=5, set_outside_temp=5,
#                         set_is_raining=False,
#                         set_force_light=False, set_force_window=False, set_force_cooler=False, set_force_water=False,
#                         light_on_state=internal_state["light_on"], windows_open_state=internal_state["windows_open"], air_cooler_on_state=internal_state["air_cooler_on"], water_spender_on_state=internal_state["water_spender_on"]
#                         )

#     action = planner.solve()[0]

#     print(action)

#     update_state(action)

#     print(internal_state)

#     time.sleep(3)

import time
    
class Tester:
    def __init__(self):
        self.light = 200
        self.humidity = 70
        self.inside_temp = 20 
        self.water_level = 0

        self.outside_temp = 20
        self.is_raining = False

        self.force_light = 1
        self.force_window = 1
        self.force_cooler = 1
    
    def set_sensor_data(self, light=None, humidity=None, inside_temp=None, water_level=None):
        if light != None: self.light = light
        if humidity != None: self.humidity = humidity
        if inside_temp != None: self.inside_temp = inside_temp 
        if water_level != None: self.water_level = water_level
    
    def set_weather_api(self, outside_temp=None, is_raining=None):
        if outside_temp != None: self.outside_temp = outside_temp
        if is_raining != None: self.is_raining = is_raining
    
    def set_user_inputs(self, force_light=None, force_window=None, force_cooler=None):
        if force_light != None: self.force_light = force_light
        if force_window != None: self.force_window = force_window
        if force_cooler != None: self.force_cooler = force_cooler

    def get_sensor_data(self):
        return self.light, self.humidity, self.inside_temp, self.water_level
    
    def get_weather_api(self):
        return self.outside_temp, self.is_raining
    
    def get_user_inputs(self):
        return self.force_light, self.force_window, self.force_cooler

    def run(self):
        time.sleep(3)

        # light test 
        self.set_sensor_data(light=100)
        time.sleep(3)
        self.set_user_inputs(force_light=0)
        time.sleep(3)
        self.set_sensor_data(light=200)
        self.set_user_inputs(force_light=1)
        time.sleep(3)

        # window test
        self.set_sensor_data(inside_temp=30)
        self.set_weather_api(outside_temp=20)
        time.sleep(3)
        self.set_user_inputs(force_window=0)
        time.sleep(3)
        self.set_sensor_data(inside_temp=20)
        self.set_weather_api(outside_temp=20)
        self.set_user_inputs(force_window=1)
        time.sleep(3)

        # cooler test
        self.set_sensor_data(inside_temp=30)
        self.set_weather_api(outside_temp=40)
        time.sleep(3)
        self.set_user_inputs(force_cooler=0)
        time.sleep(3)
        self.set_sensor_data(inside_temp=20)
        self.set_weather_api(outside_temp=20)
        self.set_user_inputs(force_cooler=1)
        time.sleep(3)

        # rain test
        self.set_sensor_data(inside_temp=30)
        self.set_weather_api(outside_temp=20)
        time.sleep(3)
        self.set_sensor_data(water_level=100)
        self.set_weather_api(is_raining=True)
        time.sleep(3)
        self.set_user_inputs(force_windows=2)
        time.sleep(3)
        self.set_sensor_data(inside_temp=20, water_level=0)
        self.set_weather_api(outside_temp=20, is_raining=False)
        self.set_user_inputs(force_windows=1)
        time.sleep(3)
    

