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


def normal(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Normal\n\nStrong Against (Damage Given X2):\nNone\n\nWeak Against (Damage Given X1/2):\nRock, Steel\nGhost (Damage Given X0)\n\nResistant To (Damage Recived X0):\nGhost\n\nVulnerable To (Damage Recived X2):\nFighting",
    )

def fighting(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Fighting\n\nStrong Against (Damage Given X2):\nNormal, Rock, Steel, Ice, Dark\n\nWeak Against (Damage Given X1/2):\nFlying, Poison, Psychic, Bug, Fairy\nGhost (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nRock, Bug, Dark\n\nVulnerable To (Damage Recived X2):\nFlying, Psychic, Fairy",
    )

def flying(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Flying\n\nStrong Against (Damage Given X2):\nFighting, Bug, Grass\n\nWeak Against (Damage Given X1/2):\nRock, Steel, Electric\n\nResistant To (Damage Recived X1/2):\nFighting, Bug, Grass\nGround (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nRock, Electric, Ice",
    )

def poison(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Poison\n\nStrong Against (Damage Given X2):\nGrass, Fairy\n\nWeak Against (Damage Given X1/2):\nPoison, Ground, Rock, Ghost\nSteel (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nFighting, Poison, Grass, Fairy, Bug\n\nVulnerable To (Damage Recived X2):\nGround, Psychic",
    )

def ground(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Ground\n\nStrong Against (Damage Given X2):\nPoison, Rock, Steel, Fire, Electric\n\nWeak Against (Damage Given X1/2):\nBug, Grass\nFlying (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nPoison, Rock\nElectric (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nWater, Grass, Ice",
    )

def rock(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Rock\n\nStrong Against (Damage Given X2):\nFlying, Bug, Fire, Ice\n\nWeak Against (Damage Given X1/2):\nFighting, Ground, Steel\n\nResistant To (Damage Recived X1/2):\nNormal, Flying, Poison, Fire\n\nVulnerable To (Damage Recived X2):\nFighting, Ground, Steel, Water, Grass",
    )
def bug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Bug\n\nStrong Against (Damage Given X2):\nGrass, Psychic, Dark\n\nWeak Against (Damage Given X1/2):\nFighting, Flying, Poison, Ghost, Steel, Fire, Fairy\n\nResistant To (Damage Recived X1/2):\nFighting, Ground, Grass\n\nVulnerable To (Damage Recived X2):\nFlying, Rock, Fire",
    )

def ghost(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Ghost\n\nStrong Against (Damage Given X2):\nGhost, Psychic\n\nWeak Against (Damage Given X1/2):\nDark\nNormal (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nPoison, Bug\nNormal, Fighting (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nGhost, Dark",
    )

def steel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Steel\n\nStrong Against (Damage Given X2):\nRock, Ice, Fairy\n\nWeak Against (Damage Given X1/2):\nSteel, Fire, Water, Electric\n\nResistant To (Damage Recived X1/2):\nNormal, Flying, Rock, Bug, Steel, Grass, Psychic, Ice, Dragon, Fairy\nPoison (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nFighting, Ground, Fire",
    )

def fire(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Fire\n\nStrong Against (Damage Given X2):\nBug, Steel, Grass, Ice\n\nWeak Against (Damage Given X1/2):\nRock, Fire, Water, Dragon\n\nResistant To (Damage Recived X1/2):\nBug, Steel, Fire, Grass, Ice, Fairy\n\nVulnerable To (Damage Recived X2):\nGround, Rock, Water",
    )

def water(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Water\n\nStrong Against (Damage Given X2):\nGround, Rock, Fire\n\nWeak Against (Damage Given X1/2):\nWater, Grass, Dragon\n\nResistant To (Damage Recived X1/2):\nSteel, Fire, Water, Ice\n\nVulnerable To (Damage Recived X2):\nGrass, Electric",
    )

def grass(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Grass\n\nStrong Against (Damage Given X2):\nGround, Rock, Water\n\nWeak Against (Damage Given X1/2):\nFlying, Poison, Bug, Steel, Fire, Grass, Dragon\n\nResistant To (Damage Recived X1/2):\nGround, Water, Grass, Electric\n\nVulnerable To (Damage Recived X2):\nFlying, Poison, Bug, Fire, Ice",
    )

def electric(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Electric\n\nStrong Against (Damage Given X2):\nFlying, Water\n\nWeak Against (Damage Given X1/2):\nGrass, Electric, Dragon\nGround (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nFlying, Steel, Electric\n\nVulnerable To (Damage Recived X2):\nGround",
    )

def psychic(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Psychic\n\nStrong Against (Damage Given X2):\nFighting, Poison\n\nWeak Against (Damage Given X1/2):\nSteel, Psychic\nDark (Damage Given X0)\n\nResistant To (Damage Recived X1/2:)\nFighting, Psychic\n\nVulnerable To (Damage Recived X2):\nBug, Ghost, Dark",
    )

def ice(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Ice\n\nStrong Against (Damage Given X2):\nFlying, Ground, Grass, Dragon\n\nWeak Against (Damage Given X1/2):\nSteel, Fire, Water, Ice\n\nResistant To (Damage Recived X1/2):\nIce\n\nVulnerable To (Damage Recived X2):\nFighting, Rock, Steel, Fire",
    )

def dragon(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Dragon\n\nStrong Against (Damage Given X2):\nDragon\n\nWeak Against (Damage Given X1/2):\nSteel\nFairy (Damage Given X0)\n\nResistant To (Damage Recived X1/2):\nFire, Water, Grass, Electric\n\nVulnerable To (Damage Recived X2):\nIce, Dragon, Fairy",
    )

def dark(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Dark\n\nStrong Against (Damage Given X2):\nGhost, Psychic\n\nWeak Against (Damage Given X1/2):\nFighting, Dark, Fairy\n\nResistant To (Damage Recived X1/2):\nGhost, Dark\nPsychic (Damaged Recived X0)\n\nVulnerable To (Damage Recived X2):\nFighting, Bug, Fairy",
    )

def fairy(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "Type:Fairy\n\nStrong Against (Damage Given X2):\nFighting, Dragon, Dark\n\nWeak Against (Damage Given X1/2):\nPoison, Steel, Fire\n\nResistant To (Damage Recived X1/2):\nFighting, Bug, Dark\nDragon (Damage Recived X0)\n\nVulnerable To (Damage Recived X2):\nPoison, Steel",
    )

NORMAL_HANDLER = DisableAbleCommandHandler("normal", normal, run_async=True)
FIGHTING_HANDLER = DisableAbleCommandHandler("fighting", fighting, run_async=True)
FLYING_HANDLER = DisableAbleCommandHandler("flying", flying, run_async=True)
POISON_HANDLER = DisableAbleCommandHandler("poison", poison, run_async=True)
GROUND_HANDLER = DisableAbleCommandHandler("ground", ground, run_async=True)
ROCK_HANDLER = DisableAbleCommandHandler("rock", rock, run_async=True)
BUG_HANDLER = DisableAbleCommandHandler("bug", bug, run_async=True)
GHOST_HANDLER = DisableAbleCommandHandler("ghost", ghost, run_async=True)
STEEL_HANDLER = DisableAbleCommandHandler("steel", steel, run_async=True)
FIRE_HANDLER = DisableAbleCommandHandler("fire", fire, run_async=True)
WATER_HANDLER = DisableAbleCommandHandler("water", water, run_async=True)
GRASS_HANDLER = DisableAbleCommandHandler("grass", grass, run_async=True)
ELECTRIC_HANDLER = DisableAbleCommandHandler("electric", electric, run_async=True)
PSYCHIC_HANDLER = DisableAbleCommandHandler("psychic", psychic, run_async=True)
ICE_HANDLER = DisableAbleCommandHandler("ice", ice, run_async=True)
DRAGON_HANDLER = DisableAbleCommandHandler("dragon", dragon, run_async=True)
DARK_HANDLER = DisableAbleCommandHandler("dark", dark, run_async=True)
FAIRY_HANDLER = DisableAbleCommandHandler("fairy", fairy, run_async=True)

dispatcher.add_handler(NORMAL_HANDLER)
dispatcher.add_handler(FIGHTING_HANDLER)
dispatcher.add_handler(FLYING_HANDLER)
dispatcher.add_handler(POISON_HANDLER)
dispatcher.add_handler(GROUND_HANDLER)
dispatcher.add_handler(ROCK_HANDLER)
dispatcher.add_handler(BUG_HANDLER)
dispatcher.add_handler(GHOST_HANDLER)
dispatcher.add_handler(STEEL_HANDLER)
dispatcher.add_handler(FIRE_HANDLER)
dispatcher.add_handler(WATER_HANDLER)
dispatcher.add_handler(GRASS_HANDLER)
dispatcher.add_handler(ELECTRIC_HANDLER)
dispatcher.add_handler(PSYCHIC_HANDLER)
dispatcher.add_handler(ICE_HANDLER)
dispatcher.add_handler(DRAGON_HANDLER)
dispatcher.add_handler(DARK_HANDLER)
dispatcher.add_handler(FAIRY_HANDLER)
