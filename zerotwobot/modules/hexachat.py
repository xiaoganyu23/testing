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


def hexa(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Hi There\nThis is HeXa command.\nCurrently this bot has 100+ Pokemon Best nature added.\nIn future we will soon add about safari, about nature, about elements.\nUse /factions to know about factions and other stuff.",
    )

HEXA_HANDLER = DisableAbleCommandHandler("hexa", hexa, run_async=True)

dispatcher.add_handler(HEXA_HANDLER)
