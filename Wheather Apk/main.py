import tkinter as tk
from tkinter import ttk, messagebox
import threading
import random
import time
from typing import List, Protocol

class Observer(Protocol):
    def update(self, temperature: float, humidity: float, pressure: float):
        ...

class WeatherStation:
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 25.0
        self._humidity = 50.0
        self._pressure = 1013.0

    def register(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_weather(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()

    @property
    def weather(self):
        return self._temperature, self._humidity, self._pressure

class PhoneDisplay(tk.LabelFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Phone Display", padx=10, pady=10, **kwargs)
        self.label = tk.Label(self, text="No data", font=("Arial", 12))
        self.label.pack()

    def update(self, temperature: float, humidity: float, pressure: float):
        self.label.config(text=f"Temp: {temperature}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa")

class WindowDisplay(tk.LabelFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Window Display", padx=10, pady=10, **kwargs)
        self.label = tk.Label(self, text="No data", font=("Arial", 12))
        self.label.pack()

    def update(self, temperature: float, humidity: float, pressure: float):
        self.label.config(text=f"Temp: {temperature}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa")

class WeatherGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather Monitoring System")
        self.geometry("500x400")
        self.resizable(False, False)
        self.station = WeatherStation()
        self.simulation_running = False
        self.sim_thread = None

        # Observer widgets
        self.phone_display = PhoneDisplay(self)
        self.window_display = WindowDisplay(self)
        self.phone_display.place(x=30, y=120, width=200, height=120)
        self.window_display.place(x=270, y=120, width=200, height=120)

        # Controls
        self.create_controls()

    def create_controls(self):
        frame = tk.LabelFrame(self, text="Weather Controls", padx=10, pady=10)
        frame.place(x=30, y=10, width=440, height=90)

        tk.Label(frame, text="Temperature (°C):").grid(row=0, column=0)
        tk.Label(frame, text="Humidity (%):").grid(row=0, column=2)
        tk.Label(frame, text="Pressure (hPa):").grid(row=0, column=4)

        self.temp_var = tk.DoubleVar(value=25)
        self.hum_var = tk.DoubleVar(value=50)
        self.pres_var = tk.DoubleVar(value=1013)

        tk.Entry(frame, textvariable=self.temp_var, width=6).grid(row=0, column=1)
        tk.Entry(frame, textvariable=self.hum_var, width=6).grid(row=0, column=3)
        tk.Entry(frame, textvariable=self.pres_var, width=8).grid(row=0, column=5)

        ttk.Button(frame, text="Update Weather", command=self.update_weather).grid(row=1, column=0, pady=8)
        ttk.Button(frame, text="Register Phone", command=self.register_phone).grid(row=1, column=1)
        ttk.Button(frame, text="Unregister Phone", command=self.unregister_phone).grid(row=1, column=2)
        ttk.Button(frame, text="Register Window", command=self.register_window).grid(row=1, column=3)
        ttk.Button(frame, text="Unregister Window", command=self.unregister_window).grid(row=1, column=4)
        self.sim_btn = ttk.Button(frame, text="Start Simulation", command=self.toggle_simulation)
        self.sim_btn.grid(row=1, column=5)

    def update_weather(self):
        try:
            t = self.temp_var.get()
            h = self.hum_var.get()
            p = self.pres_var.get()
            self.station.set_weather(t, h, p)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def register_phone(self):
        self.station.register(self.phone_display)
        messagebox.showinfo("Observer", "Phone Display registered.")

    def unregister_phone(self):
        self.station.unregister(self.phone_display)
        messagebox.showinfo("Observer", "Phone Display unregistered.")

    def register_window(self):
        self.station.register(self.window_display)
        messagebox.showinfo("Observer", "Window Display registered.")

    def unregister_window(self):
        self.station.unregister(self.window_display)
        messagebox.showinfo("Observer", "Window Display unregistered.")

    def toggle_simulation(self):
        if not self.simulation_running:
            self.simulation_running = True
            self.sim_btn.config(text="Stop Simulation")
            self.sim_thread = threading.Thread(target=self.simulate_weather, daemon=True)
            self.sim_thread.start()
        else:
            self.simulation_running = False
            self.sim_btn.config(text="Start Simulation")

    def simulate_weather(self):
        while self.simulation_running:
            t = round(random.uniform(15, 35), 1)
            h = round(random.uniform(30, 70), 1)
            p = round(random.uniform(990, 1030), 1)
            self.temp_var.set(t)
            self.hum_var.set(h)
            self.pres_var.set(p)
            self.station.set_weather(t, h, p)
            time.sleep(2)

if __name__ == "__main__":
    app = WeatherGUI()
    app.mainloop()
