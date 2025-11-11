from telegram import Update, LabeledPrice
from telegram.ext import PreCheckoutQueryHandler, MessageHandler, ContextTypes

ANALYSIS_PRICE = 30000  # 300 руб в копейках

async def request_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    await context.bot.send_invoice(
        chat_id=update.effective_chat.id,
        title="Анализ техники плавания",
        description="Подробный AI-анализ твоего видео",
        payload="analysis_payment",
        provider_token="",  # Для теста оставь пустым
        currency="RUB",
        prices=[LabeledPrice("Анализ", ANALYSIS_PRICE)]
    )

async def pre_checkout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

async def successful_payment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Оплата прошла успешно! Анализ начат...")
    # Здесь запускаем анализ видео
