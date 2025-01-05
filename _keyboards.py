from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_start = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton('Рассчитать'),
            KeyboardButton('Информация')
        ],
        [
            KeyboardButton('Купить')
        ]
    ], resize_keyboard = True
)

kb_inline = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton('Формула расчёта', callback_data='formulas')
        ]
    ]
)

kb_catalog = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton('Product1', callback_data='product_buying'),
            InlineKeyboardButton('Product2', callback_data='product_buying'),
            InlineKeyboardButton('Product3', callback_data='product_buying'),
            InlineKeyboardButton('Product4', callback_data='product_buying')
        ]
    ]
)

# kb_buy = InlineKeyboardMarkup(
#     inline_keyboard = [
#         [InlineKeyboardButton('Оплатить', url = 'https://www.wildberries.ru/brands/310797852-ewa-product')],
#         [InlineKeyboardButton('Назад', callback_data='back_to_catalog')]
#     ]
# )