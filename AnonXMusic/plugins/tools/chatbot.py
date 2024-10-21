from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import markdown
from info import *
import requests

storage = MemoryStorage()

class Chatbot(StatesGroup):
    chatbot_on = State()
    chatbot_off = State()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hello! I'm a chatbot. I can help you with any questions you have.")

@dp.message_handler(commands=['chatbot'])
async def chatbot(message: types.Message):
    if message.chat.type == 'group' and message.from_user.id == message.chat.get_administrators()[0].user.id:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        on_button = types.InlineKeyboardButton(text="ON", callback_data="chatbot_on")
        off_button = types.InlineKeyboardButton(text="OFF", callback_data="chatbot_off")
        keyboard.add(on_button, off_button)
        await message.reply("Do you want to activate chatbot service in this group?", reply_markup=keyboard)
    else:
        await message.reply("You need to be an administrator of this group to activate the chatbot service.")

@dp.callback_query_handler(lambda c: c.data == 'chatbot_on')
async def chatbot_on(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(Chatbot.chatbot_on)
    await callback_query.message.edit_text("Chatbot service activated!")

@dp.callback_query_handler(lambda c: c.data == 'chatbot_off')
async def chatbot_off(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(Chatbot.chatbot_off)
    await callback_query.message.edit_text("Chatbot service deactivated!")

@dp.message_handler(state=Chatbot.chatbot_on)
async def chatbot_on_message(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user_message = message.text
    response = requests.get(API_URL.format(chat=user_message, model="blackbox")).json()
    bot_message = response["chat"]["text"]
    await message.reply(bot_message)

@dp.message_handler(state=Chatbot.chatbot_off)
async def chatbot_off_message(message: types.Message):
    await message.reply("Chatbot service is currently disabled. Please contact an administrator to activate it.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
