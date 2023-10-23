import tkinter as tk
import ttkbootstrap as ttk
import requests

def show_weather(event):
    # api config
    baseUrl = 'http://api.openweathermap.org/data/2.5/weather?'
    key = '' #place your api key here!
    city = cityVar.get()
    
    # final api url
    finallurl = baseUrl + "appid=" + key + "&q=" + city
    response = requests.get(finallurl).json()
    
    tempCelcius = response['main']['temp'] - 273.15
    description = response['weather'][0]['description']
    windspeed = response['wind']['speed']
    humidity = response['main']['humidity']
    
    tempVar.set(f'{round(tempCelcius)}°')
    descVar.set(description)
    humidityVar.set(f'{humidity}% \n humidity')
    windVar.set(f'{round(windspeed, 1)} m/s \n windspeed')
    
    window.geometry('550x700')
    
# window setup
window = ttk.Window()
window.title("WeatherApp")
window.geometry('550x120')

#
icon = tk.PhotoImage(file='icon.png')
window.iconphoto(False, icon)

# frame of input and button
inputFrame = ttk.Frame(master=window)

# city input
cityVar = tk.StringVar()
inputCity = ttk.Entry(master=inputFrame, textvariable=cityVar, font='Roboto 24')
inputCity.bind('<Return>', show_weather)

# temporary prompt
inputCity.insert(0, "Enter your city")
inputCity.bind('<FocusIn>', lambda event: inputCity.delete(0, "end"))

# button photo
buttonPhoto = tk.PhotoImage(file='search.png')

# button
button = tk.Button(master=inputFrame, image=buttonPhoto, text="X", height=60, width=60, border=0)
button.bind('<Button-1>', show_weather)

# photo frame
photoFrame = ttk.Frame(master=window, width= 200)
photo = ttk.PhotoImage(file='sun.png')
photoLabel = ttk.Label(master= photoFrame , image=photo,)

# temp and description frame
tempFrame = ttk.Frame(master=window)

# output Temperatur
tempVar = tk.StringVar()
temp = tk.Label(master=tempFrame, textvariable=tempVar, font='Roboto 35 bold')

# output Description
descVar = tk.StringVar()
desc = tk.Label(master=tempFrame, textvariable=descVar, font='Roboto 22')

# humidity and windspeed frame
humidityFrame = ttk.Frame(master=window)

# output humidity
humidityVar = tk.StringVar()
humidity = tk.Label(master=humidityFrame, textvariable=humidityVar, font='Roboto 15')

# output windspeed
windVar = tk.StringVar()
wind = tk.Label(master=humidityFrame, textvariable=windVar, font='Roboto 15')

# packing
inputCity.pack(side="left", padx=10)
button.pack(side="left")
inputFrame.pack(pady=30)
photoLabel.pack()
photoFrame.pack()
temp.pack()
desc.pack()
tempFrame.pack()
humidity.pack(side='left', padx= 50, pady=50)
wind.pack(side='right', padx= 50, pady=50)
humidityFrame.pack()

# call mainloop
window.mainloop()
