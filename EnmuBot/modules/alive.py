# ALIVE.PY MADE USING PYROGRAM
##. @Yash_Sharma_1807
# Yash-Sharma-1807


import pyrogram
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message)
from EnmuBot import pbot
from telegram import __version__ as PTBV
from telethon import __version__ as THV
from platform import python_version
from pyrogram import __version__ as PYRV

ALIVE_PH = "https://telegra.ph/file/99c8370d64b59ff87adc9.jpg"

@pbot.on_message(filters.command('alive'))
async def alive(_,message:Message):
  await message.reply_photo(photo = ALIVE_PH,
                      caption = ("I'm alive Running on \nPython - `{}`\nPTB Version - `{}`\nTelethon Version - `{}`\nPyrogram Version - `{}`").format(python_version(),PTBV,THV,PYRV),
                                            reply_markup = InlineKeyboardMarkup(
                                                  [
                                                        [ InlineKeyboardButton (text = 'Support' , url = 'https://t.me/strangers_bots')],
                                                        [InlineKeyboardButton (text = 'Help' , url = 't.me/alexaprobot?start=help')]]))
                                                        
                                                        
                                                        


