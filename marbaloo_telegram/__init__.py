import cherrypy
from cherrypy.process import plugins
from telegram.ext import Updater


class Plugin(plugins.SimplePlugin):
    def __init__(self, bus, token):
        """
        Get Token and initialize bot updater
        :param bus:
        :param token:
        """
        plugins.SimplePlugin.__init__(self, bus)
        self.token = token
        self.bot_updater = Updater(self.token)
        self.bot_dp = self.bot_updater.dispatcher
        self.bot_updater.start_polling()

    def start(self):
        self.bus.subscribe('telegram-init', self.telegram_init)

    def stop(self):
        self.bus.unsubscribe('telegram-init', self.telegram_init)
        self.bot_updater.stop()

    def telegram_init(self):
        return self


class Tool(cherrypy.Tool):
    def __init__(self):
        cherrypy.Tool.__init__(self, 'on_start_resource',
                               self.set_telegram_tool,
                               priority=20)

    def _setup(self):
        cherrypy.Tool._setup(self)

    @staticmethod
    def set_telegram_tool():
        bot = cherrypy.engine.publish('telegram-init').pop()
        cherrypy.request.telegram_dp = bot.bot_dp
        cherrypy.request.telegram_updater = bot.bot_updater
