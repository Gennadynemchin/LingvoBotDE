import os
import logging
from dotenv import load_dotenv
from tg_bot import start, hello, help_command
from telegram.ext import Application, CommandHandler, MessageHandler, filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)


def main():
    logger = logging.getLogger(__name__)
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    lingvo_token = os.getenv('LINGVO_TOKEN')

    application = Application.builder().token(tg_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT, hello))
    application.run_polling()


if __name__ == '__main__':
    main()
