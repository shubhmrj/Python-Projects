import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO



class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌦 Weather Monitor - India")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # Load background image
        self.bg_img = Image.open("background.jpg").resize((700, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Weather info frame
        self.frame = tk.Frame(root, bg='white', bd=2, relief=tk.RIDGE)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        self.title = tk.Label(self.frame, text="Weather App (India)", font=("Segoe UI", 16, "bold"), bg="white", fg="#007acc")
        self.title.grid(row=0, column=0, columnspan=2, pady=10)

        # City Entry
        self.city_entry = ttk.Entry(self.frame, font=("Segoe UI", 12), width=30)
        self.city_entry.grid(row=1, column=0, padx=10, pady=10)
        self.city_entry.insert(0, "Enter Indian city")

        # Search Button
        self.search_btn = ttk.Button(self.frame, text="Check Weather", command=self.get_weather)
        self.search_btn.grid(row=1, column=1, padx=10, pady=10)

        # Weather icon
        self.icon_label = tk.Label(self.frame, bg="white")
        self.icon_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Weather details
        self.result_label = tk.Label(self.frame, text="", font=("Segoe UI", 12), bg="white", justify='left')
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def get_weather(self):
        city = self.city_entry.get()
        if not city.strip():
            self.result_label.config(text="❌ Please enter a valid city name.")
            return

        params = {
            'key': API_KEY,
            'q': city,
            'aqi': 'no'
        }

        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if "error" in data:
                self.result_label.config(text=f"❌ Error: {data['error']['message']}")
                return

            location = data['location']['name']
            country = data['location']['country']
            current = data['current']
            condition = current['condition']['text']
            temp_c = current['temp_c']
            feels_like = current['feelslike_c']
            humidity = current['humidity']
            wind = current['wind_kph']

            # Display icon
            icon_url = "http:" + current['condition']['icon']
            icon_img = Image.open(BytesIO(requests.get(icon_url).content)).resize((64, 64))
            self.icon_photo = ImageTk.PhotoImage(icon_img)
            self.icon_label.config(image=self.icon_photo)

            # Weather details
            self.result_label.config(
                text=f"📍 {location}, {country}\n"
                     f"🌡 Temperature: {temp_c}°C (Feels like {feels_like}°C)\n"
                     f"🌥 Condition: {condition}\n"
                     f"💧 Humidity: {humidity}%\n"
                     f"💨 Wind: {wind} km/h"
            )

        except Exception as e:
            self.result_label.config(text="⚠️ Could not retrieve data.\n" + str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
