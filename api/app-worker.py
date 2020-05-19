'''
    Boot Call for Celery Worker.
    Descritpion: Called by the boot-celery.sh Script and Runs Celery Worker.
'''
from api import create_app, db, cli, celery
app = create_app()
app.app_context().push()
cli.register(app)
