from telegram.ext import Updater, CommandHandler


def start(update,context):
    
    update.message.reply_text('hola mundo')


if __name__ == '__main__':

    updater = Updater(token='1701235964:AAEXvfD57oiuBY85dWb7bAIWF-c2bgn9VIY', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()

    

    updater.idle()
