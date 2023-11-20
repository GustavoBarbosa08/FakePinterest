from flask import Flask, render_template, url_for
from  flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt  import Bcrypt
 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "0754fae0d445f39134e5b79ee8ef0209"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_maneger = LoginManager(app)
login_maneger.login_view = "homepage"


from fakePinterest import routes