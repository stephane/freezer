import subprocess

from flask.ext.script import Manager, Server

from .app import app
from .frozen import freezer

manager = Manager(app, with_default_commands=False)
manager.add_command('run', Server())


@manager.command
def freeze(serve=False):
    """Freezes the static version of the website."""
    if serve:
        freezer.run(debug=True)
    else:
        urls = freezer.freeze()
        print("Built %i files." % len(urls))


@manager.command
def push(destination=app.config['RSYNC_DESTINATION']):
    """Freezes and uploads the website."""
    print("### Freezing")
    freeze()
    print("### Uploading to", destination)
    subprocess.call(
        ['rsync', '-Pah', '--delete', freezer.root + '/', destination])


if __name__ == '__main__':
    manager.run()
