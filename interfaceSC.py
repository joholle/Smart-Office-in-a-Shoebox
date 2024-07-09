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
        sensor_frame = ttk.LabelFrame(self.root, text="Sensors", padding=(10, 5))
        sensor_frame.grid(column=0, row=0, padx=10, pady=10, sticky='NSEW')

        actuator_frame = ttk.LabelFrame(self.root, text="Actuators", padding=(10, 5))
        actuator_frame.grid(column=1, row=0, padx=10, pady=10, sticky='NSEW')

        # Add sensor labels
        humidity_frame = ttk.LabelFrame(sensor_frame, text="Humidity", padding=(5, 5))
        humidity_frame.grid(column=0, row=0, padx=5, pady=5, sticky='NSEW')
        humidity_label = ttk.Label(humidity_frame, textvariable=self.humidity, font=("Helvetica", 12))
        humidity_label.pack(padx=10, pady=10)

        water_frame = ttk.LabelFrame(sensor_frame, text="Water Level", padding=(5, 5))
        water_frame.grid(column=0, row=1, padx=5, pady=5, sticky='NSEW')
        water_label = ttk.Label(water_frame, textvariable=self.water, font=("Helvetica", 12))
        water_label.pack(padx=10, pady=10)

        temperature_frame = ttk.LabelFrame(sensor_frame, text="Temperature", padding=(5, 5))
        temperature_frame.grid(column=0, row=2, padx=5, pady=5, sticky='NSEW')
        temperature_label = ttk.Label(temperature_frame, textvariable=self.temperature, font=("Helvetica", 12))
        temperature_label.pack(padx=10, pady=10)

        light_frame = ttk.LabelFrame(sensor_frame, text="Light Intensity", padding=(5, 5))
        light_frame.grid(column=0, row=3, padx=5, pady=5, sticky='NSEW')
        light_label = ttk.Label(light_frame, textvariable=self.light, font=("Helvetica", 12))
        light_label.pack(padx=10, pady=10)

        # Add actuator controls
        window_frame = ttk.LabelFrame(actuator_frame, text="Windows", padding=(5, 5))
        window_frame.grid(column=0, row=0, padx=5, pady=5, sticky='NSEW')
        window_open_button = tk.Button(window_frame, text="Open", command=lambda: self.set_window_status("Open"))
        window_open_button.pack(side="left", padx=5, pady=5)
        window_closed_button = tk.Button(window_frame, text="Closed", command=lambda: self.set_window_status("Closed"))
        window_closed_button.pack(side="left", padx=5, pady=5)

        beamer_frame = ttk.LabelFrame(actuator_frame, text="Beamer", padding=(5, 5))
        beamer_frame.grid(column=0, row=1, padx=5, pady=5, sticky='NSEW')
        beamer_on_button = tk.Button(beamer_frame, text="On", command=lambda: self.set_beamer_status("On"))
        beamer_on_button.pack(side="left", padx=5, pady=5)
        beamer_off_button = tk.Button(beamer_frame, text="Off", command=lambda: self.set_beamer_status("Off"))
        beamer_off_button.pack(side="left", padx=5, pady=5)

        watercooling_frame = ttk.LabelFrame(actuator_frame, text="Air Conditioning", padding=(5, 5))
        watercooling_frame.grid(column=0, row=2, padx=5, pady=5, sticky='NSEW')
        watercooling_on_button = tk.Button(watercooling_frame, text="On", command=lambda: self.set_watercooling_status("On"))
        watercooling_on_button.pack(side="left", padx=5, pady=5)
        watercooling_off_button = tk.Button(watercooling_frame, text="Off", command=lambda: self.set_watercooling_status("Off"))
        watercooling_off_button.pack(side="left", padx=5, pady=5)

        # Configure column and row weights to make widgets resize proportionally
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        sensor_frame.grid_rowconfigure(0, weight=1)
        sensor_frame.grid_rowconfigure(1, weight=1)
        sensor_frame.grid_rowconfigure(2, weight=1)
        sensor_frame.grid_rowconfigure(3, weight=1)
        sensor_frame.grid_columnconfigure(0, weight=1)

        actuator_frame.grid_rowconfigure(0, weight=1)
        actuator_frame.grid_rowconfigure(1, weight=1)
        actuator_frame.grid_rowconfigure(2, weight=1)
        actuator_frame.grid_columnconfigure(0, weight=1)

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

        # Call the update_status function to initialize the status updates
        self.update_status()

        # Start the Tkinter event loop
        self.root.mainloop()

    
    # Function to update the sensor and actuator status
    def update_status(self):
        # Dummy data, replace with actual sensor data fetching logic
        self.humidity.set("45%") #
        self.water.set("Low")
        self.temperature.set("22°C")
        self.light.set("Medium")
        
        # Update the status every second
        self.root.after(1000, self.update_status)

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

