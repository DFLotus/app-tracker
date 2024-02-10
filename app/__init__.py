import os
from flask import Flask
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from db_Config import connect_to_db
from routes import hello


# To run the application type in following command:  flask --app app  run --debug
def create_app(test_config=None) -> Flask:
    # create and configure the app
    app: Flask = Flask(__name__, instance_relative_config=True)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # Register routes
    app.register_blueprint(hello.helloWorld)

    app.db_conn = connect_to_db() # establish data base connection

    # When connection is closed the application is terminated
    @app.teardown_appcontext
    def teardown_db(exception=None):
        if hasattr(app, "db_conn"):
            app.db_conn.close()

    return app
