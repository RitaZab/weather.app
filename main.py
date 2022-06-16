import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url="https://weather.com/pl-PL/pogoda/dzisiaj/l/4bb2170beefd39564b5c8e62005678d9e9826ec700418193a170e148a76face9"

main=Tk()
main.title("Pogoda na dziś")
main.config(bg="#a6d4e0")

img=Image.open("C:/Users/Rita/PycharmProjects/Weather_ap/weather-news.png")
img=img.resize((200,200))
img=ImageTk.PhotoImage(img)
cityLabel=Label(main,font=("Times bold",21),bg="#a6d4e0")
cityLabel.grid(row=0, sticky="N",padx=100)
tempLabel=Label(main,font=("Times bold",90),bg="#a6d4e0")
tempLabel.grid(row=1, sticky="E",padx=100)
Label(main,image=img, bg="#a6d4e0").grid(row=1,sticky="W",padx=100)
weather_state_lab=Label(main,font=("Times bold",25),bg="#a6d4e0")
weather_state_lab.grid(row=2,sticky="E",padx=100)

def import_weather():
    page=requests.get(url)
    soup= BeautifulSoup(page.content, "html.parser")
    city=soup.find("h1",class_="CurrentConditions--location--kyTeL").text
    temp=soup.find("span", class_="CurrentConditions--tempValue--3a50n").text
    weather_state=soup.find("div", class_="CurrentConditions--phraseValue--2Z18W").text
    cityLabel.config(text=city)
    tempLabel.config(text=temp)
    weather_state_lab.config(text=weather_state)
import_weather()

main.mainloop()



