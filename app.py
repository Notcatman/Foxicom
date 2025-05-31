from flask import Flask, render_template
from flask_login import login_required, LoginManager, current_user
from flask_migrate import Migrate
from models import db, User
from login import log
from routes import routes


app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "log.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(log)
app.register_blueprint(routes)



if __name__ == "__main__":
    app.run(debug=True, port=4444)
