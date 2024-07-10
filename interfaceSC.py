import tkinter as tk
from tkinter import ttk
from arduinoSerial import ArduinoSerial

class Interface:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Sensor and Actuator Status")
        self.root.configure(bg="#E6E6FA")

        # Create StringVar variables to hold the status text
        self.humidity = tk.StringVar()
        self.water = tk.StringVar()
        self.temperature = tk.StringVar()
        self.light = tk.StringVar()
        self.window_status = tk.StringVar()
        self.lights_status = tk.StringVar()
        self.watercooling_status = tk.StringVar()
        self.weather_temperature = tk.StringVar()
        self.weather_conditions = tk.StringVar()

        # Create frames for sensors, actuators, and weather
        self.sensor_frame = ttk.LabelFrame(self.root, text="Sensors", padding=(10, 5))
        self.sensor_frame.grid(column=0, row=0, padx=10, pady=10, sticky='NSEW')

        self.actuator_frame = ttk.LabelFrame(self.root, text="Actuators", padding=(10, 5))
        self.actuator_frame.grid(column=1, row=0, padx=10, pady=10, sticky='NSEW')

        self.weather_frame = ttk.LabelFrame(self.root, text="Weather", padding=(10, 5))
        self.weather_frame.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky='NSEW')

        # Add sensor labels
        self.humidity_frame = ttk.LabelFrame(self.sensor_frame, text="Humidity", padding=(5, 5))
        self.humidity_frame.grid(column=0, row=0, padx=5, pady=5, sticky='NSEW')
        self.humidity_label = ttk.Label(self.humidity_frame, textvariable=self.humidity, font=("Helvetica", 12))
        self.humidity_label.pack(padx=10, pady=10)

        self.water_frame = ttk.LabelFrame(self.sensor_frame, text="Water Level", padding=(5, 5))
        self.water_frame.grid(column=0, row=1, padx=5, pady=5, sticky='NSEW')
        self.water_label = ttk.Label(self.water_frame, textvariable=self.water, font=("Helvetica", 12))
        self.water_label.pack(padx=10, pady=10)

        self.temperature_frame = ttk.LabelFrame(self.sensor_frame, text="Temperature", padding=(5, 5))
        self.temperature_frame.grid(column=0, row=2, padx=5, pady=5, sticky='NSEW')
        self.temperature_label = ttk.Label(self.temperature_frame, textvariable=self.temperature, font=("Helvetica", 12))
        self.temperature_label.pack(padx=10, pady=10)

        self.light_frame = ttk.LabelFrame(self.sensor_frame, text="Light Intensity", padding=(5, 5))
        self.light_frame.grid(column=0, row=3, padx=5, pady=5, sticky='NSEW')
        self.light_label = ttk.Label(self.light_frame, textvariable=self.light, font=("Helvetica", 12))
        self.light_label.pack(padx=10, pady=10)

        # Add actuator controls
        self.window_frame = ttk.LabelFrame(self.actuator_frame, text="Windows", padding=(5, 5))
        self.window_frame.grid(column=0, row=0, padx=5, pady=5, sticky='NSEW')

        # Add labels above the slider using grid
        self.window_close_label = tk.Label(self.window_frame, text="Close", font=("Helvetica", 8))
        self.window_close_label.grid(column=0, row=0, padx=5)

        self.window_default_label = tk.Label(self.window_frame, text="Default", font=("Helvetica", 8))
        self.window_default_label.grid(column=1, row=0, padx=5)

        self.window_open_label = tk.Label(self.window_frame, text="Open", font=("Helvetica", 8))
        self.window_open_label.grid(column=2, row=0, padx=5)

        # Add the slider for window control using grid
        self.window_slider = tk.Scale(self.window_frame, from_=0, to=2, orient='horizontal', length=200, showvalue=False, command=self.window_status)
        self.window_slider.grid(column=0, row=1, columnspan=3, padx=5, pady=5)
        self.window_slider.set(1)  # Set to default

        self.window_status_label = ttk.Label(self.window_frame, textvariable=self.window_status, font=("Helvetica", 12))
        self.window_status_label.grid(column=0, row=2, columnspan=3, padx=5, pady=5)

        self.lights_frame = ttk.LabelFrame(self.actuator_frame, text="Lights", padding=(5, 5))
        self.lights_frame.grid(column=0, row=1, padx=5, pady=5, sticky='NSEW')

        # Add labels above the slider using grid for lights
        self.lights_off_label = tk.Label(self.lights_frame, text="Off", font=("Helvetica", 8))
        self.lights_off_label.grid(column=0, row=0, padx=5)

        self.lights_default_label = tk.Label(self.lights_frame, text="Default", font=("Helvetica", 8))
        self.lights_default_label.grid(column=1, row=0, padx=5)

        self.lights_on_label = tk.Label(self.lights_frame, text="On", font=("Helvetica", 8))
        self.lights_on_label.grid(column=2, row=0, padx=5)

        # Add the slider for lights control using grid
        self.lights_slider = tk.Scale(self.lights_frame, from_=0, to=2, orient='horizontal', length=200, showvalue=False, command=self.lights_status)
        self.lights_slider.grid(column=0, row=1, columnspan=3, padx=5, pady=5)
        self.lights_slider.set(1)  # Set to default

        self.lights_status_label = ttk.Label(self.lights_frame, textvariable=self.lights_status, font=("Helvetica", 12))
        self.lights_status_label.grid(column=0, row=2, columnspan=3, padx=5, pady=5)

        self.watercooling_frame = ttk.LabelFrame(self.actuator_frame, text="Air Conditioning", padding=(5, 5))
        self.watercooling_frame.grid(column=0, row=2, padx=5, pady=5, sticky='NSEW')

        # Add labels above the slider using grid for air conditioning
        self.cooling_off_label = tk.Label(self.watercooling_frame, text="Off", font=("Helvetica", 8))
        self.cooling_off_label.grid(column=0, row=0, padx=5)

        self.cooling_default_label = tk.Label(self.watercooling_frame, text="Default", font=("Helvetica", 8))
        self.cooling_default_label.grid(column=1, row=0, padx=5)

        self.cooling_on_label = tk.Label(self.watercooling_frame, text="On", font=("Helvetica", 8))
        self.cooling_on_label.grid(column=2, row=0, padx=5)

        # Add the slider for air conditioning control using grid
        self.cooling_slider = tk.Scale(self.watercooling_frame, from_=0, to=2, orient='horizontal', length=200, showvalue=False, command=self.watercooling_status)
        self.cooling_slider.grid(column=0, row=1, columnspan=3, padx=5, pady=5)
        self.cooling_slider.set(1)  # Set to default

        self.watercooling_status_label = ttk.Label(self.watercooling_frame, textvariable=self.watercooling_status, font=("Helvetica", 12))
        self.watercooling_status_label.grid(column=0, row=2, columnspan=3, padx=5, pady=5)

        # Add weather labels
        self.weather_temperature_frame = ttk.LabelFrame(self.weather_frame, text="Temperature", padding=(5, 5))
        self.weather_temperature_frame.grid(column=0, row=0, padx=5, pady=5, sticky='NSEW')
        self.weather_temperature_label = ttk.Label(self.weather_temperature_frame, textvariable=self.weather_temperature, font=("Helvetica", 12))
        self.weather_temperature_label.pack(padx=10, pady=10)

        self.weather_conditions_frame = ttk.LabelFrame(self.weather_frame, text="Conditions", padding=(5, 5))
        self.weather_conditions_frame.grid(column=1, row=0, padx=5, pady=5, sticky='NSEW')
        self.weather_conditions_label = ttk.Label(self.weather_conditions_frame, textvariable=self.weather_conditions, font=("Helvetica", 12))
        self.weather_conditions_label.pack(padx=10, pady=10)

        # Configure column and row weights to make widgets resize proportionally
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.sensor_frame.grid_rowconfigure(0, weight=1)
        self.sensor_frame.grid_rowconfigure(1, weight=1)
        self.sensor_frame.grid_rowconfigure(2, weight=1)
        self.sensor_frame.grid_rowconfigure(3, weight=1)
        self.sensor_frame.grid_columnconfigure(0, weight=1)

        self.actuator_frame.grid_rowconfigure(0, weight=1)
        self.actuator_frame.grid_rowconfigure(1, weight=1)
        self.actuator_frame.grid_rowconfigure(2, weight=1)
        self.actuator_frame.grid_columnconfigure(0, weight=1)

        self.weather_frame.grid_columnconfigure(0, weight=1)
        self.weather_frame.grid_columnconfigure(1, weight=1)

        # Apply style settings
        style = ttk.Style()
        style.configure("TFrame", background="#E6E6FA")
        style.configure("TLabel")
        style.configure("TLabelFrame", background="#9370DB", foreground="#FFFFFF", borderwidth=2, relief="solid")
        style.configure("TButton", background="#9370DB", foreground="#FFFFFF", font=("Helvetica", 10, "bold"))

        # Initialize actuator status
        self.set_window_status("Default")
        self.set_lights_status("Default")
        self.set_watercooling_status("Default")

    def start_loop(self, function):
        # Call the update_status function to initialize the status updates
        self.update_status(function, {"humidity": 0, "water": 0, "temperature": 0, "light": 0, "weather_temperature": 0, "weather_conditions": ""})

        # Start the Tkinter event loop
        self.root.mainloop()

    # Function to update the sensor and actuator status
    def update_status(self, function, sensor_data):
        if sensor_data is not None:
            self.humidity.set(str(sensor_data["humidity"]))
            self.water.set(str(sensor_data["water"]))
            self.temperature.set(str(sensor_data["temperature"]) + "°C")
            self.light.set(str(sensor_data["light"]))
            self.weather_temperature.set(str(sensor_data["weather_temperature"]) + "°C")
            self.weather_conditions.set(sensor_data["weather_conditions"])

        # Update the status every second
        self.root.after(1000, function)

    # Function to update window status based on slider position
    # def update_window_status(self, value):
    #     value = int(value)
    #     if value == 0:
    #         self.set_window_status("Force Close")
    #     elif value == 1:
    #         self.set_window_status("Default")
    #     elif value == 2:
    #         self.set_window_status("Force Open")

    # # Function to update lights status based on slider position
    # def update_lights_status(self, value):
    #     value = int(value)
    #     if value == 0:
    #         self.set_lights_status("Force Off")
    #     elif value == 1:
    #         self.set_lights_status("Default")
    #     elif value == 2:
    #         self.set_lights_status("Force On")

    # # Function to update air conditioning status based on slider position
    # def update_watercooling_status(self, value):
    #     value = int(value)
    #     if value == 0:
    #         self.set_watercooling_status("Force Off")
    #     elif value == 1:
    #         self.set_watercooling_status("Default")
    #     elif value == 2:
    #         self.set_watercooling_status("Force On")

    # Callback functions to handle actuator status change
    def set_window_status(self, state):
        self.window_status.set(state)

    def set_lights_status(self, state):
        self.lights_status.set(state)

    def set_watercooling_status(self, state):
        self.watercooling_status.set(state)

    def get_manual_input(self):
        is_window_open = self.get_int_from_state(self.window_status.get())
        is_lights_on = self.get_int_from_state(self.lights_status.get())
        is_cooling_on = self.get_int_from_state(self.watercooling_status.get())
        return is_window_open, is_lights_on, is_cooling_on

    def get_int_from_state(self, state):
        if state in ["Force Close", "Force Off"]:
            return 0
        elif state in ["Default"]:
            return 1
        elif state in ["Force Open", "Force On"]:
            return 2
        else:
            print("invalid state")
            return -1

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_lights_status(self):
        return self.lights_status

    def get_water_level(self):
        return self.water

    def get_window_status(self):
        return self.window_status

    def get_watercooling_status(self):
        return self.watercooling_status

    def get_weather_temperature(self):
        return self.weather_temperature

    def get_weather_conditions(self):
        return self.weather_conditions