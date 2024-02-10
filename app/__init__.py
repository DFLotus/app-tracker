import os
from flask import Flask
import psycopg2
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from db_Config import connect_to_db


# To run the application flask --app app  run --debug
def create_app(test_config=None) -> Flask:
    # create and configure the app
    app: Flask = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.db_conn = connect_to_db()

    # When connection is closed the application is terminated
    @app.teardown_appcontext
    def teardown_db(exception=None):
        if hasattr(app, "db_conn"):
            app.db_conn.close()

    return app
