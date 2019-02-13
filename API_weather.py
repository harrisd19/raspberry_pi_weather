import requests

def get_all_weather():
    payload = {'id':'5180225', 'appid':'b11cb1a1d02b30e459bd6c5ce5615c1e', 'units':'imperial', 'mode':'json'}
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params = payload)
    weather_data = response.json()
    return weather_data

def get_temp(all_weather_data):
    current_temp = all_weather_data['main']['temp']
    return current_temp

def get_city(all_weather_data):
    selected_city = all_weather_data['name']
    return selected_city

def main():
    all_weather = get_all_weather()
    print (get_temp(all_weather))
    print (get_city(all_weather))

if __name__ == "__main__":
    main()

