import requests

def get_temp(all_weather_data):
    current_temp = all_weather_data['main']['temp']
    return current_temp

def get_city(all_weather_data):
    selected_city = all_weather_data['name']
    return selected_city

def main():
    payload = {'id':'5180225', 'appid':'b11cb1a1d02b30e459bd6c5ce5615c1e', 'units':'imperial', 'mode':'json'}
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params = payload)
    weather_data = response.json()    

    print(response.text)
    print (get_temp(weather_data))
    print (get_city(weather_data))

if __name__ == "__main__":
    main()

