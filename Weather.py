import requests
 

hello = input("Welcome to the Weather Program! \n Press Enter to start your Search \n ")
 

def by_city():
    city = input('Please Enter The City Name You Are Looking For: ')
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=d9e31fd8e89a1cb219ffe0b49b43fac5&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)
 
 
    
    question = input('Do you want to conduct another search ? Type Yes or No: ')
    if question == 'Yes' or question == 'yes':
        main()
    if question == 'No' or question == 'no':
        print("Thank you for using the weather program. Have a great day!")
        exit()
 

def by_zip():
    zip_code = int(input('Please Enter The Zip Code You Are Looking For: '))
    
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=d9e31fd8e89a1cb219ffe0b49b43fac5'.format(zip_code)
    res = requests.get(url)
    
    data = res.json()
    show_data(data)
 
    
    question = input('Do you want to conduct another search ? Type Yes or No: ')
    if question == 'Yes' or question == 'yes':
        main()
    if question == 'No' or question == 'no':
        print("Thank you for using the weather program. Have a great day!")
        exit()
 

def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']
 
    print('Current Temperature : {} degrees fahrenheit'.format(temp))
    print('High Temperature : {} degrees fahrenheit'.format(hightemp))
    print('Low Temperature : {} degrees fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(pressure))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))
 
 
def main():
    while True:
        answer = input("If you would like to find out the current weather information, please choose from the following.\nType City to request information by City.\nType Zip to request information by Zip Code.\n")
        if answer == 'City' or answer == 'city':
            try:
                by_city()
 
            except Exception:
                print(" Try again, please!")
                by_city()
        if answer == 'Zip' or answer == 'zip':
            try:
                by_zip()
 
            except Exception:
                print(" Try again, please!")
                by_zip()
        else:
            print("Unfortunately, we could not find your request. Please try again.")
 
main()
