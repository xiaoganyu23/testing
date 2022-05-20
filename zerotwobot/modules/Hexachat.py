import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


@register(pattern=("/hexa"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Officer Jenny.** \n\n"
  TEXT += "❍ **This is hexa command** \n\n"
  TEXT += f"❍ **My Master : [AYATO](https://t.me/SILVER_KING)** \n\n"
  TEXT += "❍ **Use /faction - to know about faction and how to join them** \n\n"
  TEXT += "❍ **Currently this bot has 100+ Pokemon Best nature added.** \n\n"
  TEXT += "❍ **In future we will soon add about safari, about nature, about elements** \n\n"
  TEXT += "**Thanks For Using me**"
  await tbot.send_message(event.chat_id, caption=TEXT)
