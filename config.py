import os

class Config(object):
    APP_ID = int(os.environ['APP_ID'])
    API_HASH = os.environ['API_HASH']
    BOT_TOKEN = os.environ['BOT_TOKEN']
    OWNER_ID = int(os.environ['OWNER_ID'])
