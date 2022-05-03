import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from zerotwobot.events import register
from zerotwobot import telethn as tbot


PHOTO = "https://telegra.ph/file/2c13e570944404a6c0d86.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Naruto Uzumaki.** \n\n"
  TEXT += "❍ **I'm Working Properly** \n\n"
  TEXT += f"❍ **My Master : [Rin Okumura](https://t.me/Redeye_Ghoul)** \n\n"
  TEXT += f"❍ **Library Version :** `{telever}` \n\n"
  TEXT += f"❍ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"❍ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✉️", "https://t.me/naruto_robot_support"), Button.url("𝙽𝙴𝚃𝚆𝙾𝚁𝙺 📡", "https://t.me/ignite_Xnetwork")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
