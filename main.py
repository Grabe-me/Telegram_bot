from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)
import random
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_name = message.from_user.username
    await message.answer(f'Привет, {user_name}! Напиши, сколько символов'
                         'должен быть пароль, максимум 72 символа.')
@dp.message_handler()
async def get_password(message: types.Message):
    passlength = message.text
    try:
        passlength = int(passlength)
        if passlength <= 0:
            await message.reply('Пароль не может быть меньше 0')
            await message.answer('Попробуй любое целое число от 1 до 72')
        elif passlength > 72:
            await message.reply('Слишком длинный пароль')
            await message.answer('Попробуй любое целое число от 1 до 72')
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
                #start = f"@dp.message_handler(commands=['start'])"
            if passlength < 6:
                await message.answer('Пароль меньше 6 символов считается "слабым"')
            await message.answer('Можем попробовать снова. Просто нажми /start')
    except Exception as ex2:
        print(ex2)
        await message.reply('Это не подойдет')
        await message.answer('Попробуй любое целое число от 1 до 72')
if __name__ == '__main__':
    executor.start_polling(dp)