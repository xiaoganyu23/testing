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

def tmall(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE LIST OF ALL TMS PRESENT IN HEXA:-\n\nTM02 -Thunder claw (80/100)\nTM03 -Psyshock (80/100)\nTM09 -Venoshock (65/100)\nTM10- Hidden power (60/100)\nTM13 -Ice Beam (90/100)\nTM14 -Blizzard (110/70)\nTM15 -Hyper Beam (150/90)\nTM22 -Solar Beam (120/100)\nTM23 -Smack Down (50/100)\nTM24 -Thunderbolt (90/100)\nTM25 -Thunder (110/70)\nTM26 -Earthquake (100/100)\nTM28 -Leech Life (80/100)\nTM29 -Psychic (90/100)\nTM30 -Shadow Ball (80/100)\nTM31 -Brick Break (75/100)\nTM34 -Sludge Wave (95/100)\nTM35 -Flamethrower (90/100)\nTM36 -Sludge Bomb (90/100)\nTM38 -Fire Blast (110/85)\nTM39 -Rock Tomb (60/95)\nTM40 -Aerial Ace (60/100)\nTM42 -Facade (70/100)\nTM43 -Flame Charge (50/100)\nTM46 -Thief (60/100)\nTM47 -Low Sweep (65/100)\nTM48 -Round (60/100)\nTM49 -Echoed Voice (40/100)\nTM50 -Ovearheat (130/90)\nTM51 -Steel Wings (70/90)\nTM52 -Focus Blast (120/70)\nTM53 -Energy Ball (90/100)\nTM54 -False swipe (40/100)\nTM55 -Scald (80/100)\nTM57 -Charge Beam (50/90)\nTM58 -Sky Drop (60/100)\nTM59 -Brutal Swing (60/100)\nTM62 -Acrobatics (55/100)\nTM65 -Shadow Claw (70/100)\nTM66 -Payback (50/100)\nTM67 -Smart Strike (70/100)\nTM68 -Giga Impact (150/90)\nTM71 -Stone Edge (100/80)\nTM72 -Volt Switch (70/100)\nTM76 -Fly (90/95)\nTM78 -Bulldoze (60/100)\nTM79 -Frost Breath (60/90)\nTM80 -Rock Slide (75/90)\nTM81 -X-Scissor (80/100)\nTM82 -Dragon Tail (60/90)\nTM83 -Infestation (70/100)\nTM84 -Poison Jab (80/100)\nTM85 -Dream Eater (100/100)\nTM89 -U-Turn (70/100)\nTM91 -Flash Cannon (80/100)\nTM93 -Wild Charge (90/100)\nTM94 -Surf (90/100)\nTM95 -Snarl (55/95)\nTM97 -Dark Pulse (80/100)\nTM98 -Waterfall (80/100)\nTM99 -Dazzling Gleam (80/100)",
    )
    
def tms(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "HERE ARE LIST OF ALL TMS PRESENT IN HEXA:-\n\nTM02 -Thunder claw (80/100)\nTM03 -Psyshock (80/100)\nTM09 -Venoshock (65/100)\nTM10- Hidden power (60/100)\nTM13 -Ice Beam (90/100)\nTM14 -Blizzard (110/70)\nTM15 -Hyper Beam (150/90)\nTM22 -Solar Beam (120/100)\nTM23 -Smack Down (50/100)\nTM24 -Thunderbolt (90/100)\nTM25 -Thunder (110/70)\nTM26 -Earthquake (100/100)\nTM28 -Leech Life (80/100)\nTM29 -Psychic (90/100)\nTM30 -Shadow Ball (80/100)\nTM31 -Brick Break (75/100)\nTM34 -Sludge Wave (95/100)\nTM35 -Flamethrower (90/100)\nTM36 -Sludge Bomb (90/100)\nTM38 -Fire Blast (110/85)\nTM39 -Rock Tomb (60/95)\nTM40 -Aerial Ace (60/100)\nTM42 -Facade (70/100)\nTM43 -Flame Charge (50/100)\nTM46 -Thief (60/100)\nTM47 -Low Sweep (65/100)\nTM48 -Round (60/100)\nTM49 -Echoed Voice (40/100)\nTM50 -Ovearheat (130/90)\nTM51 -Steel Wings (70/90)\nTM52 -Focus Blast (120/70)\nTM53 -Energy Ball (90/100)\nTM54 -False swipe (40/100)\nTM55 -Scald (80/100)\nTM57 -Charge Beam (50/90)\nTM58 -Sky Drop (60/100)\nTM59 -Brutal Swing (60/100)\nTM62 -Acrobatics (55/100)\nTM65 -Shadow Claw (70/100)\nTM66 -Payback (50/100)\nTM67 -Smart Strike (70/100)\nTM68 -Giga Impact (150/90)\nTM71 -Stone Edge (100/80)\nTM72 -Volt Switch (70/100)\nTM76 -Fly (90/95)\nTM78 -Bulldoze (60/100)\nTM79 -Frost Breath (60/90)\nTM80 -Rock Slide (75/90)\nTM81 -X-Scissor (80/100)\nTM82 -Dragon Tail (60/90)\nTM83 -Infestation (70/100)\nTM84 -Poison Jab (80/100)\nTM85 -Dream Eater (100/100)\nTM89 -U-Turn (70/100)\nTM91 -Flash Cannon (80/100)\nTM93 -Wild Charge (90/100)\nTM94 -Surf (90/100)\nTM95 -Snarl (55/95)\nTM97 -Dark Pulse (80/100)\nTM98 -Waterfall (80/100)\nTM99 -Dazzling Gleam (80/100)",
    )
    
TMALL_HANDLER = DisableAbleCommandHandler("tmall", tmall, run_async=True)
TMS_HANDLER = DisableAbleCommandHandler("tms", tms, run_async=True)

dispatcher.add_handler(TMALL_HANDLER)
dispatcher.add_handler(TMS_HANDLER)
