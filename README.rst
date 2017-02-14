Telegram Bot for Cherrypy
=========================

`python-telegram-bot <https://python-telegram-bot.org/>`_ support for cherrypy.

Installation
------------
::

    pip install marbaloo_telegram

Usage
-----
For the simple way you can just send anything supported by `python-telegram-bot <https://python-telegram-bot.org/>`_,

::

    # app.py
    import marbaloo_telegram
    import cherrypy

    marbaloo_telegram.Plugin(cherrypy.engine, 'TOKEN').subscribe()
    cherrypy.tools.telegram = marbaloo_telegram.Tool()


    class Root(object):
        @cherrypy.expose
        def index(self):
            bot = cherrypy.request.telegram_dp.bot
            message = bot.sendMessage(text='TestMessage!', chat_id='38855883')
            return  message.text

    root_path = os.path.dirname(__file__)
    cherrypy.quickstart(Root(), '/', {
                                '/': {
                                    'tools.telegram.on': True,
                                }
                            })

But if you want to use more interactive interface,
you can get bot dispatcher from plugin and define your telegram controller after ``cherrypy.engine.start``,
