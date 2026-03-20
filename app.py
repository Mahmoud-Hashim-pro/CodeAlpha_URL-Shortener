from flask import Flask
from routes.url_routes import url_bp
from database.db import init_db

app = Flask(__name__)

init_db()

app.register_blueprint(url_bp)

if __name__ == '__main__':
    app.run(debug=True)