from flask import Flask
from flask_migrate import Migrate
from veiws import main_views, question_views, answer_views, auth_views
import config
from models import db
app = Flask(__name__)
migrate = Migrate()
app.config.from_object(config)
#ORM
db.init_app(app)
migrate.init_app(app, db)
import models

HOST = "localhost"
PORT = 27710
app.register_blueprint(question_views.bp)
app.register_blueprint(main_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)

# 필터
from filter import format_datetime
app.jinja_env.filters['datetime'] = format_datetime

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
