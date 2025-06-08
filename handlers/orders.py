from aiogram import types
from config import GROUP_ID

async def order_handler(message: types.Message):
    user = message.from_user
    username = user.username
    full_name = user.full_name or "No Name"

    # Username yo‘qmi, eslatma yuborish uchun
    if not username:
        await message.answer(
            "⚠️ Sizda Telegram @username yo'q. "
            "Iltimos, managerlar bilan bog‘lanishda muammo bo‘lmasligi uchun @username o‘rnatishingizni so‘raymiz."
        )

    order_text = (
        f"🆕 <b>Yangi buyurtma</b>!\n\n"
        f"<b>Foydalanuvchi:</b> {full_name} @{username if username else 'username yo‘q'}\n"
        f"<b>Telegram ID:</b> {user.id}\n"
        f"<b>Buyurtma matni:</b>\n{message.text}\n\n"
        f"⏰ Vaqt: <i>{message.date.strftime('%Y-%m-%d %H:%M:%S')}</i>"
    )

    await message.bot.send_message(GROUP_ID, order_text)
    await message.answer("Buyurtmangiz qabul qilindi! Tez orada managerlar siz bilan bog‘lanishadi.")

def register_handlers(dp):
    # Buyurtma sifatida qabul qilinadigan barcha matnli xabarlar
    dp.message.register(order_handler, lambda message: message.text not in [
        "🕋 Umra Paketlari",
        "🛂 Visa Xizmatlari",
        "🌙 Ravza / Tasreeh Ruxsatnomalari",
        "🚗 Transport Xizmatlari",
        "🚆 Po‘ezd Biletlar",
        "✈️ Aviabiletlar",
        "🍽️ Ovqat Xizmatlari",
        "💳 To‘lov Tizimlari",
        "💸 Donat Qilish",
        "👨‍💼 Admin Panel / Buyurtma Tizimi"
    ])
