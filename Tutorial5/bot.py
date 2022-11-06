from dotenv import load_dotenv
from telegram import Update,Bot
from telegram.ext import Updater,MessageHandler,Filters
from telegram.utils.request import Request
import os

#load api key from env file
load_dotenv()
pwd=os.getenv("API_KEY")

def message_handler(update,context):
    user_message=update.message.text
    user_info=update.message
    dict={"First_Name":user_info.from_user.first_name,"User_Name":user_info.from_user.username,"Message":user_message}
    print(dict)

def main():
    req=Request(con_pool_size=10,connect_timeout=0.5)
    t_bot=Bot(request=req,token=pwd)
    updater=Updater(bot=t_bot,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.all,callback=message_handler))
    updater.start_polling()
    updater.idle()


if __name__=="__main__":
    main()