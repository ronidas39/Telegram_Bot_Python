
from dotenv  import load_dotenv
from telegram import Bot,Update
from telegram.ext import Updater,CommandHandler
from telegram.utils.request import Request
import os
from datetime import datetime


load_dotenv()
pwd=os.getenv("API_KEY")

def get_time(update,context):
    print(update.message.text)
    now=datetime.now()
    dt_string=now.strftime("%d/%m/%Y_%H:%M:%S")
    update.message.reply_text(f"Current Time is : {dt_string}")

def main():
    req=Request(connect_timeout=0.5)
    my_bot=Bot(token=pwd,request=req)
    updater=Updater(bot=my_bot,use_context=True)
    dp=updater.dispatcher
#adding commands
    cmd=[("gettime","get the current date time in string format")]
    my_bot.set_my_commands(cmd)
    dp.add_handler(CommandHandler("gettime",get_time))
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
