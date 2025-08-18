import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import openai

# ✅ Set your OpenAI API key here

# WeatherAPI key



class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Weather Monitor + AI Image (India)")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # Background
        bg_img = Image.open("background.jpg").resize((900, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_img)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        self.title = tk.Label(root, text="Weather App (India) + AI Image",
                              font=("Segoe UI", 20, "bold"), bg="#ffffff", fg="#005f9e")
        self.title.place(relx=0.5, y=30, anchor='center')

        # City Entry
        self.city_entry = ttk.Entry(root, font=("Segoe UI", 12), width=30)
        self.city_entry.place(relx=0.32, rely=0.13)
        self.city_entry.insert(0, "Enter Indian city")

        self.search_btn = ttk.Button(root, text="Check Weather", command=self.get_weather)
        self.search_btn.place(relx=0.65, rely=0.13)

        # Weather Icon
        self.icon_label = tk.Label(root, bg=None)
        self.icon_label.place(relx=0.25, rely=0.35, anchor='center')

        # Weather Result
        self.result_label = tk.Label(root, text="", font=("Segoe UI", 13),
                                     bg="#000080", fg="#ffffff", justify='center', wraplength=500)
        self.result_label.place(relx=0.28, rely=0.55, anchor='center')

        # AI Image
        self.ai_image_label = tk.Label(root, bg="#ffffff", bd=2, relief="solid")
        self.ai_image_label.place(relx=0.75, rely=0.5, anchor='center', width=300, height=300)

        # Status
        self.status = tk.Label(root, text="", font=("Segoe UI", 10), bg="#ffffff", fg="green")
        self.status.place(relx=0.5, rely=0.95, anchor='center')

        self.loading_label = tk.Label(root, text="", font=("Segoe UI", 10), bg="#ffffff", fg="blue")
        self.loading_label.place(relx=0.75, rely=0.85, anchor='center')

    def get_weather(self):
        city = self.city_entry.get()
        if not city.strip():
            self.result_label.config(text="❌ Please enter a valid city name.")
            self.icon_label.config(image='')
            return

        params = {
            'key': WEATHER_API_KEY,
            'q': city,
            'aqi': 'no'
        }

        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if "error" in data:
                self.result_label.config(text=f"❌ Error: {data['error']['message']}")
                self.icon_label.config(image='')
                return

            location = data['location']['name']
            country = data['location']['country']
            current = data['current']
            condition = current['condition']['text']
            temp_c = current['temp_c']
            feels_like = current['feelslike_c']
            humidity = current['humidity']
            wind = current['wind_kph']

            # Icon
            icon_url = "http:" + current['condition']['icon']
            icon_data = requests.get(icon_url).content
            icon_img = Image.open(BytesIO(icon_data)).resize((64, 64))
            self.icon_photo = ImageTk.PhotoImage(icon_img)
            self.icon_label.config(image=self.icon_photo)

            self.result_label.config(
                text=f"📍 {location}, {country}\n"
                     f"🌡 Temperature: {temp_c}°C (Feels like {feels_like}°C)\n"
                     f"🌥 Condition: {condition}\n"
                     f"💧 Humidity: {humidity}%\n"
                     f"💨 Wind: {wind} km/h"
            )

            prompt = f"A realistic scenic image showing {condition.lower()} weather in an Indian city"
            self.generate_ai_image(prompt)

        except Exception as e:
            self.result_label.config(text="⚠️ Could not retrieve data.\n" + str(e))
            self.icon_label.config(image='')

    def generate_ai_image(self, prompt):
        try:
            self.status.config(text="Generating AI image...")
            self.loading_label.config(text="🎨 Creating image...")

            response = openai.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024"
            )

            image_url = response.data[0].url
            img_data = requests.get(image_url).content

            ai_img = Image.open(BytesIO(img_data)).resize((300, 300))
            self.ai_photo = ImageTk.PhotoImage(ai_img)
            self.ai_image_label.config(image=self.ai_photo)

            self.status.config(text="AI image generated.")
            self.loading_label.config(text="")

        except Exception as e:
            self.status.config(text="❌ AI image failed. Check API key or billing.")
            self.loading_label.config(text="")
            print("AI image generation error:", e)


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
