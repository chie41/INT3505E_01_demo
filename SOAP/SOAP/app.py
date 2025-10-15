from flask import Flask, request, Response
from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Định nghĩa SOAP service
class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Unicode)
    def say_hello(ctx, name, times):
        return f"Hello {name}! " * times

# Tạo ứng dụng SOAP
soap_app = Application(
    [HelloWorldService],
    'spyne.examples.hello.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)

# Kết hợp với Flask
flask_app = Flask(__name__)

@flask_app.route("/soap", methods=["POST"])
def soap_service():
    response = wsgi_app(request.environ, start_response)
    return Response(response, mimetype="text/xml")

def start_response(status, response_headers, exc_info=None):
    return lambda data: None

if __name__ == "__main__":
    flask_app.run(host="127.0.0.1", port=5000, debug=True)
