from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import io

font_style = ("arial", 15, "bold")
font_style_heading = ("arial", 30, "bold", "italic", "underline")
color = "dark blue"

API_KEY = "333a2648a54f8c2a0a56e26600ac28ad"


class WeatherForecast:
    def __init__(self):
        self.guiWindow = Tk()
        self.guiWindow.title("Weather Forecast App")
        self.guiWindow.geometry("500x500")
        self.guiWindow.resizable(0, 0)

        # creating heading for app
        self.heading_label = Label(
            text="WEATHER APP", font=font_style_heading, foreground=color, justify="center")
        self.heading_label.pack()

        # creating Text field and Label for city or pincode
        self.city_label = Label(
            self.guiWindow, text="Enter city or pincode: ", font=font_style)
        self.city_label.pack(pady=10)

        self.city_text = Entry(self.guiWindow, font=font_style, relief="solid")
        self.city_text.pack()

        # creating Button to retrive weather information
        self.btn_get_weather = Button(
            self.guiWindow, text="GET WEATHER", command=self.button_get_weather, bg="powder blue", foreground="black", height=1, width=10)
        self.btn_get_weather.pack(pady=10)

        # icon image label
        self.result_label = Label(self.guiWindow, text="", font=font_style)
        self.result_label.pack(pady=10)

        self.icon_image_label = Label(self.guiWindow)
        self.icon_image_label.pack(pady=10)

        self.guiWindow.mainloop()

    # creating function to get weather

    def get_weather_information(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}q={city}&appid={API_KEY}"

        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != 404:
            # extracting weather information
            city = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"]
            # icon image displaying according to weather condition
            icon_id = data['weather'][0]['icon']
            icon_url = f" https://openweathermap.org/img/w/{icon_id}.png"

            return {
                "city": city,
                "country": country,
                "temperature": temperature,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "description": description.capitalize(),
                "icon_url": icon_url
            }
        else:
            None

    def button_get_weather(self):
        city = self.city_text.get()
        if city:
            weather_data = self.get_weather_information(city)
            if weather_data:
                weather_info = f"Country: {weather_data ['country']}\nTemperature: {weather_data ['temperature']:.1f} °C\nHumidity:{weather_data ['humidity']}%\nWind:{weather_data ['wind_speed']}m/s\nDescription:{weather_data ['description']}"
                self.result_label.config(text=weather_info)

                # displaying weather icons
                icon_url = weather_data['icon_url']
                icon_response = requests.get(icon_url, stream=True)
                if icon_response:
                    icon_data = icon_response.content
                    icon_image = Image.open(io.BytesIO(icon_data))
                    icon_image = icon_image.resize(
                        (140, 140))  # Resize the image
                    icon_photo = ImageTk.PhotoImage(icon_image)
                    self.icon_image_label.config(image=icon_photo)
                    self.icon_image_label.image = icon_photo
            else:
                messagebox.showerror("ERROR", "No city found")
        else:
            messagebox.showerror("Input Error", "Please enter city name")


if __name__ == "__main__":
    weather = WeatherForecast()