from flask import Flask, render_template
from routes.home import home_route
from routes.cliente import cliente_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix="/clientes")

if __name__ == '__main__':
    app.run(debug=True)
