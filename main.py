import asyncio
import logging

from keep_alive import keep_alive
from moderator_logic import dp, bot, shutdown

logging.basicConfig(level=logging.INFO)

# Запускаем keep_alive сервер для Replit
keep_alive()

async def main():
    logging.info("Запуск бота...")
    try:
        await dp.start_polling(bot)
    finally:
        try:
            await shutdown()
        except Exception:
            pass
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
