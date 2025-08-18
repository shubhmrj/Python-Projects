import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from datetime import datetime
import threading
import json



class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Smart Weather Visualizer (Advanced)")
        self.root.geometry("1050x750")
        self.root.resizable(False, False)
        self.search_history = []
        self.dark_mode = False
        self.city_autocomplete_list = []
        self.current_city = None
        self.unit = 'C'  # 'C' or 'F'
        self.bg_label = tk.Label(root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.overlay = tk.Frame(root, bg='#ffffff', bd=0, highlightthickness=0)
        self.overlay.place(relx=0.5, rely=0.05, anchor='n', relwidth=0.96)
        self.title_label = tk.Label(self.overlay, text="🌍 Weather Visualizer (Advanced)",
                                    font=("Segoe UI", 26, "bold"), bg='#ffffff', fg='#003366')
        self.title_label.pack(pady=10)
        input_frame = tk.Frame(self.overlay, bg='#ffffff')
        input_frame.pack()
        self.city_entry = ttk.Entry(input_frame, font=("Segoe UI", 14), width=30)
        self.city_entry.insert(0, "Enter Indian city")
        self.city_entry.pack(side='left', padx=5)
        self.city_entry.bind("<Button-1>", lambda e: self.city_entry.delete(0, tk.END))
        self.city_entry.bind("<KeyRelease>", self.on_city_typing)
        self.city_entry.bind("<Return>", lambda e: self.get_weather())
        self.autocomplete_listbox = tk.Listbox(input_frame, font=("Segoe UI", 12), width=30, height=4)
        self.autocomplete_listbox.pack_forget()
        self.autocomplete_listbox.bind("<ButtonRelease-1>", self.select_autocomplete)
        ttk.Button(input_frame, text="Check Weather", command=self.get_weather).pack(side='left', padx=5)
        ttk.Button(input_frame, text="Refresh", command=self.refresh_weather).pack(side='left', padx=5)
        ttk.Button(input_frame, text="Download Background", command=self.download_image).pack(side='left', padx=5)
        ttk.Button(input_frame, text="Toggle Theme", command=self.toggle_theme).pack(side='left', padx=5)
        ttk.Button(input_frame, text="Graph", command=self.show_forecast_graph).pack(side='left', padx=5)
        ttk.Button(input_frame, text="Settings", command=self.open_settings).pack(side='left', padx=5)
        self.status = tk.Label(self.overlay, text="", font=("Segoe UI", 10), bg='#ffffff', fg="green")
        self.status.pack(pady=5)
        self.result_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="solid")
        self.result_frame.place(relx=0.5, rely=0.38, anchor='n', width=650, height=320)
        self.result_label = tk.Label(self.result_frame, text="", font=("Segoe UI", 14), bg="#ffffff",
                                     fg="#003366", justify='center')
        self.result_label.place(relx=0.5, rely=0.25, anchor='center')
        self.details_label = tk.Label(self.result_frame, text="", font=("Segoe UI", 11), bg="#ffffff",
                                      fg="#222222", justify='center')
        self.details_label.place(relx=0.5, rely=0.45, anchor='center')
        self.forecast_label = tk.Label(self.result_frame, text="", font=("Segoe UI", 11), bg="#ffffff",
                                       fg="#444444", justify='center')
        self.forecast_label.place(relx=0.5, rely=0.83, anchor='center')
        self.icon_label = tk.Label(self.overlay, bg="#ffffff")
        self.icon_label.pack(pady=10)
        self.history_label = tk.Label(self.overlay, text="", font=("Segoe UI", 10, "italic"), bg="#ffffff", fg="#555555", cursor="hand2")
        self.history_label.pack()
        self.history_label.bind("<Button-1>", self.on_history_click)
        self.graph_type = tk.StringVar(value='Temperature')
        self.loading_label = tk.Label(self.overlay, text="", font=("Segoe UI", 12, "italic"), bg="#ffffff", fg="#0077cc")
        self.loading_label.pack(pady=2)
        self.load_city_autocomplete()

    def load_city_autocomplete(self):
        def fetch():
            try:
                # Only Indian cities
                resp = requests.get(CITIES_URL)
                cities = resp.json()
                self.city_autocomplete_list = sorted(list(set(
                    city['name'] for city in cities if city['country_id'] == '101')))
            except Exception:
                self.city_autocomplete_list = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad", "Jaipur"]
        threading.Thread(target=fetch, daemon=True).start()

    def on_city_typing(self, event):
        typed = self.city_entry.get().strip().lower()
        matches = [c for c in self.city_autocomplete_list if c.lower().startswith(typed)] if typed else []
        if matches:
            self.autocomplete_listbox.delete(0, tk.END)
            for city in matches[:8]:
                self.autocomplete_listbox.insert(tk.END, city)
            self.autocomplete_listbox.place(x=self.city_entry.winfo_x(), y=self.city_entry.winfo_y()+30)
        else:
            self.autocomplete_listbox.place_forget()

    def select_autocomplete(self, event):
        selection = self.autocomplete_listbox.get(tk.ACTIVE)
        self.city_entry.delete(0, tk.END)
        self.city_entry.insert(0, selection)
        self.autocomplete_listbox.place_forget()

    def set_loading(self, is_loading=True, msg="Loading..."):
        self.loading_label.config(text=msg if is_loading else "")
        self.root.update_idletasks()

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            self.result_label.config(text="Please enter a valid city.")
            return
        self.set_loading(True, f"Fetching weather for {city}...")
        threading.Thread(target=self._fetch_weather, args=(city,), daemon=True).start()

    def _fetch_weather(self, city):
        params = {
            'key': WEATHER_API_KEY,
            'q': city,
            'days': 3,
            'aqi': 'no',
            'alerts': 'no'
        }
        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            if "error" in data:
                self.result_label.config(text=f"Error: {data['error']['message']}")
                self.set_loading(False)
                return
            current = data['current']
            location = data['location']['name']
            country = data['location']['country']
            temp_c = current['temp_c']
            temp_f = current['temp_f']
            feels_like_c = current['feelslike_c']
            feels_like_f = current['feelslike_f']
            humidity = current['humidity']
            wind = current['wind_kph']
            vis_km = current.get('vis_km', '-')
            uv = current.get('uv', '-')
            pressure = current.get('pressure_mb', '-')
            sunrise = data['forecast']['forecastday'][0]['astro'].get('sunrise', '-')
            sunset = data['forecast']['forecastday'][0]['astro'].get('sunset', '-')
            condition = current['condition']['text']
            icon_url = "http:" + current['condition']['icon']
            icon_img = Image.open(BytesIO(requests.get(icon_url).content)).resize((64, 64))
            self.icon_photo = ImageTk.PhotoImage(icon_img)
            self.icon_label.config(image=self.icon_photo)
            temp = f"{temp_c}°C (Feels {feels_like_c}°C)" if self.unit == 'C' else f"{temp_f}°F (Feels {feels_like_f}°F)"
            self.result_label.config(
                text=f"📍 {location}, {country}\n"
                     f"🌡 Temperature: {temp}\n"
                     f"🌤 Condition: {condition}\n"
                     f"💧 Humidity: {humidity}%\n"
                     f"💨 Wind: {wind} km/h\n"
            )
            self.details_label.config(
                text=f"🌅 Sunrise: {sunrise}    🌇 Sunset: {sunset}\n"
                     f"👁 Visibility: {vis_km} km    ☀️ UV: {uv}\n"
                     f"📈 Pressure: {pressure} mb"
            )
            self.forecast_data = data['forecast']['forecastday']
            forecast_text = "🗓 3-Day Forecast:\n"
            for day in self.forecast_data:
                avgtemp = day['day']['avgtemp_c'] if self.unit == 'C' else day['day']['avgtemp_f']
                forecast_text += f"{day['date']}: {day['day']['condition']['text']} ({avgtemp}°{self.unit})\n"
            self.forecast_label.config(text=forecast_text.strip())
            self.update_background(condition)
            if city not in self.search_history:
                self.search_history.insert(0, city)
            self.update_history_label()
            self.current_city = city
        except Exception as e:
            self.result_label.config(text=f"Error fetching data: {e}")
        self.set_loading(False)

    def update_background(self, condition):
        try:
            query = f"indian city {condition}"
            url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
            response = requests.get(url)
            image_url = response.json()['urls']['regular']
            self.current_bg_data = requests.get(image_url).content
            bg_image = Image.open(BytesIO(self.current_bg_data)).resize((1050, 750)).convert("RGBA")
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            self.bg_label.config(image=self.bg_photo)
            self.status.config(text="✅ Background updated.")
        except:
            self.status.config(text="❌ Failed to update background.")

    def download_image(self):
        try:
            if hasattr(self, 'current_bg_data'):
                file = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")])
                if file:
                    with open(file, "wb") as f:
                        f.write(self.current_bg_data)
                    self.status.config(text="✅ Image downloaded.")
        except:
            self.status.config(text="❌ Failed to download image.")

    def show_forecast_graph(self):
        if not hasattr(self, 'forecast_data'):
            self.status.config(text="❗ No forecast data.")
            return
        def plot():
            dates = [d['date'] for d in self.forecast_data]
            temps = [d['day']['avgtemp_c'] if self.unit == 'C' else d['day']['avgtemp_f'] for d in self.forecast_data]
            humidities = [d['day']['avghumidity'] for d in self.forecast_data]
            winds = [d['day']['maxwind_kph'] for d in self.forecast_data]
            plt.figure(figsize=(7, 4))
            if self.graph_type.get() == 'Temperature':
                plt.plot(dates, temps, marker='o', color='blue', label='Avg Temp')
                plt.ylabel(f'Avg Temp (°{self.unit})')
            elif self.graph_type.get() == 'Humidity':
                plt.plot(dates, humidities, marker='s', color='green', label='Avg Humidity')
                plt.ylabel('Avg Humidity (%)')
            elif self.graph_type.get() == 'Wind':
                plt.plot(dates, winds, marker='^', color='orange', label='Max Wind')
                plt.ylabel('Max Wind (km/h)')
            plt.title(f'3-Day {self.graph_type.get()} Forecast')
            plt.xlabel('Date')
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            plt.show()
        # Dialog to select graph type
        graph_win = tk.Toplevel(self.root)
        graph_win.title("Select Graph Type")
        graph_win.geometry("250x120")
        tk.Label(graph_win, text="Graph Type:", font=("Segoe UI", 12)).pack(pady=10)
        for t in ['Temperature', 'Humidity', 'Wind']:
            ttk.Radiobutton(graph_win, text=t, value=t, variable=self.graph_type).pack(anchor='w', padx=30)
        ttk.Button(graph_win, text="Show Graph", command=lambda: [plot(), graph_win.destroy()]).pack(pady=10)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        bg_color = '#222222' if self.dark_mode else '#ffffff'
        fg_color = '#fafafa' if self.dark_mode else '#003366'
        details_fg = '#cccccc' if self.dark_mode else '#222222'
        for widget in [self.overlay, self.result_frame, self.result_label, self.details_label, self.forecast_label,
                       self.icon_label, self.status, self.history_label, self.title_label, self.loading_label]:
            widget.config(bg=bg_color)
            if hasattr(widget, 'fg'):
                widget.config(fg=fg_color)
        self.details_label.config(fg=details_fg)

    def update_history_label(self):
        if self.search_history:
            self.history_label.config(text="🕘 Last searched: " + ", ".join(self.search_history[:5]))
        else:
            self.history_label.config(text="")

    def on_history_click(self, event):
        if not self.search_history:
            return
        # Show a popup menu for history
        menu = tk.Menu(self.root, tearoff=0)
        for city in self.search_history[:8]:
            menu.add_command(label=city, command=lambda c=city: self.city_entry.delete(0, tk.END) or self.city_entry.insert(0, c) or self.get_weather())
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

    def refresh_weather(self):
        if self.current_city:
            self.get_weather()
        else:
            self.status.config(text="No city to refresh.")

    def open_settings(self):
        # Settings: units, theme
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Settings")
        settings_win.geometry("300x200")
        tk.Label(settings_win, text="Settings", font=("Segoe UI", 15, "bold")).pack(pady=10)
        # Units
        tk.Label(settings_win, text="Temperature Unit:", font=("Segoe UI", 11)).pack(anchor='w', padx=20)
        unit_var = tk.StringVar(value=self.unit)
        ttk.Radiobutton(settings_win, text="Celsius", value='C', variable=unit_var).pack(anchor='w', padx=40)
        ttk.Radiobutton(settings_win, text="Fahrenheit", value='F', variable=unit_var).pack(anchor='w', padx=40)
        # Theme
        tk.Label(settings_win, text="Theme:", font=("Segoe UI", 11)).pack(anchor='w', padx=20, pady=(10,0))
        theme_var = tk.BooleanVar(value=self.dark_mode)
        ttk.Checkbutton(settings_win, text="Dark Mode", variable=theme_var).pack(anchor='w', padx=40)
        def save_settings():
            self.unit = unit_var.get()
            if self.dark_mode != theme_var.get():
                self.toggle_theme()
            settings_win.destroy()
        ttk.Button(settings_win, text="Save", command=save_settings).pack(pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
