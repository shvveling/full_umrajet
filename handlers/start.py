from aiogram import types
from keyboards.main_menu import main_menu

async def cmd_start(message: types.Message):
    full_name = message.from_user.full_name or "Hurmatli mijoz"
    username = message.from_user.username

    welcome_text = (
        f"👋 Assalomu alaykum, <b>{full_name}</b>!\n\n"
        "UmraJet botga xush kelibsiz! 🌟\n\n"
        "Quyidagi xizmatlardan birini tanlang:\n"
        "🕋 Umra Paketlari\n"
        "🛂 Visa Xizmatlari\n"
        "🌙 Ravza / Tasreeh Ruxsatnomalari\n"
        "🚗 Transport Xizmatlari\n"
        "🚆 Po‘ezd Biletlar\n"
        "✈️ Aviabiletlar\n"
        "🍽️ Ovqat Xizmatlari\n"
        "💳 To‘lov Tizimlari\n"
        "💸 Donat Qilish\n"
        "👨‍💼 Admin Panel / Buyurtma Tizimi\n\n"
        "📢 Rasmiy kanallarimiz:\n"
        "🔹 @umrajet\n"
        "🔹 @the_ravza\n\n"
        "👨‍💼 Bog‘lanish uchun mas’ul managerlar:\n"
        "🔹 @vip_arabiy — Asosiy manager\n"
        "🔹 @V001VB — Zaxira manager\n\n"
    )

    if not username:
        welcome_text += (
            "⚠️ Sizda Telegram @username yo'q.\n"
            "Iltimos, managerlar bilan bog‘lanishda muammo bo‘lmasligi uchun @username o‘rnatishingizni so‘raymiz.\n"
            "Agar managerlar bilan bog‘lana olmasangiz, iltimos, bu haqda yozing."
        )
    await message.answer(welcome_text, reply_markup=main_menu)

def register_handlers(dp):
    dp.message.register(cmd_start, commands=["start", "menu"])
