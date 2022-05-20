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

def fire(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type: FIRE\n\nStrong against (Damage Given X2)\nBug, Steel, Grass, Ice\n\nWeak Against (Damage Given X1/2)\nRock, Fire, Water, Dragon\n\nResistant To (Damage Recived X1/2)\nBug, Steel, Fire, Grass, Ice, Fairy\n\nVulnerable To (Damage Recived X2)\nGround, Rock, Water",
    )

FIRE_HANDLER = DisableAbleCommandHandler("fire", fire, run_async=True)

dispatcher.add_handler(FIRE_HANDLER)
