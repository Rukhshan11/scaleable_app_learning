import base64

from flask import Flask
from flask.sessions import SecureCookieSessionInterface

from routes import user_blueprint
from flask_migrate import Migrate
from models import User
import models
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jknfjajm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# sqlite:///C:\\Path\\To\\mydatabase.db
# C:\Users\Alam\Desktop\docker_demo\user\database
# 'C:\\Program Files\\Applications\\python_3_8_2\\python38.zip
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Alam\\Desktop\\docker_demo\\user\\database\\user.db'
models.init_app(app)
app.register_blueprint(user_blueprint)
login_manager = LoginManager(app)
migrate = Migrate(app, models.db)

@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        user = models.User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    return None


class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""

    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args, **kwargs)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)