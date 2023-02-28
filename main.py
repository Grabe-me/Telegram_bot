from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)
import random
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
     await message.answer('Привет! Напиши, сколько символов должен быть пароль, максимум 72 символа.')
@dp.message_handler()
async def get_password(message: types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if passlength < 0 and passlength > 72:
            await message.reply('Недопустимый размер пароля')
        else:
            await message.answer('Вот 5 вариантов пароля:')
            a = 'abcdefghijklmnopqrstuvwxyz'
            b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            c = '0123456789'
            d = '[]{}()*/,-_!?'
            all = a + b + c + d
            for password in range(1, 6):
                password = ''.join(random.sample(all, passlength))
                await message.answer(f"\t{password}")
                start = f"@dp.message_handler(commands=['start'])"
            await message.answer('Можем попробовать снова. Просто нажми /start')
    except Exception as ex2:
        print(ex2)
        await message.answer('Необходимо ввести подходящее число')
if __name__ == '__main__':
    executor.start_polling(dp)