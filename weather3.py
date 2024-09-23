import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for handling images

def get_weather():
    city_name = city_entry.get()
    api_key = '4ba43fd97bafb65bbe3825345a5213f5'  # Replace with your OpenWeatherMap API key
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    try:
        response = requests.get(api_url)
        data = response.json()

        if data['cod'] == 200:
            temp_celsius = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            weather_desc = data['weather'][0]['description'].capitalize()
            wind_speed = data['wind']['speed']

            # Display weather details in the label
            result_text = f"City: {city_name.capitalize()}\n"
            result_text += f"Temperature: {temp_celsius:.2f} °C\n"
            result_text += f"Humidity: {humidity} %\n"
            result_text += f"Pressure: {pressure} hPa\n"
            result_text += f"Weather: {weather_desc}\n"
            result_text += f"Wind Speed: {wind_speed} m/s\n"

            weather_label.config(text=result_text)
        else:
            messagebox.showerror("Error", f"City '{city_name}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve weather data.\n{str(e)}")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("600x400")
root.resizable(False, False)

# Load the background image using Pillow
image_path = "E:/Weather/fluffy-clouds-windy-sky-with-sun.jpg"  # Replace with your actual image path
bg_image = Image.open(image_path)
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS instead of Image.ANTIALIAS
background_image = ImageTk.PhotoImage(bg_image)

# Background label
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Heading label
heading_label = tk.Label(root, text="Weather App", font=("Helvetica", 24, "bold"), bg="#333", fg="white")
heading_label.pack(pady=10)

# City entry field
city_entry = tk.Entry(root, font=("Helvetica", 18), justify="center", bg="#ffffff")
city_entry.pack(pady=20)
city_entry.focus()

# Search button
search_button = tk.Button(root, text="Search", font=("Helvetica", 14), command=get_weather, bg="#007BFF", fg="white")
search_button.pack(pady=10)

# Weather details label
weather_label = tk.Label(root, font=("Helvetica", 16), bg="#333", fg="white", justify="left")
weather_label.pack(pady=20)

# Start the main event loop
root.mainloop()
