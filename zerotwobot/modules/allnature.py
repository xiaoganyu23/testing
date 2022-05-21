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

def lonely(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ LONELY Pokemons ⚡️\n\n👍 Lonely\n\n👉 Effects :\n👉 Stats increase⬆️  : Attack\n👉 Stats decrease⬇️ : Defense",
    )

def brave(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ BRAVE Pokemons ⚡️\n\n👍 Brave\n\n👉 Effects :\n👉 Stats increase⬆️  : Attack\n👉 Stats decrease⬇️ : Speed",
    )

def adamant(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ ADAMANT Pokemons ⚡️\n\n👍 Adamant\n\n👉 Effects :\n👉 Stats increase⬆️  : Attack\n👉 Stats decrease⬇️ : Sp. Attack",
    )

def naughty(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ NAUGHTY Pokemons ⚡️\n\n👍 Naughty\n\n👉 Effects :\n👉 Stats increase⬆️  : Attack\n👉 Stats decrease⬇️ : Sp. Defense",
    )

def bold(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ BOLD Pokemons ⚡️\n\n👍 Bold\n\n👉 Effects :\n👉 Stats increase⬆️  : Defence\n👉 Stats decrease⬇️ : Attack",
    )

def relaxed(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ RELAXED Pokemons ⚡️\n\n👍 Relaxed\n\n👉 Effects :\n👉 Stats increase⬆️  : Defence\n👉 Stats decrease⬇️ : Speed",
    )

def impish(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ IMPISH Pokemons ⚡️\n\n👍 Impish\n\n👉 Effects :\n👉 Stats increase⬆️  : Defence\n👉 Stats decrease⬇️ : Sp. Attack",
    )

def lax(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ LAX Pokemons ⚡️\n\n👍 Lax\n\n👉 Effects :\n👉 Stats increase⬆️  : Defence\n👉 Stats decrease⬇️ : Sp. Defense",
    )

def timid(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ TIMID Pokemons ⚡️\n\n👍 Timid\n\n👉 Effects :\n👉 Stats increase⬆️  : Speed\n👉 Stats decrease⬇️ : Attack",
    )

def hasty(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ HASTY Pokemons ⚡️\n\n👍 Hasty\n\n👉 Effects :\n👉 Stats increase⬆️  : Speed\n👉 Stats decrease⬇️ : Defense",
    )

def jolly(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ JOLLY Pokemons ⚡️\n\n👍 Jolly\n\n👉 Effects :\n👉 Stats increase⬆️  : Speed\n👉 Stats decrease⬇️ : Sp. Attack",
    )

def naive(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ NAIVE Pokemons ⚡️\n\n👍 Naive\n\n👉 Effects :\n👉 Stats increase⬆️  : Speed\n👉 Stats decrease⬇️ : Sp. Defense",
    )

def modest(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ MODEST Pokemons ⚡️\n\n👍 Modest\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Attack\n👉 Stats decrease⬇️ : Attack",
    )

def mild(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ MILD Pokemons ⚡️\n\n👍 Mild\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Attack\n👉 Stats decrease⬇️ : Defense",
    )

def quiet(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ Quiet Pokemons ⚡️\n\n👍 Quiet\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Attack\n👉 Stats decrease⬇️ : Speed",
    )

def rash(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ RASH Pokemons ⚡️\n\n👍 Rash\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Attack\n👉 Stats decrease⬇️ : Sp. Defense",
    )

def calm(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ CALM Pokemons ⚡️\n\n👍 Calm\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Defense\n👉 Stats decrease⬇️ : Attack",
    )

def gentle(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ GENTLE Pokemons ⚡️\n\n👍 Gentle\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Defense\n👉 Stats decrease⬇️ : Defense",
    )

def sassy(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ SASSY Pokemons ⚡️\n\n👍 Sassy\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Defense\n👉 Stats decrease⬇️ : Speed",
    )

def careful(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ CAREFUL Pokemons ⚡️\n\n👍 Careful\n\n👉 Effects :\n👉 Stats increase⬆️  : Sp. Defense\n👉 Stats decrease⬇️ : Sp. Attack",
    )

def hardy(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ HARDY Pokemons ⚡️\n\n👍 Hardy\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

def docile(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ DOCILE Pokemons ⚡️\n\n👍 Docile\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

def serious(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ SERIOUS Pokemons ⚡️\n\n👍 Serious\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

def bashful(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ BASHFUL Pokemons ⚡️\n\n👍 Bashful\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

def quirky(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "⚡️ QUIRKY Pokemons ⚡️\n\n👍 Quirky\n\n👉 Effects :\n👉 Stats increase⬆️  : None\n👉 Stats decrease⬇️ : None",
    )

LONELY_HANDLER = DisableAbleCommandHandler("lonely", lonely, run_async=True)
BRAVE_HANDLER = DisableAbleCommandHandler("brave", brave, run_async=True)
ADAMANT_HANDLER = DisableAbleCommandHandler("adamant", adamant, run_async=True)
NAUGHTY_HANDLER = DisableAbleCommandHandler("naughty", naughty, run_async=True)
BOLD_HANDLER = DisableAbleCommandHandler("bold", bold, run_async=True)
RELAXED_HANDLER = DisableAbleCommandHandler("relaxed", relaxed, run_async=True)
IMPISH_HANDLER = DisableAbleCommandHandler("impish", impish, run_async=True)
LAX_HANDLER = DisableAbleCommandHandler("lax", lax, run_async=True)
TIMID_HANDLER = DisableAbleCommandHandler("timid", timid, run_async=True)
HASTY_HANDLER = DisableAbleCommandHandler("hasty", hasty, run_async=True)
JOLLY_HANDLER = DisableAbleCommandHandler("jolly", jolly, run_async=True)
NAIVE_HANDLER = DisableAbleCommandHandler("naive", naive, run_async=True)
MODEST_HANDLER = DisableAbleCommandHandler("modest", modest, run_async=True)
MILD_HANDLER = DisableAbleCommandHandler("mild", mild, run_async=True)
QUIET_HANDLER = DisableAbleCommandHandler("quiet", quiet, run_async=True)
RASH_HANDLER = DisableAbleCommandHandler("rash", rash, run_async=True)
CALM_HANDLER = DisableAbleCommandHandler("calm", calm, run_async=True)
GENTLE_HANDLER = DisableAbleCommandHandler("gentle", gentle, run_async=True)
SASSY_HANDLER = DisableAbleCommandHandler("sassy", sassy, run_async=True)
CAREFUL_HANDLER = DisableAbleCommandHandler("careful", careful, run_async=True)
HARDY_HANDLER = DisableAbleCommandHandler("hardy", hardy, run_async=True)
DOCILE_HANDLER = DisableAbleCommandHandler("docile", docile, run_async=True)
SERIOUS_HANDLER = DisableAbleCommandHandler("serious", serious, run_async=True)
BASHFUL_HANDLER = DisableAbleCommandHandler("bashful", bashful, run_async=True)
QUIRKY_HANDLER = DisableAbleCommandHandler("quirky", quirky, run_async=True)

dispatcher.add_handler(LONELY_HANDLER)
dispatcher.add_handler(BRAVE_HANDLER)
dispatcher.add_handler(ADAMANT_HANDLER)
dispatcher.add_handler(NAUGHTY_HANDLER)
dispatcher.add_handler(BOLD_HANDLER)
dispatcher.add_handler(RELAXED_HANDLER)
dispatcher.add_handler(IMPISH_HANDLER)
dispatcher.add_handler(LAX_HANDLER)
dispatcher.add_handler(TIMID_HANDLER)
dispatcher.add_handler(HASTY_HANDLER)
dispatcher.add_handler(JOLLY_HANDLER)
dispatcher.add_handler(NAIVE_HANDLER)
dispatcher.add_handler(MODEST_HANDLER)
dispatcher.add_handler(MILD_HANDLER)
dispatcher.add_handler(QUIET_HANDLER)
dispatcher.add_handler(RASH_HANDLER)
dispatcher.add_handler(CALM_HANDLER)
dispatcher.add_handler(GENTLE_HANDLER)
dispatcher.add_handler(SASSY_HANDLER)
dispatcher.add_handler(CAREFUL_HANDLER)
dispatcher.add_handler(HARDY_HANDLER)
dispatcher.add_handler(DOCILE_HANDLER)
dispatcher.add_handler(SERIOUS_HANDLER)
dispatcher.add_handler(BASHFUL_HANDLER)
dispatcher.add_handler(QUIRKY_HANDLER)
