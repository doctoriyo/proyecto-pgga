import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import json
from HuidaFoco import *


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        #self.write("This is your response")
        #self.finish()
        self.render("index.html")

class WSHandler(tornado.websocket.WebSocketHandler):
    connections = set()

    def open(self):
        self.connections.add(self)
        print('New connection was opened')
        self.write_message("Conn!")

    def on_message(self, message):
        # print(message)
        print(type(message))
        json_string = u'%s' %(message,)
        print(json_string)
        # json_string = u'{ "id":"123456789"}'
        print(json_string)
        mensajedeJS = json.loads(json_string)
        print(type(mensajedeJS))
        # obj = json.loads(json_string)
        # print(type(obj))
        message = mensajedeJS['msg']

        print('received message: %s\n' %message)

        if mensajedeJS['msg'] == "valor":
            print("*"*20)

        #loquemandare = myfuncion_calcula(mensajedeJS["msg"])


        #print(self.connections)
        #for elem in self.connections:
        #    elem.write_message({"msg": message + ' a todos'}, binary=False)

        # [con.write_message('Hi!') for con in self.connections]



        midict = {"msg": message + ' al que lo manda', "posicionesx": matrizposicionx, "posicionesy": matrizposiciony}


        self.write_message(midict)

    def on_close(self):
        print('connection closed\n')



application = tornado.web.Application([(r'/', IndexHandler),(r'/ws', WSHandler),])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()