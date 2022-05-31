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

def attack(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 ATTACK POKEMONS\n\nNORMAL\n\n👉 Nidoking\n👉 Machamp\n👉 Victreebel\n👉 Dragonite\n👉 Tyranitar\n👉 Blaziken\n👉 Swampert\n👉 Shiftry\n👉 Salamence\n👉 Staraptor\n👉 Luxray\n👉 Garchomp\n👉 Rhyperior\n👉 Electivire\n👉 Mamoswine\n👉 Gallade\n👉 Emboar\n👉 Stoutland\n👉 Unfezant\n👉 Gigalith\n👉 Conkeldurr\n👉 Leavanny\n👉 Krookodile\n👉 Eelektross\n👉 Haxorus\n👉 Decidueye\n👉 Incineroar\n👉 Toucannon\n👉 Tsareena\n\nLEGENDARY\n\n👉 Groudon\n👉 Regigigas\n👉 Tornadus(Incarnate Forme)\n👉 Thundurus(Incarnate Forme)\n👉 Landorus(Therian Forme)\n👉 Terrakion\n👉 Zekrom\n👉 Kyurem(Black)\n👉 Tapu Bulu\n👉 Solgalao\n👉 Kartana\n👉 Necrozma Dusk mane\n👉 Melmetal",
    )

def defence(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 DEFENCE POKEMONS\n\nNORMAL\n\n👉 Poliwrath\n👉 Golem\n👉 Aggron\n👉 Metagross\n👉 Klinklang\n👉 Chesnaught\n👉 Kommo-o\n\nLEGENDARY\n\n👉 Regirock\n👉 Cobalion\n👉 Stakataka  ",
    )

def spa(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 SPECIAL ATTACK POKEMONS\n\nNORMAL\n\n👉 Charizard\n👉 Vileplume\n👉 Alakazam\n👉 Gengar\n👉 Typhlosion\n👉 Ampharos\n👉 Beautifly\n👉 Gardevoir\n👉 Empolion\n👉 Roserade\n👉 Magnezone\n👉 Magmortar\n👉 Porygon-Z \n👉 Samurott\n👉 Reuniclus\n👉 Vanilluxe\n👉 Chandelure\n👉 Hydreigon\n👉 Volcarona\n👉 Delphox\n👉 Primarina\n👉 Vikavolt\n\nLEGENDARY\n\n👉 Zapdos\n👉 Moltres\n👉 Mewtwo\n👉 Latios\n👉 Kyogre\n👉 Dialga\n👉 Palkia\n👉 Reshiram\n👉 Volcanion\n👉 Lunala\n👉 Xurkitree\n👉 Magearna\n👉 Naganadel\n👉 Blacephalon\n👉 Tapu Lele\n👉 Heatran\n👉 Thundurus(Therian Forme)\n👉 Landorus(Incarnate Forme)\n👉 Keldeo(Ordinary/Resolute)\n👉 Kyurem(White)\n👉 Hoopa(Confined/Unbound)\n👉 Necrozma Dawn Wings",
    )

def spd(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 SPECIAL DEFENCE POKEMONS\n\nNORMAL\n\n👉 Blastoise\n👉 Bellossom\n👉 Politoed\n👉 Dustox\n👉 Ludicolo\n👉 Gothitelle\n👉 Florges\n👉 Goodra\n\nLEGENDARY\n\n👉 Articuno\n👉 Lugia\n👉 Ho-oh\n👉 Regice\n👉 Latias\n👉 Cresselia\n👉 Virizion\n👉 Tapu Fini\n👉 Nihilego",
    )

def speed(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "3 SPEED POKEMONS\n\nNORMAL\n\n👉 Pidgeot\n👉 Raichu\n👉 Crobat\n👉 Jumpluff\n👉 Sceptile\n👉 Serperior\n👉 Greninja\n👉 Talonflame\n\nLEGENDARY\n\n👉 Shaymin\n👉 Scolipede\n👉 Pheromosa\n👉 Zeraora\n👉 Tapu Koko\n👉 Tornadus(Therian Forme)\n👉 Deoxys(Speed Forme)",
    )

ATTACK_HANDLER = DisableAbleCommandHandler("attack", attack, run_async=True)
DEFENCE_HANDLER = DisableAbleCommandHandler("defence", defence, run_async=True)
SPA_HANDLER = DisableAbleCommandHandler("spa", spa, run_async=True)
SPD_HANDLER = DisableAbleCommandHandler("spd", spd, run_async=True)
SPEED_HANDLER = DisableAbleCommandHandler("speed", speed, run_async=True)

dispatcher.add_handler(ATTACK_HANDLER)
dispatcher.add_handler(DEFENCE_HANDLER)
dispatcher.add_handler(SPA_HANDLER)
dispatcher.add_handler(SPD_HANDLER)
dispatcher.add_handler(SPEED_HANDLER)
