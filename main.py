# Umra Jet Premium Telegram Bot - Boshlang'ich fayl
# Fayl: main.py

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import logging
import os

# Token (TOKENNI SHU YERGA JOYLASHTIR)
API_TOKEN = os.getenv("BOT_TOKEN") or "7667056220:AAEc8DwQ0WJrBfVk_yLN8wLWGpxUfRKT-5A"

# Log
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# --- Start menyusi uchun tugmalar ---
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.add(
    KeyboardButton("🕋 Umra Paketlari"),
    KeyboardButton("🛂 Visa xizmatlari")
).add(
    KeyboardButton("🌙 Ravza / Tasreeh ruxsatnomalari"),
    KeyboardButton("🚗 Transport xizmatlari")
).add(
    KeyboardButton("🚆 Poezd biletlar"),
    KeyboardButton("✈️ Aviabiletlar")
).add(
    KeyboardButton("🍽️ Ovqat xizmatlari"),
    KeyboardButton("💳 To‘lov tizimlari")
).add(
    KeyboardButton("💸 Donat qilish"),
    KeyboardButton("👨‍💼 Admin panel / Buyurtma tizimi")
)

# --- Start komandasi ---
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    name = message.from_user.first_name
    welcome_text = f"""
Assalomu alaykum, <b>{name}</b>! 😊

<b>UmraJet</b> premium xizmatlar botiga xush kelibsiz!

👇 Quyidagi xizmatlardan foydalanishingiz mumkin:
🕋 Umra Paketlari
🛂 Visa xizmatlari
🌙 Ravza / Tasreeh ruxsatnomalari
🚗 Transport xizmatlari
🚆 Poezd biletlar
✈️ Aviabiletlar
🍽️ Ovqat xizmatlari
💳 To‘lov tizimlari
💸 Donat qilish
👨‍💼 Admin panel / Buyurtma tizimi

📣 Rasmiy kanal: @umrajet
📌 Ravza kanali: @the_ravza
👨‍💼 Managerlar: @vip_arabiy | @V001VB
"""
    await message.answer(welcome_text, reply_markup=start_keyboard)

# --- Botni ishga tushurish ---
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
