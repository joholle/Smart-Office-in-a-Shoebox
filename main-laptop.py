from pddl.pddl import PDDL
from mqtt.mqtt import MQTT
from interfaceSC import Interface
import json, time


# mqtt = MQTT("Laptop", "masterpi", "laptop_channel", "pi_channel")
# id = 0
# cycle = False
# while True:
#     if cycle:
#         mqtt.publish(str(id) + " open window")
#     else:
#         mqtt.publish(str(id) + " close window")
#     id += 1
#     cycle = not cycle
#     time.sleep(4)
# time.sleep(5)

# pddl = PDDL("AIPlanning/Domain.pddl", "AIPlanning/Problem.pddl")
# pddl.set_state(frozenset({('off', 'light1'), ('on', 'light2'), ('value-low', 'light_sensor'), ('value-low', 'light_sensor2')}))

# plan = pddl.plan()
# if plan != None:
#     for action in plan:
#         print(str(action))
        # mqtt.publish(json.loads(str(action)))

# print("DONE")


from AIPlanning.planner import Planner
import requests

class Laptop:
    def __init__(self):
        self.mqtt = MQTT("Laptop", "masterpi", "laptop_channel", "pi_channel")
        self.id = 0
        self.old_messages = []
        self.outside_temp = 20

        self.interface = Interface()
        self.interface.start_loop(self.update)

        self.planner = Planner()
        self.internal_state = { "light_on" : True,
                                "windows_open" : True,
                                "air_cooler_on" : True,
                                "water_spender_on" : True
                                }

    def update(self):
        readings = self.get_readings()

        try:
            response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=0e6e446d1e4dba85c052351ca6b2bf40&units=metric")
            response.raise_for_status()
            weather_api = response.json()
            self.outside_temp = weather_api['main']['temp']
        except: 
            self.outside_temp = self.outside_temp

        # process readings with pddl
        self.planner.update_problem(
            set_light=readings["light"], set_humidity=readings["humidity"], set_inside_temp=readings["temperature"], set_water_level=readings["water"], set_outside_temp=self.outside_temp,
            set_is_raining=False,
            set_force_light=False, set_force_window=False, set_force_cooler=False, set_force_water=False,
            light_on_state=self.internal_state["light_on"], windows_open_state=self.internal_state["windows_open"], air_cooler_on_state=self.internal_state["air_cooler_on"], water_spender_on_state=self.internal_state["water_spender_on"])
        
        action = self.planner.solve()[0]

        self.update_internal_state(action)

        # print action to mqtt with id

        self.interface.update_status(self.update, readings)

    def get_readings(self):
        if self.mqtt.on_message:
            received_message = self.mqtt.message
            if received_message != "" and received_message not in self.old_messages:
                self.old_messages.append(received_message)
                return json.loads(received_message)

    def update_internal_state(self, action):
        match action:
            case "turn_on_light":
                self.internal_state["light_on"] = True
            case "force_on_light":
                self.internal_state["light_on"] = True
            case "force_off_light":
                self.internal_state["light_on"] = False

            case "open_window":
                self.internal_state["windows_open"] = True
            case "close_window":
                self.internal_state["windows_open"] = False
            case "force_open_window":
                self.internal_state["windows_open"] = True
            case "force_close_window":
                self.internal_state["windows_open"] = False

            case "turn_on_cooler":
                self.internal_state["air_cooler_on"] = True
            case "turn_off_cooler":
                self.internal_state["air_cooler_on"] = False
            case "force_turn_on_cooler":
                self.internal_state["air_cooler_on"] = True
            case "force_turn_off_cooler":
                self.internal_state["air_cooler_on"] = False

            case "fill_up_water":
                self.internal_state["water_spender_on"] = True
            case "stop_water":
                self.internal_state["water_spender_on"] = False
            case "force_fill_up_water":
                self.internal_state["water_spender_on"] = True

if __name__ == "__main__":
    laptop = Laptop()

# Run interface
# every 5 seconds:
#   get sensor readings from arduino
#   create pddl plan by recieving info from mqtt
#   execute plan, by sending back to mqtt arduino
#   update interface