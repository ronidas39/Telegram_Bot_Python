import os, json
from aiohttp import request
from dotenv import load_dotenv
from telegram import Bot,Update
from telegram.ext import Updater
from telegram.utils.request import Request


load_dotenv()
pwd=os.getenv("API_KEY")

def main():
    req=Request(connect_timeout=0.5)
    bot=Bot(token=pwd,request=req)
    updater=Updater(bot=bot,use_context=True)
    cmd=[("ptbcmd11","description from ptbcmd11"),("ptbcmd22","description from ptbcmd22")]
    bot.set_my_commands(cmd)
    dp=updater.dispatcher
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()
