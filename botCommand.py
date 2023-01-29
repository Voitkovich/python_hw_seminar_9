from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import datetime
from log import *


async def hi(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}')


async def help(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')


async def time(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')    