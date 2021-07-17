from pyrogram import Client, filters
from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup
from translation import Translation


@Client.on_message(filters.private & filters.command('start'))
def _start(bot, update):
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(str(update.from_user.first_name)),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                       "Source", url="https://github.com/X-Gorn/MangaLoader"
                   ),
                   InlineKeyboardButton("Project Channel", url="https://t.me/xTeamBots"),
                ],
                [InlineKeyboardButton("Author", url="https://t.me/xgorn")],
            ]
        ),
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.private & filters.command('help'))
def _help(bot, update):
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_to_message_id=update.message_id
    )
