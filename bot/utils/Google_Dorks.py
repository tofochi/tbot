from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, F, types
from aiogram.client.default import DefaultBotProperties
from handlers import start
from callbacks import callback

dp = Dispatcher()

dp.include_router(start.router)

@dp.message()
async def googel_dorks(message: types.Message):
    username = message.text.lower()

    text2 = f"""
🔎 <b>Google Dorks:</b>

• Общий поиск: <code>site:google.com/search?q={username}</code>
• Поиск по VK: <code>site:google.com/search?q=site:vk.com "{username}"</code>
• Поиск по Instagram: <code>site:google.com/search?q=site:instagram.com "{username}"</code>
• Поиск по Twitter: <code>site:google.com/search?q=site:twitter.com "{username}"</code>
• Поиск по Telegram: <code>site:google.com/search?q=site:t.me "{username}"</code>
• Поиск по Facebook: <code>site:google.com/search?q=site:facebook.com "{username}"</code>
• Поиск по GitHub: <code>site:google.com/search?q=site:github.com "{username}"</code>
• Поиск по YouTube: <code>site:google.com/search?q=site:youtube.com "{username}"</code>
• Поиск по TikTok: <code>site:google.com/search?q=site:tiktok.com "{username}"</code>
• Поиск по Reddit: <code>site:google.com/search?q=site:reddit.com "{username}"</code>

"""

    await message.answer("Результаты поиска по Google Dorks", text2)