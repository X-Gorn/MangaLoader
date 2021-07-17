from pyrogram import Client
from config import Config


xbot = Client(
	"MangaLoader",
	api_id=Config.APP_ID,
	api_hash=Config.API_HASH,
	bot_token=Config.BOT_TOKEN,
	plugins=dict(root="plugins"),
)

xbot.run()
