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
        self.beamer_status = tk.StringVar()
        self.watercooling_status = tk.StringVar()

        # Create frames for sensors and actuators
        self.sensor_frame = ttk.LabelFrame(self.root, text="Sensors", padding=(10, 5))
        self.sensor_frame.grid(column=0, row=0, padx=10, pady=10, sticky='NSEW')

        self.actuator_frame = ttk.LabelFrame(self.root, text="Actuators", padding=(10, 5))
        self.actuator_frame.grid(column=1, row=0, padx=10, pady=10, sticky='NSEW')

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
        self.window_open_button = tk.Button(self.window_frame, text="Open", command=lambda: self.set_window_status("Open"))
        self.window_open_button.pack(side="left", padx=5, pady=5)
        self.window_closed_button = tk.Button(self.window_frame, text="Closed", command=lambda: self.set_window_status("Closed"))
        self.window_closed_button.pack(side="left", padx=5, pady=5)

        self.beamer_frame = ttk.LabelFrame(self.actuator_frame, text="Beamer", padding=(5, 5))
        self.beamer_frame.grid(column=0, row=1, padx=5, pady=5, sticky='NSEW')
        self.beamer_on_button = tk.Button(self.beamer_frame, text="On", command=lambda: self.set_beamer_status("On"))
        self.beamer_on_button.pack(side="left", padx=5, pady=5)
        self.beamer_off_button = tk.Button(self.beamer_frame, text="Off", command=lambda: self.set_beamer_status("Off"))
        self.beamer_off_button.pack(side="left", padx=5, pady=5)

        self.watercooling_frame = ttk.LabelFrame(self.actuator_frame, text="Air Conditioning", padding=(5, 5))
        self.watercooling_frame.grid(column=0, row=2, padx=5, pady=5, sticky='NSEW')
        self.watercooling_on_button = tk.Button(self.watercooling_frame, text="On", command=lambda: self.set_watercooling_status("On"))
        self.watercooling_on_button.pack(side="left", padx=5, pady=5)
        self.watercooling_off_button = tk.Button(self.watercooling_frame, text="Off", command=lambda: self.set_watercooling_status("Off"))
        self.watercooling_off_button.pack(side="left", padx=5, pady=5)

        # Configure column and row weights to make widgets resize proportionally
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.sensor_frame.grid_rowconfigure(0, weight=1)
        self.sensor_frame.grid_rowconfigure(1, weight=1)
        self.sensor_frame.grid_rowconfigure(2, weight=1)
        self.sensor_frame.grid_rowconfigure(3, weight=1)
        self.sensor_frame.grid_columnconfigure(0, weight=1)

        self.actuator_frame.grid_rowconfigure(0, weight=1)
        self.actuator_frame.grid_rowconfigure(1, weight=1)
        self.actuator_frame.grid_rowconfigure(2, weight=1)
        self.actuator_frame.grid_columnconfigure(0, weight=1)

        # Apply style settings
        style = ttk.Style()
        style.configure("TFrame", background="#E6E6FA")
        style.configure("TLabel", background="#E6E6FA")
        style.configure("TLabelFrame", background="#9370DB", foreground="#FFFFFF", borderwidth=2, relief="solid")
        style.configure("TButton", background="#9370DB", foreground="#FFFFFF", font=("Helvetica", 10, "bold"))

        # Initialize actuator status
        self.set_window_status("Closed")
        self.set_beamer_status("Off")
        self.set_watercooling_status("Off")

    def start_loop(self, function):
        # Call the update_status function to initialize the status updates
        self.update_status(function, {"humidity": 0, "water": 0, "temperature": 0, "light": 0})

        # Start the Tkinter event loop
        self.root.mainloop()

    
    # Function to update the sensor and actuator status
    def update_status(self, function, sensor_data):
        if sensor_data is not None:
            self.humidity.set(str(sensor_data["humidity"]))
            self.water.set(str(sensor_data["water"]))
            self.temperature.set(str(sensor_data["temperature"]) + "°C")
            self.light.set(str(sensor_data["light"]))
        
        # Update the status every second
        self.root.after(1000, function)

    # Callback functions to handle actuator status change
    def set_window_status(self, state):
        if state == "Open":
            self.window_status.set("Open")
            self.window_open_button.config(bg="green", activebackground="green")
            self.window_closed_button.config(bg="grey", activebackground="grey")
        else:
            self.window_status.set("Closed")
            self.window_open_button.config(bg="grey", activebackground="grey")
            self.window_closed_button.config(bg="red", activebackground="red")

    def set_beamer_status(self, state):
        if state == "On":
            self.beamer_status.set("On")
            self.beamer_on_button.config(bg="green", activebackground="green")
            self.beamer_off_button.config(bg="grey", activebackground="grey")
        else:
            self.beamer_status.set("Off")
            self.beamer_on_button.config(bg="grey", activebackground="grey")
            self.beamer_off_button.config(bg="red", activebackground="red")

    def set_watercooling_status(self, state):
        if state == "On":
            self.watercooling_status.set("On")
            self.watercooling_on_button.config(bg="green", activebackground="green")
            self.watercooling_off_button.config(bg="grey", activebackground="grey")
        else:
            self.watercooling_status.set("Off")
            self.watercooling_on_button.config(bg="grey", activebackground="grey")
            self.watercooling_off_button.config(bg="red", activebackground="red")

    def get_temperatur(self):
        return self.temperature
    
    def get_humidity(self):
        return self.humidity

    def get_light(self):
        return self.light
    
    def get_water_level(self):
        return self.water
    def get_window_status(self):
        return self.window_status
    
    def get_watercooling_status(self):
        return self.watercooling_status