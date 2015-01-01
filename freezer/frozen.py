import os
import mimetypes

from flask.ext.frozen import Freezer, walk_directory

from .app import app
from .models import Article

# Seems to be available only on some systems...
mimetypes.add_type('application/atom+xml', '.atom')

freezer = Freezer(app)

@freezer.register_generator
def static_in_posts():
    root_path = os.path.join(app.root_path, 'articles')
    for year in Article.get_years():
        for name in os.listdir(os.path.join(root_path, year)):
            directory = os.path.join(root_path, year, name)
            if os.path.isdir(directory):
                for path in walk_directory(directory):
                    yield {'year': int(year), 'name': name, 'path': path}

@freezer.register_generator
def archives():
    for year in Article.get_years():
        yield {'year': int(year)}
