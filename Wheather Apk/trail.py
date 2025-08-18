import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from datetime import datetime
import threading
import json
import pyttsx3




class WeatherApp:
    def __init__(self, root):
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 170)
        self.tts_engine.setProperty('volume', 1.0)
        self.root = root
        self.root.title("🌤️ Smart Weather Visualizer (Advanced)")
        self.root.geometry("1050x750")
        self.root.resizable(False, False)
        self.search_history = []
        self.favorites = self.load_favorites()
        self.dark_mode = False
        self.city_autocomplete_list = []
        self.current_city = None
        self.unit = 'C'  # 'C' or 'F'
        self.auto_dark_mode_check()
        self.bg_label = tk.Label(root, borderwidth=0, highlightthickness=0, bg='#ffffff')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.overlay = tk.Frame(root, bg='#ffffff', bd=0, highlightthickness=0)
        self.overlay.place(relx=0.5, rely=0.05, anchor='n', relwidth=0.96)
        self.title_label = tk.Label(self.overlay, text="🌍 Weather Visualizer (Advanced)",
                                    font=("Segoe UI", 26, "bold"), bg='#ffffff', fg='#003366')
        self.title_label.pack(pady=10)
        # Search frame (top)
        search_frame = tk.Frame(self.overlay, bg='#ffffff')
        search_frame.pack(pady=(0, 5))
        self.city_entry = ttk.Entry(search_frame, font=("Segoe UI", 14), width=30)
        self.city_entry.insert(0, "Enter Indian city")
        self.city_entry.pack(side='left', padx=5)
        self.city_entry.bind("<Button-1>", lambda e: self.city_entry.delete(0, tk.END))
        self.city_entry.bind("<KeyRelease>", self.on_city_typing)
        self.city_entry.bind("<Return>", lambda e: self.get_weather())
        self.autocomplete_listbox = tk.Listbox(search_frame, font=("Segoe UI", 12), width=30, height=4)
        self.autocomplete_listbox.pack_forget()
        self.autocomplete_listbox.bind("<ButtonRelease-1>", self.select_autocomplete)

        # Button frames (two rows below search)
        button_frame1 = tk.Frame(self.overlay, bg='#ffffff')
        button_frame1.pack(pady=(0, 2))
        button_frame2 = tk.Frame(self.overlay, bg='#ffffff')
        button_frame2.pack(pady=(0, 10))

        btn_check = ttk.Button(button_frame1, text="Check Weather", command=self.get_weather)
        btn_refresh = ttk.Button(button_frame1, text="Refresh", command=self.refresh_weather)
        btn_download = ttk.Button(button_frame1, text="Download Background", command=self.download_image)
        btn_theme = ttk.Button(button_frame1, text="Toggle Theme", command=self.toggle_theme)
        btn_graph = ttk.Button(button_frame1, text="Graph", command=self.show_forecast_graph)
        btn_hourly = ttk.Button(button_frame1, text="Hourly Forecast", command=self.show_hourly_forecast)

        btn_map = ttk.Button(button_frame2, text="Weather Map", command=self.show_weather_map)
        btn_export = ttk.Button(button_frame2, text="Export", command=self.export_weather_data)
        btn_settings = ttk.Button(button_frame2, text="Settings", command=self.open_settings)
        btn_speak = ttk.Button(button_frame2, text="🔊 Speak", command=self.speak_weather_details)
        btn_stop = ttk.Button(button_frame2, text="⏹ Stop Voice", command=self.stop_voice)
        self.favorite_btn = ttk.Button(button_frame2, text="☆", command=self.toggle_favorite, width=2)

        for btn in [btn_check, btn_refresh, btn_download, btn_theme, btn_graph, btn_hourly]:
            btn.pack(side='left', padx=6, pady=3)
        for btn in [btn_map, btn_export, btn_settings, btn_speak, btn_stop, self.favorite_btn]:
            btn.pack(side='left', padx=6, pady=3)

        # Tooltips for buttons
        def add_tooltip(widget, text):
            def on_enter(e):
                self.status.config(text=text)
            def on_leave(e):
                self.status.config(text="")
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
        add_tooltip(btn_check, "Get weather for selected city")
        add_tooltip(btn_refresh, "Refresh current city's weather")
        add_tooltip(btn_download, "Download background image")
        add_tooltip(btn_theme, "Toggle light/dark theme")
        add_tooltip(btn_graph, "Show 3-day forecast graph")
        add_tooltip(btn_hourly, "Show hourly forecast graph")
        add_tooltip(btn_map, "Show weather map for city")
        add_tooltip(btn_export, "Export forecast data (CSV/JSON)")
        add_tooltip(btn_settings, "Open settings")
        add_tooltip(btn_speak, "Speak weather details")
        add_tooltip(btn_stop, "Stop voice output")
        add_tooltip(self.favorite_btn, "Add/remove city from favorites")
        self.status = tk.Label(self.overlay, text="", font=("Segoe UI", 10), bg='#ffffff', fg="green")
        self.status.pack(pady=5)
        self.favorites_dropdown = ttk.Combobox(self.overlay, values=self.favorites, state="readonly", font=("Segoe UI", 12), width=25)
        self.favorites_dropdown.pack()
        self.favorites_dropdown.bind("<<ComboboxSelected>>", self.select_favorite)
        self.result_frame = tk.Frame(root, bg='#ffffff', bd=0, relief="flat", highlightthickness=0)
        self.result_frame.place(relx=0.5, rely=0.38, anchor='n', width=650, height=320)
        self.result_label = tk.Label(self.result_frame, text="", font=("Segoe UI", 14), bg='#ffffff',
                                     fg="#003366", justify='center')
        self.result_label.place(relx=0.5, rely=0.25, anchor='center')
        self.details_label = tk.Label(self.result_frame, text="", font=("Segoe UI", 11), bg='#ffffff',
                                      fg="#222222", justify='center')
        self.details_label.place(relx=0.5, rely=0.45, anchor='center')
        self.forecast_label = tk.Label(self.result_frame, text="", font=("Segoe UI", 11), bg='#ffffff',
                                       fg="#444444", justify='center')
        self.forecast_label.place(relx=0.5, rely=0.83, anchor='center')
        self.icon_label = tk.Label(self.overlay, bg='#ffffff')
        self.icon_label.pack(pady=10)
        self.history_var = tk.StringVar(value=self.search_history[:8])
        self.history_dropdown = ttk.Combobox(self.overlay, values=self.search_history[:8], state="readonly", font=("Segoe UI", 10, "italic"), width=30)
        self.history_dropdown.pack()
        self.history_dropdown.bind("<<ComboboxSelected>>", self.select_history)
        self.delete_history_btn = ttk.Button(self.overlay, text="Delete", command=self.delete_history_entry)
        self.delete_history_btn.pack(pady=2)
        self.graph_type = tk.StringVar(value='Temperature')
        self.loading_label = tk.Label(self.overlay, text="", font=("Segoe UI", 12, "italic"), bg='#ffffff', fg="#0077cc")
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
            'alerts': 'yes'
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
            # Animated weather icon (placeholder: use static for now, can be replaced with GIFs)
            icon_url = "http:" + current['condition']['icon']
            try:
                import os
                gif_path = f"icons/{condition.lower().replace(' ', '_')}.gif"
                if os.path.exists(gif_path):
                    self.animate_gif(gif_path)
                else:
                    icon_img = Image.open(BytesIO(requests.get(icon_url).content)).resize((64, 64))
                    self.icon_photo = ImageTk.PhotoImage(icon_img)
                    self.icon_label.config(image=self.icon_photo)
            except Exception as e:
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
            # Weather alerts
            alerts = data.get('alerts', {}).get('alert', [])
            if alerts:
                alert_msgs = '\n'.join([a.get('headline', '') + ': ' + a.get('desc', '') for a in alerts])
                messagebox.showwarning("Weather Alerts", alert_msgs)
            if city not in self.search_history:
                self.search_history.insert(0, city)
            self.update_history_label()
            self.current_city = city
            # Update favorite button state
            if city in self.favorites:
                self.favorite_btn.config(text="★")
            else:
                self.favorite_btn.config(text="☆")
            self.speak_weather_details()
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

    def show_hourly_forecast(self):
        if not hasattr(self, 'forecast_data'):
            self.status.config(text="❗ No forecast data.")
            return
        city = self.city_entry.get().strip()
        def fetch_and_show():
            try:
                params = {
                    'key': WEATHER_API_KEY,
                    'q': city,
                    'days': 1,
                    'aqi': 'no',
                    'alerts': 'no'
                }
                response = requests.get(BASE_URL, params=params)
                data = response.json()
                hours = data['forecast']['forecastday'][0]['hour']
                import matplotlib.pyplot as plt
                times = [h['time'][-5:] for h in hours]
                temps = [h['temp_c'] if self.unit == 'C' else h['temp_f'] for h in hours]
                humidity = [h['humidity'] for h in hours]
                wind = [h['wind_kph'] for h in hours]
                plt.figure(figsize=(10, 5))
                plt.subplot(311)
                plt.plot(times, temps, marker='o', color='blue')
                plt.ylabel(f'Temp (°{self.unit})')
                plt.subplot(312)
                plt.plot(times, humidity, marker='s', color='green')
                plt.ylabel('Humidity (%)')
                plt.subplot(313)
                plt.plot(times, wind, marker='^', color='orange')
                plt.ylabel('Wind (km/h)')
                plt.xlabel('Time')
                plt.tight_layout()
                plt.show()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to fetch hourly data: {e}")
        threading.Thread(target=fetch_and_show, daemon=True).start()

    def show_weather_map(self):
        city = self.city_entry.get().strip()
        if not city:
            self.status.config(text="Please enter a city.")
            return
        try:
            # Geocode city to lat/lon using Nominatim
            geocode_url = f"https://nominatim.openstreetmap.org/search?format=json&q={city}"
            geo_resp = requests.get(geocode_url, headers={'User-Agent': 'Mozilla/5.0'})
            geo_data = geo_resp.json()
            if not geo_data:
                messagebox.showerror("Error", f"Could not find location for {city}.")
                return
            lat = geo_data[0]['lat']
            lon = geo_data[0]['lon']
            # OpenStreetMap static map
            osm_url = f"https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&size=600,400&z=10&l=map&pt={lon},{lat},pm2rdm"
            map_win = tk.Toplevel(self.root)
            map_win.title(f"Map for {city}")
            map_win.geometry("600x400")
            img_data = requests.get(osm_url).content
            img = Image.open(BytesIO(img_data)).resize((600, 400))
            photo = ImageTk.PhotoImage(img)
            lbl = tk.Label(map_win, image=photo)
            lbl.image = photo
            lbl.pack()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load map: {e}")

    def export_weather_data(self):
        if not hasattr(self, 'forecast_data'):
            self.status.config(text="❗ No forecast data.")
            return
        try:
            file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json"), ("CSV", "*.csv")])
            if file:
                if file.endswith('.json'):
                    with open(file, 'w') as f:
                        json.dump(self.forecast_data, f, indent=2)
                else:
                    import csv
                    with open(file, 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(['date', 'condition', 'avgtemp_c', 'avgtemp_f', 'avghumidity', 'maxwind_kph'])
                        for day in self.forecast_data:
                            writer.writerow([
                                day['date'],
                                day['day']['condition']['text'],
                                day['day']['avgtemp_c'],
                                day['day']['avgtemp_f'],
                                day['day']['avghumidity'],
                                day['day']['maxwind_kph']
                            ])
                self.status.config(text="✅ Data exported.")
        except Exception as e:
            self.status.config(text=f"❌ Failed to export: {e}")

    def auto_dark_mode_check(self):
        import time
        now = datetime.now().hour
        if 19 <= now or now < 7:
            if not self.dark_mode:
                self.toggle_theme()
        else:
            if self.dark_mode:
                self.toggle_theme()
        # Check every hour
        self.root.after(60*60*1000, self.auto_dark_mode_check)


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
        self.history_dropdown['values'] = self.search_history[:8]
        if self.search_history:
            self.history_dropdown.set(self.search_history[0])
        else:
            self.history_dropdown.set("")

    def select_history(self, event):
        city = self.history_dropdown.get()
        if city:
            self.city_entry.delete(0, tk.END)
            self.city_entry.insert(0, city)
            self.get_weather()

    def delete_history_entry(self):
        city = self.history_dropdown.get()
        if city in self.search_history:
            self.search_history.remove(city)
            self.update_history_label()

    def refresh_weather(self):
        if self.current_city:
            self.get_weather()
        else:
            self.status.config(text="No city to refresh.")

    def toggle_favorite(self):
        city = self.city_entry.get().strip()
        if city in self.favorites:
            self.favorites.remove(city)
            self.favorite_btn.config(text="☆")
        else:
            self.favorites.append(city)
            self.favorite_btn.config(text="★")
        self.save_favorites()
        self.favorites_dropdown['values'] = self.favorites

    def select_favorite(self, event):
        city = self.favorites_dropdown.get()
        if city:
            self.city_entry.delete(0, tk.END)
            self.city_entry.insert(0, city)
            self.get_weather()

    def save_favorites(self):
        try:
            with open("favorites.json", "w") as f:
                json.dump(self.favorites, f)
        except Exception:
            pass

    def load_favorites(self):
        try:
            with open("favorites.json", "r") as f:
                return json.load(f)
        except Exception:
            return []

    def speak_weather_details(self):
        try:
            if not hasattr(self, 'forecast_data') or not self.result_label.cget('text'):
                self.status.config(text="❗ No weather details to speak.")
                return
            city = self.current_city or self.city_entry.get().strip()
            details = self.result_label.cget('text').replace('\n', ', ')
            forecast = self.forecast_label.cget('text').replace('\n', ', ')
            speak_text = f"Weather for {city}. {details}. {forecast}."
            self.tts_engine.say(speak_text)
            self.status.config(text="🔊 Speaking weather details...")
            self.tts_engine.runAndWait()
        except Exception as e:
            self.status.config(text=f"❌ Voice error: {e}")

    def stop_voice(self):
        try:
            self.tts_engine.stop()
            self.status.config(text="⏹ Voice stopped.")
        except Exception as e:
            self.status.config(text=f"❌ Voice stop error: {e}")

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
