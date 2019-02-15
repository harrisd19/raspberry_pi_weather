import requests

def get_all_current_weather():
    payload = {'id':'5180225', 'appid':'b11cb1a1d02b30e459bd6c5ce5615c1e', 'units':'imperial', 'mode':'json'}
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params = payload)
    print(response.text)
    weather_data = response.json()
    return weather_data

def get_current_temp(all_current_weather_data):
    current_temp = all_current_weather_data['main']['temp']
    return current_temp

def get_current_city(all_current_weather_data):
    selected_city = all_current_weather_data['name']
    return selected_city

def get_current_wind_condition(all_current_weather_data):
    wind_direction_in_degrees = int(all_current_weather_data['wind']['deg'])
    wind_speed_in_mph = int(all_current_weather_data['wind']['speed'])

    return wind_direction_in_degrees, wind_speed_in_mph

def get_current_conditions(all_current_weather_data):
    current_condition_code = int(all_current_weather_data['weather'][0]['id'])
    current_condition_main = str(all_current_weather_data['weather'][0]['main'])
    current_condition_description = str(all_current_weather_data['weather'][0]['description'])

    weather_icon = get_current_weather_icon(all_current_weather_data['weather'][0]['icon'])

    return weather_icon, current_condition_code, current_condition_main, current_condition_description
     
def get_current_weather_icon(icon_code):
    icon_url = 'http://openweathermap.org/img/w/' + icon_code + '.png'
    icon = requests.get(icon_url)
    return icon


def main():
    all_current_weather = get_all_current_weather()
    print (get_current_wind_condition(all_current_weather))
    print (get_current_conditions(all_current_weather))
    print (get_current_temp(all_current_weather))
    print (get_current_city(all_current_weather))

if __name__ == "__main__":
    main()

