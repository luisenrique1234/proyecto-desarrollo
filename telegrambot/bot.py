from telegram.ext import Updater, CommandHandler


def start(update,context):
    
    update.message.reply_text('hola mundo')


if __name__ == '__main__':

    updater = Updater(token='you taken', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()

    

    updater.idle()
