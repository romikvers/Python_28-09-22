#pyown

import telebot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('ce002a6406e95acdafa4b6241178d5ce')
mgr = owm.weather_manager()

bot = telebot.TeleBot("5696104567:AAEoznXOltSaEVrB4DH_zBxfO75av6QVrxw")

@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
	bot.reply_to(message, "Hi! This is a SINOPTYK! About who city or village want you know about weather? \n Write right here!")

@bot.message_handler(content_types=['text'])
def send_echo(message):
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        wind_1 = w.wind()['speed']

        answer = "Weather in this place:" + "\n\n" + "Температура: " + str(temp) + "\n\n" + "Вітер(m/s): " + str(wind_1) + "\n\n"
        
        if temp < 10:
            answer += "Ohhh, so cold, take a cap!"
        else:
           answer += "Wether is So HOT!!!"

        if wind_1 < 5:
            answer += "\nWind is so leight!"
        else:
            answer += "\nStrong Wind!!!"
        
        bot.send_message(message.chat.id, answer)

bot.infinity_polling(none_stop = True)
 
