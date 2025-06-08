import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, services, orders
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="menu", description="Asosiy menyu"),
    ]
    await bot.set_my_commands(commands)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Register handlers
    start.register_handlers(dp)
    services.register_handlers(dp)
    orders.register_handlers(dp)

    await set_commands(bot)

    print("Umra Jet bot ishga tushmoqda...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
