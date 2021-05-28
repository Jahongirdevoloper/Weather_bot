import requests
from config import dp, bot
from aiogram import types
from keyboards import main_keyboard

@dp.message_handler(commands=['start','help'])
async def start_and_help(message:types.Message):
    await message.reply("Botga hush kelibsiz, Iltimos shahringizni kiriting! ",reply_markup=main_keyboard)


@dp.message_handler()
async def weather_sender(message: types.Message):
    city = message.text
    res = requests.api.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=eb2b0c7cfe10be08fe08251e95de8aa2')
    if res.ok:
        d = res.json()
    if (d['main']['temp']-273.15)>20:
        temp = '☀️'
    elif (d['main']['temp']-273.15)>10:
        temp = '⛅️'
    elif (d['main']['temp']-273.15)>0:
        temp = '🌧'
    elif (d['main']['temp']-273.15)<0:
        temp = '❄️'
    await message.reply(f" {city}\n\n Bugun\n\n {temp}   +{d['main']['temp']-273.15:.0f}°\n\n Namlik:    {d['main']['humidity']}%\n\
 Shamol tezlik:   {d['wind']['speed']} m/s\n Bosim:   {d['main']['pressure']} mm  sim.ust\n\n")

# humidity->namlik
# description->tazsif
# speed->tezlik
# pressure->bosim


#     print("Temratura: ",d["main"]['temp'] - 273.15)

