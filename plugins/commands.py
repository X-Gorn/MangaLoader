import os, shutil
from pyrogram import Client, filters
from pyrogram.types.bots_and_keyboards import InlineKeyboardMarkup
from translation import Translation


@Client.on_message(filters.private & filters.command('start'))
def _start(bot, update):
    update.reply_text(
        Translation.START_TEXT.format(str(update.from_user.first_name)), reply_markup=InlineKeyboardMarkup(Translation.start_buttons)
    )


@Client.on_message(filters.private & filters.command('help'))
def _help(bot, update):
    update.reply_text(Translation.HELP_TEXT)


@Client.on_message(filters.private & filters.command('cleandir'))
def _cleandir(bot, update):
    dirx = './Manga/'
    if os.path.isdir(dirx):
        shutil.rmtree(dirx)
        update.reply_text(Translation.CLEANDIR_SUCCESS)
    else:
        update.reply_text(Translation.CLEANDIR_UNSUCCESS)
