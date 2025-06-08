from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🕋 Umra Paketlari"), KeyboardButton(text="🛂 Visa Xizmatlari")],
        [KeyboardButton(text="🌙 Ravza / Tasreeh Ruxsatnomalari"), KeyboardButton(text="🚗 Transport Xizmatlari")],
        [KeyboardButton(text="🚆 Po‘ezd Biletlar"), KeyboardButton(text="✈️ Aviabiletlar")],
        [KeyboardButton(text="🍽️ Ovqat Xizmatlari"), KeyboardButton(text="💳 To‘lov Tizimlari")],
        [KeyboardButton(text="💸 Donat Qilish"), KeyboardButton(text="👨‍💼 Admin Panel / Buyurtma Tizimi")],
    ],
    resize_keyboard=True
)
