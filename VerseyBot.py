from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace this with your bot token
BOT_TOKEN = '7810481488:AAFl5CWCMzt9NgsrRmEVTaIjATlpPhXkUII'

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Play Clicker Game", web_app={"url": "https://akkannkkshaa.github.io/TRADEVERSE"})]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text("Welcome to the Clicker Game! Click the button below to start playing.", reply_markup=reply_markup)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
