
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from botCommand import *
    


app = ApplicationBuilder().token("6172619513:AAFwjWeE7UA4TzOf015soCTrtTZexQvaczI").build()
print('start')

app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler('help', help))
app.add_handler(CommandHandler('time', time))

app.run_polling()

# %%%%%%%%%%%%%%%%%%%%%%%%
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# import datetime
# from spy import *

# def hi_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'Hi {update.effective_user.first_name}!')

# def help_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'/hi\n/time\n/help')


# def time_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}')


# def help_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'/hi\n/time\n/help')


# def time_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}')


# def sum_command(update: Update, context: CallbackContext):
#     log(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split() # /sum 123 534543
#     x = int(items[1])
#     y = int(items[2])
#     update.message.reply_text(f'{x} + {y} = {x+y}')
# %%%%%%%%%%%%%%%%%%%%%%%%%%

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

# def log(update: Update, context: CallbackContext):
#     file = open('db.csv', 'a')
#     file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
#     file.close()  

###########################

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# from bot_commands import *

# updater = Updater('6172619513:AAFwjWeE7UA4TzOf015soCTrtTZexQvaczI')

# updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
# updater.dispatcher.add_handler(CommandHandler('time', time_command))
# updater.dispatcher.add_handler(CommandHandler('help', help_command))
# updater.dispatcher.add_handler(CommandHandler('sum', sum_command))


# print('server start')
# updater.start_po