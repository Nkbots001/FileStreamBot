from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", "24980957"))
    API_HASH = env.get("TELEGRAM_API_HASH", "eb547148c7c563c66afe0ebad929ad40")
    OWNER_ID = int(env.get("OWNER_ID", "7803722624"))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "7803722624").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Filetolink_a6_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7637667505:AAEV3Jve21aXLngVmemDzJRHzsp2sOy8cII")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", "-1002300036761"))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 24))

class Server:
    BASE_URL = env.get("BASE_URL", "http://127.0.0.1:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
