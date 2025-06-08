from aiogram import types

async def services_handler(message: types.Message):
    services_map = {
        "🕋 Umra Paketlari": "💎 Umra paketlarimiz:\n\nStandart Paket - 1200$\nVIP Paket - 1800$ dan boshlab",
        "🛂 Visa Xizmatlari": "Visa xizmatlarimiz bo‘yicha ma’lumotlar tez orada...",
        "🌙 Ravza / Tasreeh Ruxsatnomalari": "Ravza va tasreeh ruxsatnomalari haqida ma’lumot...",
        "🚗 Transport Xizmatlari": "Transport xizmatlarimiz: avtobus, mikroavtobus, taksi va boshqalar.",
        "🚆 Po‘ezd Biletlar": "Po‘ezd biletlar narxlari va rejalari.",
        "✈️ Aviabiletlar": "Aviabiletlar bo‘yicha eng so‘nggi takliflar.",
        "🍽️ Ovqat Xizmatlari": "Ovqatlanish xizmatlari haqida ma’lumot.",
        "💳 To‘lov Tizimlari": "To‘lov tizimlari: Click, Payme, Bank kartalari va boshqalar.",
        "💸 Donat Qilish": "Bizni qo‘llab-quvvatlash uchun donat qilishingiz mumkin.",
        "👨‍💼 Admin Panel / Buyurtma Tizimi": "Buyurtmalarni qabul qilish va admin panelga kirish uchun."
    }

    text = services_map.get(message.text, None)
    if text:
        await message.answer(text)

def register_handlers(dp):
    dp.message.register(services_handler, lambda message: message.text in [
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
