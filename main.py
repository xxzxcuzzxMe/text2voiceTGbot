from config import TOKEN
from aiogram import Bot, Dispatcher, types


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)
    await dp.start_polling()


@dp.message(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('test')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
