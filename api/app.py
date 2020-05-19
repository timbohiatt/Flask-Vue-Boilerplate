'''
    Boot Call for App Runner.
    Descritpion: Called by the boot-app.sh Script and Runs Core Application.
'''
from api import create_app, db, cli, celery
app = create_app()
app.app_context().push()
cli.register(app)
