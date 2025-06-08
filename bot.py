import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, services, orders, payments

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Register handlers
    start.register_handlers(dp)
    services.register_handlers(dp)
    orders.register_handlers(dp)
    payments.register_handlers(dp)

    print("Bot ishga tushmoqda...")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
