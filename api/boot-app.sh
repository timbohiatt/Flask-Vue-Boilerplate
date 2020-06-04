#!/bin/bash
set -o allexport; source .env; set +o allexport

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# If DB is up and running in environment dev the whole DB is rebuit every time you boot the server.
if [[ $APP_ENV == "dev" ]]; then
    #Clean up all DB Version and migrarion information.
    rm -r migrations
    rm *.db
    #Destroy DB with Flask CLI Command for Complete Local Rebuild.
    flask db-destroy
    flask db init
    flask db migrate
fi

while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

#Kick off all Unit Tests as Part of Build
flask run-unit-tests
#Kick off the Server.
exec gunicorn -b :$APP_PORT --access-logfile - --error-logfile - app:app