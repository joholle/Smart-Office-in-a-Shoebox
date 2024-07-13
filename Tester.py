import time
import datetime
    
class Tester:
    def __init__(self):
        self.light = 200
        self.humidity = 20
        self.inside_temp = 20 
        self.water_level = 0

        self.outside_temp = 20
        self.is_raining = False

        self.force_light = 1
        self.force_window = 1
        self.force_cooler = 1

        self.start_time = datetime.datetime.now()
        # self.start_time = int(time.time())
    
    def __set_sensor_data(self, light=None, humidity=None, inside_temp=None, water_level=None):
        if light != None: self.light = light
        if humidity != None: self.humidity = humidity
        if inside_temp != None: self.inside_temp = inside_temp 
        if water_level != None: self.water_level = water_level
    
    def __set_weather_api(self, outside_temp=None, is_raining=None):
        if outside_temp != None: self.outside_temp = outside_temp
        if is_raining != None: self.is_raining = is_raining
    
    def __set_user_inputs(self, force_light=None, force_window=None, force_cooler=None):
        if force_light != None: self.force_light = force_light
        if force_window != None: self.force_window = force_window
        if force_cooler != None: self.force_cooler = force_cooler

    def __set_test_data(self, current_time:datetime.time):
        seconds_passed = int((current_time - self.start_time).total_seconds())

        # print(seconds_passed)

        # light test
        if seconds_passed % 54 < 3:
            return
        elif seconds_passed % 54 < 6:
            self.__set_sensor_data(light=100)
        elif seconds_passed % 54 < 9:
            self.__set_user_inputs(force_light=0)
        elif seconds_passed % 54 < 12:
            self.__set_sensor_data(light=200)
            self.__set_user_inputs(force_light=1)

        # window test
        elif seconds_passed % 54 < 15:
            self.__set_sensor_data(inside_temp=30)
            self.__set_weather_api(outside_temp=20)
        elif seconds_passed % 54 < 18:
            self.__set_user_inputs(force_window=0)
        elif seconds_passed % 54 < 21:
            self.__set_sensor_data(inside_temp=20)
            self.__set_weather_api(outside_temp=20)
            self.__set_user_inputs(force_window=1)

        # cooler test
        elif seconds_passed % 54 < 24:
            self.__set_sensor_data(inside_temp=30)
            self.__set_weather_api(outside_temp=40)
        elif seconds_passed % 54 < 27:
            self.__set_user_inputs(force_cooler=0)
        elif seconds_passed % 54 < 30:
            self.__set_sensor_data(inside_temp=20)
            self.__set_weather_api(outside_temp=20)
            self.__set_user_inputs(force_cooler=1)

        # rain test
        elif seconds_passed % 54 < 33:
            self.__set_sensor_data(inside_temp=30)
            self.__set_weather_api(outside_temp=20)
        elif seconds_passed % 54 < 36:
            self.__set_sensor_data(water_level=100)
            self.__set_weather_api(is_raining=True)
        elif seconds_passed % 54 < 39:
            self.__set_user_inputs(force_window=2)
        elif seconds_passed % 54 < 42:
            self.__set_sensor_data(inside_temp=20, water_level=0)
            self.__set_weather_api(outside_temp=20, is_raining=False)
            self.__set_user_inputs(force_window=1)

        # humidity test
        elif seconds_passed % 54 < 54:
            self.__set_sensor_data(humidity=100)
        elif seconds_passed % 54 < 48:
            self.__set_user_inputs(force_window=0)
        elif seconds_passed % 54 < 51:
            self.__set_sensor_data(humidity=20)
            self.__set_user_inputs(force_window=1)

    def get_sensor_data(self):
        self.__set_test_data(datetime.datetime.now())
        return self.light, self.humidity, self.inside_temp, self.water_level
    
    def get_weather_api(self):
        self.__set_test_data(datetime.datetime.now())
        return self.outside_temp, self.is_raining
    
    def get_user_inputs(self):
        self.__set_test_data(datetime.datetime.now())
        return self.force_light, self.force_window, self.force_cooler

    def start(self):
        self.start_time = datetime.datetime.now()
        time.sleep(0.5)
