import html
import random
import time

import zerotwobot.modules.fun_strings as fun_strings
from zerotwobot import dispatcher
from zerotwobot.modules.disable import DisableAbleCommandHandler
from zerotwobot.modules.helper_funcs.chat_status import is_user_admin
from zerotwobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

def types(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Here are the list of all commands.\nThese command will explain about damage given and damage recived\n\n/normal - To know about normal pokemon.\n/fighting - To know about fighting pokemon.\n/flying - To know about flying pokemon.\n/poison - To know about poison pokemon.\n/ground - To know about ground pokemon.\n/rock - To know about rock pokemon.\n/bug - To know about bug pokemon.\n/ghost - To know about ghost pokemon.\n/steel - To know about steel pokemon.\n/water - To know about water pokemon.\n/fire - To know about fire pokemon.\n/grass - To know about grass pokemon.\n/electric - To know about electric pokemon.\n/psychic - To know about psychic pokemon.\n/ice - To know about ice pokemon.\n/dragon - To know about dragon pokemon.\n/dark - To know about dark Pokemon.\n/fairy - To know about fairy pokemon.",
    )

def natures(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Nature are a mechanic that influences how a Pokémon stats grow.\nNature effect is limited to only 10%.\nHere are the list of commands\n\n/hardy - About hardy natured pokemon.\n/lonely - About lonely natured pokemon.\n/brave - About brave natured pokemon.\n/adamant - About adamant natured pokemon.\n/naughty - About naughty natured pokemon.\n/bold - About bold natured pokemon.\n/docile - About docile natured pokemon.\n/relaxed - About relaxed natured pokemon.\n/impish - About impish natured pokemon.\n/lax - About lax natured pokemon.\n/modest - About modest natured pokemon.\n/mild - About mild natured pokemon.\n/serious - About serious natured pokemon.\n/quiet - About quiet natured pokemon.\n/rash - About rash natured pokemon.\n/calm - About calm natured pokemon.\n/gentle - About gentle natured pokemon.\n/sassy - About sassy natured pokemon.\n/bashful - About bashful natured pokemon.\n/careful - About careful natured pokemon.\n/timid - About timid natured pokemon.\n/hasty - About hasty natured pokemon.\n/jolly - About jolly natured pokemon.\n/naive - About naive natured pokemon.\n/quirky - About quirky natured pokemon",
    )
    
TYPES_HANDLER = DisableAbleCommandHandler("types", types, run_async=True)
NATURES_HANDLER = DisableAbleCommandHandler("natures", natures, run_async=True)
    
dispatcher.add_handler(TYPES_HANDLER)
dispatcher.add_handler(NATURES_HANDLER)
