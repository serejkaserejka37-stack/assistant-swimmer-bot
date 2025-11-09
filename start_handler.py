from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from database.crud import get_user_by_telegram_id, create_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = str(user.id)
    first_name = user.first_name or "Пользователь"
    
    existing_user = get_user_by_telegram_id(user_id)
    if not existing_user:
        create_user(telegram_id=user_id, first_name=first_name)
    
    welcome_text = f"""🏊 <b>Добро пожаловать в Assistant Swimmer Bot!</b>

Привет, {first_name}! 

Я анализирую твою технику плавания кроль по видео.

<b>Как это работает:</b>
1. Загрузи видео (10-30 сек)
2. Оплати анализ (300 ₽)
3. Получи подробный отчет с упражнениями

<b>Готов начать? Загрузи видео! 🎥</b>"""
    
    await update.message.reply_text(welcome_text, parse_mode='HTML')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """<b>📖 Справка</b>

Команды:
/start - Начать
/help - Помощь
/about - О боте

Для анализа: просто отправь видео!"""
    
    await update.message.reply_text(help_text, parse_mode='HTML')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """<b>🏊 О боте</b>

Assistant Swimmer Bot v1.0
Анализ техники плавания с помощью AI

Технологии:
• MediaPipe Pose
• Telegram Bot API
• SQLAlchemy DB

Разработчик: Assistant Team"""
    
    await update.message.reply_text(about_text, parse_mode='HTML')
