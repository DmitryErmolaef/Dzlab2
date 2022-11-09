import requests

city = "Nekrasovka,RU"
appid = "e173e2835b248384d08be500b4e16f26"
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print(f'Прогноз погоды на день:\nГород:{city}\nПогодные условия:{data["weather"][0]["description"]}\nCкорость ветра:{data["wind"]["speed"]} м/с\nВидимость:{data["visibility"] / 100}%\nТемпература:{data["main"]["temp"]}\nМинимальная температура:{data["main"]["temp_min"]}\nМаксимальная температура: {data["main"]["temp_max"]}\n{"="*30}')

print("Прогноз погоды на неделю:")
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

for i in data['list']:
    print("Дата <", i['dt_txt'], ">\r\nВидимость: <", round((i['visibility'] / 10000)*100), '%',">\r\nСкорость ветра: <", i['wind']['speed'], ' м/с',">\r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",i['weather'][0]['description'], "> \n =================")
print("=" * 30)