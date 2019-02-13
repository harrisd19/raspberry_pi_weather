import requests

def main():
    payload = {'id':'5180225', 'appid':'b11cb1a1d02b30e459bd6c5ce5615c1e', 'units':'imperial', 'mode':'json'}
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params = payload)
    weather_data = response.json()

    city = weather_data['name']
    current_weather = weather_data['main']['temp']
    print('The temperature in ' + city + ' is '+"%.2f" % current_weather)


if __name__ == "__main__":
    main()