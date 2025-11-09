import logging
import asyncio
from telegram.ext import Application
from config import TELEGRAM_BOT_TOKEN, LOG_LEVEL
from handlers.start_handler import start, help_command, about_command
from handlers.video_handler import video_handler
from handlers.payment_handler import pre_checkout_handler, successful_payment_handler
from database.crud import init_db

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    logger.info("🚀 Запуск Assistant Swimmer Bot...")
    
    # Инициализация БД
    init_db()
    logger.info("📦 Инициализация БД...")
    
    # Создание приложения
    application = Application.builder().token(8592300728:AAF5o2AFFU5_GMZC9bY-zvKNkvCLQQAkxpU).build()
    
    # Регистрация обработчиков
    application.add_handler(start)
    application.add_handler(help_command)
    application.add_handler(about_command)
    application.add_handler(video_handler)
    application.add_handler(pre_checkout_handler)
    application.add_handler(successful_payment_handler)
    
    logger.info("📝 Регистрация обработчиков...")
    logger.info("✅ Обработчики зарегистрированы")
    
    logger.info("🎯 Бот готов к работе!")
    
    # Запуск бота
    if __name__ == '__main__':
        logger.info("🔄 Polling mode (разработка)")
        application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
