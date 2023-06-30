from tkinter import *
from PIL import ImageTk, Image
import requests

url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "48fa1272d9f1a6912367ba9b34ede792"
iconUrl = "http://openweathermap.org/img/wn/{}@2x.png"

def getWeather(city):
    params = {'q':city,'appid':api_key,'lang':'tr'}
    data = requests.get(url,params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (city,country,temp,icon,condition)

def main():
    city = entryCity.get()
    weather = getWeather(city)
    if weather:
        locaitonLabel['text'] = '{},{}'.format(weather[0],weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon

app = Tk()
app.geometry("300x450")
app.title("Ref Hava Durumu")

entryCity = Entry(app,justify='center')
entryCity.pack(fill = BOTH,ipady=10,padx=18,pady=5)

searchButton = Button(app,text="Arama", font=("Arial",16),command=main)
searchButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel = Label(app)
iconLabel.pack()

locaitonLabel = Label(app,font=("Arial",30))
locaitonLabel.pack()

tempLabel = Label(app,font=("Arial",30,"bold"))
tempLabel.pack()

conditionLabel = Label(app,font=("Arial",25))
conditionLabel.pack()

app.mainloop()
