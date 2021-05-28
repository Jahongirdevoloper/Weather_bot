from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Tashkent'),
            KeyboardButton('Samarkand'),
            KeyboardButton('Jizzax'),
        ],
        [
            KeyboardButton('Xiva'),
            KeyboardButton('Navoiy'),
            KeyboardButton('Buxoro'),
        ],
        [
            KeyboardButton('Termiz'),
            KeyboardButton('Qashqadaryo'),
            KeyboardButton('Sirdaryo'),
        ],
        [
            KeyboardButton('Andijon'),
            KeyboardButton('Fagona'),
            KeyboardButton('Namangan'),
        ]
    ],
    resize_keyboard=True
)