from mqtt.mqtt import MQTT
from interfaceSC import Interface
import json, time
from AIPlanning.planner import Planner
import requests
from Tester import Tester

class Laptop:
    def __init__(self):
        self.mqtt = MQTT("Laptop", "masterpi", "laptop_channel", "pi_channel")
        self.id = 0
        self.old_messages = []
        self.outside_temp = 20
        self.is_raining = False


        self.planner = Planner()
        self.internal_state = { "light_on" : False,
                                "windows_open" : False,
                                "air_cooler_on" : False
                                }

        self.tester = Tester()
        self.tester.start()

        self.interface = Interface()
        self.interface.start_loop(self.update)


    def update(self):
        # get weather api data
        try:
            response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=48.783333&lon=9.183333&appid=0e6e446d1e4dba85c052351ca6b2bf40&units=metric")
            response.raise_for_status()
            weather_api = response.json()
            self.outside_temp = round(weather_api['main']['temp'])
            if "rain" in weather_api['weather'][0]['description'] or "thunderstorm" in weather_api['weather'][0]['description']:
                self.is_raining = True
            else: 
                self.is_raining = False
        except: 
            self.outside_temp = self.outside_temp
            self.is_raining = self.is_raining
        
        # get sensor readings
        readings = self.get_readings()
        if readings is None:
            return self.interface.update_status(self.update, readings)
        
        readings.update({
            "weather_temperature": self.outside_temp,
            "weather_conditions": "Raining" if self.is_raining else "Clear"
        })

        # get user interput for actuators from interface
        set_force_window, set_force_light, set_force_cooler = self.interface.get_manual_input()
        print(set_force_window, set_force_light, set_force_cooler)

        # get user interput for target values from interface
        target_temperature, target_humdity, target_light = self.interface.get_target_input()
        self.planner.update_domain(target_light, target_humdity, target_temperature, 20)

        # ----------------------------------------------- test values -----------------------------------------------
        # self.outside_temp, self.is_raining = self.tester.get_weather_api()
        # test_light, test_humidity, test_temperature, test_water = self.tester.get_sensor_data()
        # readings.update({
        #     "light": test_light,
        #     "humidity": test_humidity,
        #     "temperature": test_temperature,
        #     "water": test_water
        # })
        # set_force_window, set_force_light, set_force_cooler = self.tester.get_user_inputs()
        # self.planner.update_domain(150, 50, 25, 20)
        # -----------------------------------------------------------------------------------------------------------

        # process readings with pddl
        self.planner.update_problem(
            set_light=readings["light"], set_humidity=readings["humidity"], set_inside_temp=readings["temperature"], set_water_level=readings["water"], 
            set_outside_temp=self.outside_temp,
            set_is_raining=self.is_raining,
            set_force_light=set_force_light, set_force_window=set_force_window, set_force_cooler=set_force_cooler, # set_force_water=False,
            light_on_state=self.internal_state["light_on"], windows_open_state=self.internal_state["windows_open"], air_cooler_on_state=self.internal_state["air_cooler_on"], # water_spender_on_state=self.internal_state["water_spender_on"]
            )
        
        action = self.planner.solve()[0]

        print(str(action))

        self.update_state(action)

        self.interface.update_status(self.update, readings)

    def get_readings(self):
        if self.mqtt.on_message:
            received_message = self.mqtt.message
            if received_message != "" and received_message not in self.old_messages:
                self.old_messages.append(received_message)
                return json.loads(received_message)

    def update_state(self, action):
        self.interface.update_window_status(self.internal_state["windows_open"])
        self.interface.update_lights_status(self.internal_state["light_on"])
        self.interface.update_watercooling_status(self.internal_state["air_cooler_on"])
        if action == "turn_on_light" or action == "force_on_light":
            self.internal_state["light_on"] = True
            self.mqtt.publish(str(self.id) + " turn on lights")
            self.id += 1
        elif action == "force_off_light":
            self.internal_state["light_on"] = False
            self.mqtt.publish(str(self.id) + " turn off lights")
            self.id += 1
    
        elif action == "open_window" or action == "force_open_window":
            self.internal_state["windows_open"] = True
            self.mqtt.publish(str(self.id) + " open window")
            self.id += 1
        elif action == "close_window" or action == "force_close_window":
            self.internal_state["windows_open"] = False
            self.mqtt.publish(str(self.id) + " close window")
            self.id += 1

        elif action == "turn_on_cooler" or action == "force_turn_on_cooler":
            self.internal_state["air_cooler_on"] = True
            self.mqtt.publish(str(self.id) + " turn on airconditioner")
            self.id += 1
        elif action == "turn_off_cooler" or action == "force_turn_off_cooler":
            self.internal_state["air_cooler_on"] = False
            self.mqtt.publish(str(self.id) + " turn off airconditioner")
            self.id += 1

if __name__ == "__main__":
    laptop = Laptop()
