import json
from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

#api
url_api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# #filehandling
config_file='openweather.ini'
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']  #all these filees will be in json


def get_weather(city):
    result=requests.get(url_api.format(city,api_key))
    if result:
        json=result.json() 
        #it gets value in tuples like(city,country,temp,icon)
        city=json['name']
        country=json['sys']['country']
        temp_kelvin=json['main']['temp']
        temp_celcius=temp_kelvin -273.15
        temp_fahrenheit=(temp_kelvin - 273.15)*9/5 +32
        icon=json['weather'][0]['icon']
        weather=json['weather'][0]['main']
        final=(city,country,temp_celcius,temp_fahrenheit,icon,weather)
        return final
    else:
        return None
print(get_weather('London'))


def search():
    city=enter_city.get()
    weather=get_weather(city)
    if weather:
        location_entry['text']='{},{}'.format(weather[0],weather[1])
        temparature_entry['text']='{:.2f}C,{:.2f}F'.format(weather[2],weather[3])
        weather_entry['text']='{}'.format(weather[5])
    else:
        messagebox.showerror('Error','CANNOT FIND THE CITY{}'.format(city))

root=Tk()
root.title("WEATHER-GUI")
root.config(background="lightblue")
root.geometry("700x400")


#searching city
search_city=StringVar()
#entry box for searching city
enter_city=Entry(root,textvariable=search_city,fg="black",font=("times",20,"bold"),width=30)
enter_city.pack()


#search buttom
search_button=Button(root,text="SEARCH",font=("times",20,"bold"),width=20,bg="lightgreen",fg="black",command=search)
search_button.pack()

#LABLE TO SHOW LOCATION OF CITY
location_entry=Label(root,text="",font=("times",20,"bold"),bg="lime")
location_entry.pack()

#label to show temperature
temparature_entry=Label(root,text="",font=("times",30,"bold"),bg="lightpink")
temparature_entry.pack()

# #BITMAP IMAGE
# image=Label(root,bitmap="")
# image.pack()

#ADDING WEATHER
weather_entry=Label(root,text="",font=("times",30,"bold"),bg="yellow")
weather_entry.pack()


root.mainloop()