import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as font
import requests
import datetime as dt

def test():
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
    API_KEY = 'place your api key here!'
    CITY = cityVar.get()
    
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    
    response = requests.get(url).json()

    tempKelvin = response['main']['temp']
    tempCelcius = kelvinToCelcius(tempKelvin)

    description = response['weather'][0]['description']
    #windspeed = response['wind']['speed']
    
    titleStr.set(f"{CITY}")
    titleFrame.config(font='Calibri 50')
    
    inputFrame.destroy()
    
    tempLabel = tk.Label(master=window, text=f'{round(tempCelcius)}°', font='Calibri 20')
    tempLabel.pack()
    
    descriptionLabel = tk.Label(master=window, text=f'{description}',font='Calibri 16')
    descriptionLabel.pack()
    
    window.geometry('420x250')
    
def kelvinToCelcius(kelvin):
    celcius = kelvin - 273.15
    return celcius    

# window
window = ttk.Window(themename='cosmo')
window.title('WeatherApp')
window.geometry('550x290')

icon = tk.PhotoImage(file='icon.png')
window.iconphoto(False, icon)

# title
titleStr = tk.StringVar()
titleStr.set('Enter your city')
titleFrame = ttk.Label(master=window, font='Calibri 35', textvariable=titleStr)
titleFrame.pack(pady=20)

# input frame
inputFrame = ttk.Frame(master=window)

# input City
cityVar = tk.StringVar()
inputCity = ttk.Entry(master=inputFrame,font='Calibri 30' , textvariable=cityVar)

# button
button = ttk.Button(master=inputFrame, text='check weather', command=test,)

# packing
inputCity.pack()
button.pack(pady=30)
inputFrame.pack()


window.mainloop()
