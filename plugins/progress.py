from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from translation import Translation
from config import Config
from helper_funcs.help import check_url


@Client.on_message(filters.private & filters.text)
def download(bot, update):
    if update.from_user.id != Config.OWNER_ID:
        return
    url = update.text
    if check_url(url):
        pass
    else:
        return
    update.reply_text(Translation.UPLOAD, quote=True, reply_markup=InlineKeyboardMarkup(Translation.upload_buttons))
