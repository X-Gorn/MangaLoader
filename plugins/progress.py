from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from translation import Translation
from config import Config
from helper_funcs.help import check_url


@Client.on_message(filters.private & filters.text)
async def download(bot, update):
    if update.from_user.id != Config.OWNER_ID:
        return
    url = update.text
    if check_url(url):
        pass
    else:
        return
    await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.UPLOAD,
            reply_markup=InlineKeyboardMarkup(Translation.upload_buttons),
            reply_to_message_id=update.message_id
        )
