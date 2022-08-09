import logging
import logging.handlers
import os

from bot import Bot
from feed import MeuTimao

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    token = os.getenv('TOKEN_BOT')
except KeyError:
    token = "Token not available!"
    logger.info("Token not available!")
    raise
    
if __name__ == '__main__':
    mt = MeuTimao()
    bot = Bot(token)
    n = mt.last_new()

    if n:
        bot.sendPhoto(
            chat_id=1305481132,
            photo=n.media_thumbnail,
            caption=f'<b>{n.title}\n\n{n.content}</b>'
        )
        logger.info(f'UMA NOVA NOTICIA FOI ENVIADA ID({n.id_noticia})')        
    else:
        logger.info(f'SEM NOTICIA NOVA')
