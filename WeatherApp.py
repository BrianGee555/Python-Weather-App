#Import Neccessary Libraries and Declare my API key in order for weather app to retrieve weather.
import os
import requests

api_key = 'c58ef6d5b00c01e39a0d825ea81f6d67'

#Main Selection Menu , Relatively Straight Forward
def mainmenu():

    os.system('cls')

    home_selection_choice = input(""" Welcome to Weather App
                                  
    Check Weather Today (1)                                                       
    
    Exit (2)                           
                                  
    """)

#Check for Valid input and redirect to proper function
    if home_selection_choice == '1':

        pull_weather()

        mainmenu()


    if home_selection_choice == '2':

        exit()

    
    else:
        
        os.system('cls')

        input("Invalid Input Press Enter to Continue: ")

        mainmenu()

#Retrieves weather data from "openweathermap" using a free account and its associated API key.
def pull_weather():
    
    os.system('cls')

    city = input('Enter city name: ')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    #Checks for valid response from server
    if response.status_code == 200:

        data = response.json()

        temp = data['main']['temp']

        desc = data['weather'][0]['description']

    #Display gathered info
        print(f'\nTemperature: {temp} K')

        print(f'\nDescription: {desc}')

        input("\nPress Enter to Continue: ")

        mainmenu()
    
    #User input handling
    else:

        os.system('cls')

        input("Invalid Input, Press Enter to Continue: ")

        mainmenu()

#Run intial instance of selection screen
mainmenu()