import cherrypy
import marbaloo_telegram
import os
from cherrypy.test import helper


class CPTest(helper.CPWebCase):

    def setup_server():
        root_path = os.path.dirname(__file__)
        token = open(os.path.join(root_path, '.token.txt'), 'r').read()
        marbaloo_telegram.Plugin(cherrypy.engine, token).subscribe()
        cherrypy.tools.telegram = marbaloo_telegram.Tool()

        class Root(object):
            @cherrypy.expose
            def simple(self):
                bot = cherrypy.request.telegram_dp.bot
                message = bot.sendMessage(text='TestMessage!', chat_id='38855883')
                return message.text

        cherrypy.tree.mount(Root(), '/', {
                                '/': {
                                    'tools.telegram.on': True
                                }
                            })

    setup_server = staticmethod(setup_server)

    def test_simple(self):
        self.getPage("/simple")
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'text/html;charset=utf-8')
        self.assertBody('TestMessage!')
