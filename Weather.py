#pyown

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('ce002a6406e95acdafa4b6241178d5ce')
mgr = owm.weather_manager()


place = input('In who city ;')
observation = mgr.weather_at_place(place)
w = observation.weather

print(w)
print("------------------\n")
print(w.detailed_status)         # 'clouds'
print(w.clouds)
print(w.wind())                  # {'speed': 4.6, 'deg': 330}
print(w.humidity)                # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain)                    # {}
print(w.heat_index)              # None
print(w.clouds)                  # 75


temp = w.temperature('celsius')["temp"]
print("В цьому селі\місті температура :" + str(temp))
wind_1 = w.wind()['speed']
print("В цьому селі\місті wind(%):" + str(wind_1))

if temp < 10:
    print("Ohhh, so cold, take a cap")
else:
    print("Wether is So HOT!!!")

if wind_1 < 5:
    print('Wind is so leight')
else:
    print('Strong Wind')
l = input()
