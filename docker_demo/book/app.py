from flask import Flask
from route import books_blueprint
from model import db, init_app
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abhvfflsuvla'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Alam\\Desktop\\docker_demo\\book\\database\\book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(books_blueprint)
init_app(app)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5002)
