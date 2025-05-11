import asyncio
from bot import Bot
from pyrogram import idle

bot = Bot()

async def main():
    await bot.start()
    print("🤖 Bot is running...")
    await idle()  # Keeps bot alive and listening
    await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
