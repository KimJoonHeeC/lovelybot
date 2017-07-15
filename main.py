__metaclass__ = type

from microsoftbotframework import MsBot
from tasks import *
import os

bot = MsBot(port=int(os.environ['PORT']))
#bot.add_process(echo_response)
#bot.add_process(djn_response)
bot.add_process(djn_echo)
bot.run()