from flask import Flask

# ROUTES
from src.routes import blueprint_routs

app = Flask(__name__)


if __name__ == '__main__':
    #BLUEPRINTS
    app.register_blueprint(blueprint_routs.main, url_prefix='/api')

    app.run(debug=True,port=4400)
