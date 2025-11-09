from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes
from analysis.mediapipe_analyzer import analyze_video
from handlers.payment_handler import request_payment
import os

async def video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    if not video:
        await update.message.reply_text("📹 Пожалуйста, отправь видео!")
        return
    
    file = await context.bot.get_file(video.file_id)
    file_path = f"/tmp/{video.file_id}.mp4"
    await file.download_to_drive(file_path)
    
    # Проверка формата и размера
    if video.file_size > 100 * 1024 * 1024:
        await update.message.reply_text("❌ Видео слишком большое (max 100MB)")
        os.remove(file_path)
        return
    
    await update.message.reply_text("🔄 Анализ видео... Это может занять 1-2 минуты.")
    
    try:
        analysis_result = analyze_video(file_path)
        os.remove(file_path)
        
        if analysis_result:
            # Отправляем отчет
            report_text = f"""<b>📊 Результат анализа</b>

{analysis_result['summary']}

<b>Обнаруженные ошибки:</b>
{analysis_result['errors']}

<b>Рекомендации:</b>
{analysis_result['recommendations']}"""
            
            await update.message.reply_text(report_text, parse_mode='HTML')
        else:
            await update.message.reply_text("❌ Не удалось проанализировать видео. Попробуй другое.")
    
    except Exception as e:
        await update.message.reply_text("❌ Ошибка анализа. Попробуй позже.")
        logger.error(f"Video analysis error: {e}")
