import requests
s_city = "Moscow,RU"
city_id = 524901
appid = "574df22602341367b397c152bc423885"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура", data['main']['temp_max'])
    print("Скорость ветра", data['wind']['speed'])
    print("Видимость", data['visibility'])
except Exception as e:
    print("Exception (weather):", e)
    pass
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    for i in data['list']:
        print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'], i['wind']['speed'], i['visibility'])
except Exception as e:
    print("Exception (forecast):", e)
    pass
