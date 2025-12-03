import os
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackContext

# Multi-language support
LANGUAGES = {
    'en': 'Hello! How can I help you?',
    'fa': 'سلام! چطور می توانم به شما کمک کنم؟',
    'es': '¡Hola! ¿Cómo puedo ayudarte?'
}

def start(update: Update, context: CallbackContext) -> None:
    user_language = context.user_data.get('language', 'en')
    update.message.reply_text(LANGUAGES[user_language], reply_markup=ForceReply(selective=True))

def setup_handlers(updater: Updater):
    updater.dispatcher.add_handler(CommandHandler('start', start))

if __name__ == '__main__':
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    updater = Updater(TOKEN)
    setup_handlers(updater)
    updater.start_polling()
    updater.idle()