import html
import random
import time

from zerotwobot import dispatcher
from zerotwobot.modules.disable import DisableAbleCommandHandler
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

def mewtwo(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal - Timid, modest")
    reply_text(r"Best Y  -  Timid, hasty")
    reply_text(r"Best X - Naive and jolly")
    
def mew(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Timid, modest")
    
def tyranitar(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Adamant, brave")
    
def sharpedo(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Jolly, adamant")
    
def articuno(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Careful")
    
def tapu(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Koko - Jolly, naive, adamant      For Bulu- Adamant, impish      For Lele- Timid, modest      For Fini- Modest, calm, bold")
    
def zapdos(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Modest")
    
def moltres(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Modest")
    
def celebi(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Modest, Quiet")
    
def hooh(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Careful, adamant")
    
def lugia(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Adamant")
    
def raikou(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Timid")
    
def entei(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, careful, jolly, impish")
    
def suicune(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Careful")
    
def jirachi(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")
    
def kyogre(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm")
    
def groudon(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, impish")
    
def rayquaza(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, jolly")
    
def mamoswine(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")
    
def melloetta(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal- Modest, calm       For Pirouette form - Jolly, hasty, naive, adamant")
    
def deoxys(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal - Timid, modest      For Attack - Naive, hasty, timid, jolly      Speed - Naive, hasty, timid, modest      Defence - Relaxed, sassy")
    
def regirock(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Relaxed")
    
def registeel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Relaxed, sassy")
    
def regice(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Calm, careful")
    
def latias(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Calm, modest, timid")
    
def latios(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Calm, modest")
    
def arceus(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")
    
def guzzlord(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")
    
def buzzwole(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, impish")
    
def kommoo(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, impish, careful, jolly")
    
def dialga(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")
    
def bulbasaur(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm, bold")
    
def ivysaur(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm, bold")

def venusaur(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm, bold")

def charmander(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, hasty, timid ")
    reply_text(r"Jolly and naive also good if u get CHARIZARD X stone")

def charmeleon(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, hasty, timid ")
    reply_text(r"Jolly and naive also good if u get CHARIZARD X stone")
    
def charizard(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal - Modest, hasty, timid")
    reply_text(r"Best For X  - Jolly, naive")
    reply_text(r"Best For Y  - Modest, hasty, timid")

def squirtle(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm")

def wartortle(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm")

def blastoise(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm")

def caterpie(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")
    reply_text(r"NOT WORTH CATCHING . RIP POKEMON")

def metapod(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")
    reply_text(r"NOT WORTH CATCHING . RIP POKEMON")

def butterfree(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")
    reply_text(r"NOT WORTH CATCHING . RIP POKEMON")

def weedle(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, hasty, naive")

def kakuna(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, hasty, naive")

def beedrill(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, hasty, naive")

def pidgey(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly")

def pidgeotto(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly")

def pidgeot(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly")

def rattata(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, adamant")

def raticate(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, adamant")

def spearow(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, jolly")

def fearow(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, jolly")

def ekans(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, adamant")

def arbok(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly,adamant")

def pikachu(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")

def raichu(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")

def sandshrew(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def sandslash(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def nidoran(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best (m)- Adamant, impish")
    reply_text(r"Best (f)- Adamant")

def nidorina(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Adamant")

def nidoqueen(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Adamant")

def nidorino(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Adamant, impish")

def nidoking(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Adamant, impish")

def clefairy(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def clefable(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def vulpix(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Alolan- Timid, modest")

def ninetales(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Alolan- Timid, modest")

def jigglypuff(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def wigglytuff(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def zubat(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, naive, hasty")

def golbat(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, naive, hasty")

def oddish(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- gay")

def gloom(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- gay")

def vileplume(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- gay")

def paras(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- gay")

def parasect(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- gay")

def venonat(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def venomoth(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def diglett(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def dugtrio(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def meowth(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly")

def persian(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly")

def psyduck(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def golduck(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def mankey(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def primeape(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def growlithe(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, hasty, naive")

def arcanine(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, hasty, naive")

def poliwag(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def poliwhirl(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def poliwrath(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def abra(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty, naive")

def kadabra(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty, naive")

def alakazam(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty, naive")

def machop(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def machoke(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def machamp(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def bellsprout(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, adamant")

def weepinbell(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, adamant")

def victreebel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, adamant")

def tentacool(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid")

def tentacruel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid")

def geodude(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, impish")

def graveler(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, impish")

def golem(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal and alolan- Adamant, impish")

def ponyta(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")

def rapidash(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")

def slowpoke(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm")

def slowbro(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm")

def magnemite(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def magneton(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def farfetchd(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def doduo(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, jolly")

def dodrio(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, jolly")

def seel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"gey")

def dewgong(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"gey")

def grimer(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Alolan- Adamant, sassy, brave, careful")

def muk(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Alolan- Adamant, sassy, brave, careful")

def shellder(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Relaxed, sassy")

def cloyster(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Relaxed, sassy")

def gastly(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty")

def haunter(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty")

def gengar(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty")

def onix(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def drowzee(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def hypno(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def krabby(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def kingler(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def voltorb(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty, naive")
    
def fp(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"God of Gay")
    reply_text(r"Legendary gay")
    reply_text(r"Gay of all time")
    reply_text(r"Gay af")
    reply_text(r"Woh to gay h")
    reply_text(r"huh bahut bol liya ... dil par mat lena")
    
MEWTWO_HANDLER = DisableAbleCommandHandler("mewtwo", mewtwo, run_async=True)
MEW_HANDLER = DisableAbleCommandHandler("mew", mew, run_async=True)
TYRANITAR_HANDLER = DisableAbleCommandHandler("tyranitar", tyranitar, run_async=True)
SHARPEDO_HANDLER = DisableAbleCommandHandler("sharpedo", sharpedo, run_async=True)
ARTICUNO_HANDLER = DisableAbleCommandHandler("articuno", articuno, run_async=True)
TAPU_HANDLER = DisableAbleCommandHandler("tapu", tapu, run_async=True)
ZAPADOS_HANDLER = DisableAbleCommandHandler("zapdos", zapdos, run_async=True)
MOLTRES_HANDLER = DisableAbleCommandHandler("moltres", moltres, run_async=True)
CELEBI_HANDLER = DisableAbleCommandHandler("celebi", celebi, run_async=True)
HOOH_HANDLER = DisableAbleCommandHandler("hooh", hooh, run_async=True)
LUGIA_HANDLER = DisableAbleCommandHandler("lugia", lugia, run_async=True)
RAIKOU_HANDLER = DisableAbleCommandHandler("raikou", raikou, run_async=True)
ENTEI_HANDLER = DisableAbleCommandHandler("entei", entei, run_async=True)
SUICUNE_HANDLER = DisableAbleCommandHandler("suicune", suicune, run_async=True)
JIRACHI_HANDLER = DisableAbleCommandHandler("jirachi", jirachi, run_async=True)
KYOGRE_HANDLER = DisableAbleCommandHandler("kyogre", kyogre, run_async=True)
GROUDON_HANDLER = DisableAbleCommandHandler("groudon", groudon, run_async=True)
RAYQUAZA_HANDLER = DisableAbleCommandHandler("rayquaza", rayquaza, run_async=True)
MAMOSWINE_HANDLER = DisableAbleCommandHandler("mamoswine", mamoswine, run_async=True)
MELLOETTA_HANDLER = DisableAbleCommandHandler("melloetta", melloetta, run_async=True)
DEOXYS_HANDLER = DisableAbleCommandHandler("deoxys", deoxys, run_async=True)
REGIROCK_HANDLER = DisableAbleCommandHandler("regirock", regirock, run_async=True)
REGISTEEL_HANDLER = DisableAbleCommandHandler("registeel", registeel, run_async=True)
REGICE_HANDLER = DisableAbleCommandHandler("regice", regice, run_async=True)
LATIAS_HANDLER = DisableAbleCommandHandler("latias", latias, run_async=True)
LATIOS_HANDLER = DisableAbleCommandHandler("latios", latios, run_async=True)
ARCEUS_HANDLER = DisableAbleCommandHandler("arceus", arceus, run_async=True)
GUZZLORD_HANDLER = DisableAbleCommandHandler("guzzlord", guzzlord, run_async=True)
BUZZWOLE_HANDLER = DisableAbleCommandHandler("buzzwole", buzzwole, run_async=True)
KOMMO_HANDLER = DisableAbleCommandHandler("kommoo", kommoo, run_async=True)
DIALGA_HANDLER = DisableAbleCommandHandler("dialga", dialga, run_async=True)
BULBASAUR_HANDLER = DisableAbleCommandHandler("bulbasaur", bulbasaur, run_async=True)
IVYSAUR_HANDLER = DisableAbleCommandHandler("ivysaur", ivysaur, run_async=True)
VENUSAUR_HANDLER = DisableAbleCommandHandler("venusaur", venusaur, run_async=True)
CHARMANDER_HANDLER = DisableAbleCommandHandler("charmander", charmander, run_async=True)
CHARMELEON_HANDLER = DisableAbleCommandHandler("charmeleon", charmeleon, run_async=True)
CHARIZARD_HANDLER = DisableAbleCommandHandler("charizard", charizard, run_async=True)
SQUIRTLE_HANDLER = DisableAbleCommandHandler("squirtle", squirtle, run_async=True)
WARTORTLE_HANDLER = DisableAbleCommandHandler("wartortle", wartortle, run_async=True)
BLASTOISE_HANDLER = DisableAbleCommandHandler("blastoise", blastoise, run_async=True)
CATERPIE_HANDLER = DisableAbleCommandHandler("caterpie", caterpie, run_async=True)
METAPOD_HANDLER = DisableAbleCommandHandler("metapod", metapod, run_async=True)
BUTTERFREE_HANDLER = DisableAbleCommandHandler("butterfree", butterfree, run_async=True)
WEEDLE_HANDLER = DisableAbleCommandHandler("weedle", weedle, run_async=True)
KAKUNA_HANDLER = DisableAbleCommandHandler("kakuna", kakuna, run_async=True)
BEEDRILL_HANDLER = DisableAbleCommandHandler("beedrill", beedrill, run_async=True)
PIDGEY_HANDLER = DisableAbleCommandHandler("pidgey", pidgey, run_async=True)
PIDGEOTTO_HANDLER = DisableAbleCommandHandler("pidgeotto", pidgeotto, run_async=True)
PIDGEOT_HANDLER = DisableAbleCommandHandler("pidgeot", pidgeot, run_async=True)
RATTATA_HANDLER = DisableAbleCommandHandler("rattata", rattata, run_async=True)
RATICATE_HANDLER = DisableAbleCommandHandler("raticate", raticate, run_async=True)
SPEAROW_HANDLER = DisableAbleCommandHandler("spearow", spearow, run_async=True)
FEAROW_HANDLER = DisableAbleCommandHandler("fearow", fearow, run_async=True)
EKANS_HANDLER = DisableAbleCommandHandler("ekans", ekans, run_async=True)
ARBOK_HANDLER = DisableAbleCommandHandler("arbok", arbok, run_async=True)
PIKACHU_HANDLER = DisableAbleCommandHandler("pikachu", pikachu, run_async=True)
RAICHU_HANDLER = DisableAbleCommandHandler("raichu", raichu, run_async=True)
SANDSHREW_HANDLER = DisableAbleCommandHandler("sandshrew", sandshrew, run_async=True)
SANDSLASH_HANDLER = DisableAbleCommandHandler("sandslash", sandslash, run_async=True)
NIDORAN_HANDLER = DisableAbleCommandHandler("nidoran", nidoran, run_async=True)
NIDORINA_HANDLER = DisableAbleCommandHandler("nidorina", nidorina, run_async=True)
NIDOQUEEN_HANDLER = DisableAbleCommandHandler("nidoqueen", nidoqueen, run_async=True)
NIDORINO_HANDLER = DisableAbleCommandHandler("nidorino", nidorino, run_async=True)
NIDOKING_HANDLER = DisableAbleCommandHandler("nidoking", nidoking, run_async=True)
CLEFAIRY_HANDLER = DisableAbleCommandHandler("clefairy", clefairy, run_async=True)
CLEFABLE_HANDLER = DisableAbleCommandHandler("clefable", clefable, run_async=True)
VULPIX_HANDLER = DisableAbleCommandHandler("vulpix", vulpix, run_async=True)
NINETALES_HANDLER = DisableAbleCommandHandler("ninetales", ninetales, run_async=True)
JIGGLYPUFF_HANDLER = DisableAbleCommandHandler("jigglypuff", jigglypuff, run_async=True)
WIGGLYTUFF_HANDLER = DisableAbleCommandHandler("wigglytuff", wigglytuff, run_async=True)
ZUBAT_HANDLER = DisableAbleCommandHandler("zubat", zubat, run_async=True)
GOLBAT_HANDLER = DisableAbleCommandHandler("golbat", golbat, run_async=True)
ODDISH_HANDLER = DisableAbleCommandHandler("oddish", oddish, run_async=True)
GLOOM_HANDLER = DisableAbleCommandHandler("gloom", gloom, run_async=True)
VILEPLUME_HANDLER = DisableAbleCommandHandler("vileplume", vileplume, run_async=True)
PARAS_HANDLER = DisableAbleCommandHandler("paras", paras, run_async=True)
PARASECT_HANDLER = DisableAbleCommandHandler("parasect", parasect, run_async=True)
VENONAT_HANDLER = DisableAbleCommandHandler("venonat", venonat, run_async=True)
VENOMOTH_HANDLER = DisableAbleCommandHandler("venomoth", venomoth, run_async=True)
DIGLETT_HANDLER = DisableAbleCommandHandler("diglett", diglett, run_async=True)
DUGTRIO_HANDLER = DisableAbleCommandHandler("dugtrio", dugtrio, run_async=True)
MEOWTH_HANDLER = DisableAbleCommandHandler("meowth", meowth, run_async=True)
PERSIAN_HANDLER = DisableAbleCommandHandler("persian", persian, run_async=True)
PSYDUCK_HANDLER = DisableAbleCommandHandler("psyduck", psyduck, run_async=True)
GOLDUCK_HANDLER = DisableAbleCommandHandler("golduck", golduck, run_async=True)
MANKEY_HANDLER = DisableAbleCommandHandler("mankey", mankey, run_async=True)
PRIMEAPE_HANDLER = DisableAbleCommandHandler("primeape", primeape, run_async=True)
GROWLITHE_HANDLER = DisableAbleCommandHandler("growlithe", growlithe, run_async=True)
ARCANINE_HANDLER = DisableAbleCommandHandler("arcanine", arcanine, run_async=True)
POLIWAG_HANDLER = DisableAbleCommandHandler("poliwag", poliwag, run_async=True)
POLIWHIRL_HANDLER = DisableAbleCommandHandler("poliwhirl", poliwhirl, run_async=True)
POLIWRATH_HANDLER = DisableAbleCommandHandler("poliwrath", poliwrath, run_async=True)
ABRA_HANDLER = DisableAbleCommandHandler("abra", abra, run_async=True)
KADABRA_HANDLER = DisableAbleCommandHandler("kadabra", kadabra, run_async=True)
ALAKAZAM_HANDLER = DisableAbleCommandHandler("alakazam", alakazam, run_async=True)
MACHOP_HANDLER = DisableAbleCommandHandler("machop", machop, run_async=True)
MACHOKE_HANDLER = DisableAbleCommandHandler("machoke", machoke, run_async=True)
MACHAMP_HANDLER = DisableAbleCommandHandler("machamp", machamp, run_async=True)
BELLSPROUT_HANDLER = DisableAbleCommandHandler("bellsprout", bellsprout, run_async=True)
WEEPINBELL_HANDLER = DisableAbleCommandHandler("weepinbell", weepinbell, run_async=True)
VICTREEBEL_HANDLER = DisableAbleCommandHandler("victreebel", victreebel, run_async=True)
TENTACOOL_HANDLER = DisableAbleCommandHandler("tentacool", tentacool, run_async=True)
TENTACRUEL_HANDLER = DisableAbleCommandHandler("tentacruel", tentacruel, run_async=True)
GEODUDE_HANDLER = DisableAbleCommandHandler("geodude", geodude, run_async=True)
GRAVELER_HANDLER = DisableAbleCommandHandler("graveler", graveler, run_async=True)
GOLEM_HANDLER = DisableAbleCommandHandler("golem", golem, run_async=True)
PONYTA_HANDLER = DisableAbleCommandHandler("ponyta", ponyta, run_async=True)
RAPIDASH_HANDLER = DisableAbleCommandHandler("rapidash", rapidash, run_async=True)
SLOWPOKE_HANDLER = DisableAbleCommandHandler("slowpoke", slowpoke, run_async=True)
SLOWBRO_HANDLER = DisableAbleCommandHandler("slowbro", slowbro, run_async=True)
MAGNEMITE_HANDLER = DisableAbleCommandHandler("magnemite", magnemite, run_async=True)
MAGNETON_HANDLER = DisableAbleCommandHandler("magneton", magneton, run_async=True)
FARFETCHD_HANDLER = DisableAbleCommandHandler("farfetchd", farfetchd, run_async=True)
DODUO_HANDLER = DisableAbleCommandHandler("doduo", doduo, run_async=True)
DODRIO_HANDLER = DisableAbleCommandHandler("dodrio", dodrio, run_async=True)
SEEL_HANDLER = DisableAbleCommandHandler("seel", seel, run_async=True)
DEWGONG_HANDLER = DisableAbleCommandHandler("dewgong", dewgong, run_async=True)
GRIMER_HANDLER = DisableAbleCommandHandler("grimer", grimer, run_async=True)
MUK_HANDLER = DisableAbleCommandHandler("muk", muk, run_async=True)
SHELLDER_HANDLER = DisableAbleCommandHandler("shellder", shellder, run_async=True)
CLOYSTER_HANDLER = DisableAbleCommandHandler("cloyster", cloyster, run_async=True)
GASTLY_HANDLER = DisableAbleCommandHandler("gastly", gastly, run_async=True)
HAUNTER_HANDLER = DisableAbleCommandHandler("haunter", haunter, run_async=True)
GENGAR_HANDLER = DisableAbleCommandHandler("gengar", gengar, run_async=True)
ONIX_HANDLER = DisableAbleCommandHandler("onix", onix, run_async=True)
DROWZEE_HANDLER = DisableAbleCommandHandler("drowzee", drowzee, run_async=True)
HYPNO_HANDLER = DisableAbleCommandHandler("hypno", hypno, run_async=True)
KRABBY_HANDLER = DisableAbleCommandHandler("krabby", krabby, run_async=True)
KINGLER_HANDLER = DisableAbleCommandHandler("kingler", kingler, run_async=True)
VOLTORB_HANDLER = DisableAbleCommandHandler("voltorb", voltorb, run_async=True)
FP_HANDLER = DisableAbleCommandHandler("fp", fp, run_async=True)

dispatcher.add_handler(MEWTWO_HANDLER)
dispatcher.add_handler(MEW_HANDLER)
dispatcher.add_handler(TYRANITAR_HANDLER)
dispatcher.add_handler(SHARPEDO_HANDLER)
dispatcher.add_handler(ARTICUNO_HANDLER)
dispatcher.add_handler(TAPU_HANDLER)
dispatcher.add_handler(ZAPADOS_HANDLER)
dispatcher.add_handler(MOLTRES_HANDLER)
dispatcher.add_handler(CELEBI_HANDLER)
dispatcher.add_handler(HOOH_HANDLER)
dispatcher.add_handler(LUGIA_HANDLER)
dispatcher.add_handler(RAIKOU_HANDLER)
dispatcher.add_handler(ENTEI_HANDLER)
dispatcher.add_handler(SUICUNE_HANDLER)
dispatcher.add_handler(JIRACHI_HANDLER)
dispatcher.add_handler(KYOGRE_HANDLER)
dispatcher.add_handler(GROUDON_HANDLER)
dispatcher.add_handler(RAYQUAZA_HANDLER)
dispatcher.add_handler(MAMOSWINE_HANDLER)
dispatcher.add_handler(MELLOETTA_HANDLER)
dispatcher.add_handler(DEOXYS_HANDLER)
dispatcher.add_handler(REGIROCK_HANDLER)
dispatcher.add_handler(REGISTEEL_HANDLER)
dispatcher.add_handler(REGICE_HANDLER)
dispatcher.add_handler(LATIAS_HANDLER)
dispatcher.add_handler(LATIOS_HANDLER)
dispatcher.add_handler(ARCEUS_HANDLER)
dispatcher.add_handler(GUZZLORD_HANDLER)
dispatcher.add_handler(BUZZWOLE_HANDLER)
dispatcher.add_handler(KOMMO_HANDLER)
dispatcher.add_handler(DIALGA_HANDLER)
dispatcher.add_handler(BULBASAUR_HANDLER)
dispatcher.add_handler(IVYSAUR_HANDLER)
dispatcher.add_handler(VENUSAUR_HANDLER)
dispatcher.add_handler(CHARMANDER_HANDLER)
dispatcher.add_handler(CHARMELEON_HANDLER)
dispatcher.add_handler(CHARIZARD_HANDLER)
dispatcher.add_handler(SQUIRTLE_HANDLER)
dispatcher.add_handler(WARTORTLE_HANDLER)
dispatcher.add_handler(BLASTOISE_HANDLER)
dispatcher.add_handler(CATERPIE_HANDLER)
dispatcher.add_handler(METAPOD_HANDLER)
dispatcher.add_handler(BUTTERFREE_HANDLER)
dispatcher.add_handler(WEEDLE_HANDLER)
dispatcher.add_handler(KAKUNA_HANDLER)
dispatcher.add_handler(BEEDRILL_HANDLER)
dispatcher.add_handler(PIDGEY_HANDLER)
dispatcher.add_handler(PIDGEOTTO_HANDLER)
dispatcher.add_handler(PIDGEOT_HANDLER)
dispatcher.add_handler(RATTATA_HANDLER)
dispatcher.add_handler(RATICATE_HANDLER)
dispatcher.add_handler(SPEAROW_HANDLER)
dispatcher.add_handler(FEAROW_HANDLER)
dispatcher.add_handler(EKANS_HANDLER)
dispatcher.add_handler(ARBOK_HANDLER)
dispatcher.add_handler(PIKACHU_HANDLER)
dispatcher.add_handler(RAICHU_HANDLER)
dispatcher.add_handler(SANDSHREW_HANDLER)
dispatcher.add_handler(SANDSLASH_HANDLER)
dispatcher.add_handler(NIDORAN_HANDLER)
dispatcher.add_handler(NIDORINA_HANDLER)
dispatcher.add_handler(NIDOQUEEN_HANDLER)
dispatcher.add_handler(NIDORINO_HANDLER)
dispatcher.add_handler(NIDOKING_HANDLER)
dispatcher.add_handler(CLEFAIRY_HANDLER)
dispatcher.add_handler(CLEFABLE_HANDLER)
dispatcher.add_handler(VULPIX_HANDLER)
dispatcher.add_handler(NINETALES_HANDLER)
dispatcher.add_handler(JIGGLYPUFF_HANDLER)
dispatcher.add_handler(WIGGLYTUFF_HANDLER)
dispatcher.add_handler(ZUBAT_HANDLER)
dispatcher.add_handler(GOLBAT_HANDLER)
dispatcher.add_handler(ODDISH_HANDLER)
dispatcher.add_handler(GLOOM_HANDLER)
dispatcher.add_handler(VILEPLUME_HANDLER)
dispatcher.add_handler(PARAS_HANDLER)
dispatcher.add_handler(PARASECT_HANDLER)
dispatcher.add_handler(VENONAT_HANDLER)
dispatcher.add_handler(VENOMOTH_HANDLER)
dispatcher.add_handler(DIGLETT_HANDLER)
dispatcher.add_handler(DUGTRIO_HANDLER)
dispatcher.add_handler(MEOWTH_HANDLER)
dispatcher.add_handler(PERSIAN_HANDLER)
dispatcher.add_handler(PSYDUCK_HANDLER)
dispatcher.add_handler(GOLDUCK_HANDLER)
dispatcher.add_handler(MANKEY_HANDLER)
dispatcher.add_handler(PRIMEAPE_HANDLER)
dispatcher.add_handler(GROWLITHE_HANDLER)
dispatcher.add_handler(ARCANINE_HANDLER)
dispatcher.add_handler(POLIWAG_HANDLER)
dispatcher.add_handler(POLIWHIRL_HANDLER)
dispatcher.add_handler(POLIWRATH_HANDLER)
dispatcher.add_handler(ABRA_HANDLER)
dispatcher.add_handler(KADABRA_HANDLER)
dispatcher.add_handler(ALAKAZAM_HANDLER)
dispatcher.add_handler(MACHOP_HANDLER)
dispatcher.add_handler(MACHOKE_HANDLER)
dispatcher.add_handler(MACHAMP_HANDLER)
dispatcher.add_handler(BELLSPROUT_HANDLER)
dispatcher.add_handler(WEEPINBELL_HANDLER)
dispatcher.add_handler(VICTREEBEL_HANDLER)
dispatcher.add_handler(TENTACOOL_HANDLER)
dispatcher.add_handler(TENTACRUEL_HANDLER)
dispatcher.add_handler(GEODUDE_HANDLER)
dispatcher.add_handler(GRAVELER_HANDLER)
dispatcher.add_handler(GOLEM_HANDLER)
dispatcher.add_handler(PONYTA_HANDLER)
dispatcher.add_handler(RAPIDASH_HANDLER)
dispatcher.add_handler(SLOWPOKE_HANDLER)
dispatcher.add_handler(SLOWBRO_HANDLER)
dispatcher.add_handler(MAGNEMITE_HANDLER)
dispatcher.add_handler(MAGNETON_HANDLER)
dispatcher.add_handler(FARFETCHD_HANDLER)
dispatcher.add_handler(DODUO_HANDLER)
dispatcher.add_handler(DODRIO_HANDLER)
dispatcher.add_handler(SEEL_HANDLER)
dispatcher.add_handler(DEWGONG_HANDLER)
dispatcher.add_handler(GRIMER_HANDLER)
dispatcher.add_handler(MUK_HANDLER)
dispatcher.add_handler(SHELLDER_HANDLER)
dispatcher.add_handler(CLOYSTER_HANDLER)
dispatcher.add_handler(GASTLY_HANDLER)
dispatcher.add_handler(HAUNTER_HANDLER)
dispatcher.add_handler(GENGAR_HANDLER)
dispatcher.add_handler(ONIX_HANDLER)
dispatcher.add_handler(DROWZEE_HANDLER)
dispatcher.add_handler(HYPNO_HANDLER)
dispatcher.add_handler(KRABBY_HANDLER)
dispatcher.add_handler(KINGLER_HANDLER)
dispatcher.add_handler(VOLTORB_HANDLER)
dispatcher.add_handler(FP_HANDLER)
