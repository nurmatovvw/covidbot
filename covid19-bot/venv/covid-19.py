import datetime
import telebot
import requests

covid_api = 'https://covid-api.mmediagroup.fr/v1/cases?country={country}'
token = '2090470848:AAFBj4h2B9U1qC-xOmGmFnV-CJhFKY76dt0'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Hi, i'm Covid19-bot")

@bot.message_handler(content_types='text')
def send_data(message):
    covid = requests.get(covid_api.format(country=message.text.title()))
    covid_json = covid.json()
    today = datetime.datetime.now()
    data = f'The number of coronavirus cases in {message.text.title()}: {covid_json["All"]["confirmed"]} on date: {today.day}-{today.month}-{today.year}'
    bot.send_message(message.chat.id, data)


print ('Bot is working')
bot.infinity_polling()