
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    


app = ApplicationBuilder().token("6172619513:AAFwjWeE7UA4TzOf015soCTrtTZexQvaczI").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()