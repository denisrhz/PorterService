from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Admin #
from app.models import Message, City, Service
admin = Admin(app)
admin.add_view(ModelView(Message, db.session))
admin.add_view(ModelView(Service, db.session))
admin.add_view(ModelView(City, db.session))

from app import routes, models