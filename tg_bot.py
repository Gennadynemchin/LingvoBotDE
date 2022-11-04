from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(f"Hi {user.name}!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    # user_id = update.message.from_user.id
    if text:
        await update.message.reply_text(text)
