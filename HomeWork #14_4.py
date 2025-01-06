import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup


from _config import *
from _keyboards import *
from crud_functions import *
import _texts

logging.basicConfig(level=logging.INFO)
bot = Bot(token = API)
dp = Dispatcher(bot, storage = MemoryStorage())

initiate_db()
# Заполняем базу данных
Product1 = add_product(_texts.productName_1, _texts.productDescription_1, _texts.price_product1)
Product2 = add_product(_texts.productName_2, _texts.productDescription_2, _texts.price_product2)
Product3 = add_product(_texts.productName_3, _texts.productDescription_3, _texts.price_product3)
Product4 = add_product(_texts.productName_4, _texts.productDescription_4, _texts.price_product4)

products_from_db = get_all_products()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f"Привет, {message.from_user.username}! Давай посчитаем калории...", reply_markup=kb_start)

@dp.message_handler(text = ['Информация'])
async def main_menu(message):
    await message.answer("БлаБлаБла", reply_markup=kb_start)

@dp.message_handler(text = ['Купить'])
async def get_buying_list(message):
    with open('files/EWA_Women.png', "rb") as img1:
        product_item = products_from_db[0]
        await message.answer(f"Название: {product_item[1]} | Описание: {product_item[2]} | "
                             f"Цена: {product_item[3]} руб.")
        await message.answer_photo(img1)
    with open('files/EWA_Men.png', "rb") as img2:
        product_item = products_from_db[1]
        await message.answer(f"Название: {product_item[1]} | Описание: {product_item[2]} | "
                             f"Цена: {product_item[3]} руб.")
        await message.answer_photo(img2)
    with open('files/EWA_Detox.png', "rb") as img3:
        product_item = products_from_db[2]
        await message.answer(f"Название: {product_item[1]} | Описание: {product_item[2]} | "
                             f"Цена: {product_item[3]} руб.")
        await message.answer_photo(img3)
    with open('files/EWA_Immuno.png', "rb") as img4:
        product_item = products_from_db[3]
        await message.answer(f"Название: {product_item[1]} | Описание: {product_item[2]} | "
                             f"Цена: {product_item[3]} руб.")
        await message.answer_photo(img4)
    await message.answer('Выберите продукт для покупки', reply_markup=kb_catalog)

@dp.callback_query_handler(text = ['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!!!')
    await call.answer() #Строка нужна, чтобы Инлайт клавиатура не ожидала 30 секунд окончания выполнения хэндлера

@dp.message_handler(text = ['Рассчитать'])
async def main_menu(message):
    await message.answer("Выберите опцию...", reply_markup=kb_inline)

@dp.callback_query_handler(text = ['formulas'])
async def get_formulas(call):
    await call.message.answer(f"Ваша норма калорий: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5")

@dp.callback_query_handler(text = ['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = int(message.text))

    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {calories}ккал", reply_markup=kb_start)
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)