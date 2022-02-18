from turtle import update
from dotenv import load_dotenv
from telegram import Update,Bot
from telegram.ext import Updater,MessageHandler,Filters
from telegram.utils.request import Request
import os
#get api key from env
load_dotenv()
pwd=os.getenv("API_KEY")

def mesaage_handler(update,context):
    user_message=update.message.text
    print(user_message)
    if(user_message.lower() == "hi"):
        update.message.reply_text(f'hello , how can i help you')
    else:
        update.message.reply_text(f'you sent the following: {update.message.text}')


def main():
    req=Request(connect_timeout=0.5)
    t_bot=Bot(request=req,token=pwd)
    updater=Updater(bot=t_bot,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.all,callback=mesaage_handler))
    updater.start_polling()
    updater.idle()

if __name__=='__main__':
    main()


    



