import datetime

from flask import Flask
import jinja2

app = Flask(__name__)
app.config.from_object('freezer.config')
app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.globals['today'] = datetime.date.today

from . import views
