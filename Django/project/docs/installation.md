# Installation

## Requirements

- Python 3.14 (the project environment used for development) or a compatible Python version.
- `pip`.

Django and the image-processing dependency Pillow are pinned in `requirements.txt`.

## Local installation

Run these commands from the directory containing `manage.py` (`project/`):

```zsh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver --insecure
```

Open <http://127.0.0.1:8000/> in a browser. Stop the server with `Ctrl+C`.

The default database is SQLite at `db.sqlite3`. No environment variables, external credentials, or prepopulated database are required. `migrate` creates the database schema from the checked-in migrations. The project can be started with an empty database.

## Why `runserver --insecure` is used

`DEBUG` is `False` so the custom error pages can be viewed. With debug off, `runserver` does not serve CSS and JavaScript unless `--insecure` is passed. The flag only enables Django's development static-file view for this presentation. It does not turn debug back on.

`runserver` is not a production server. On a real host, a web server such as nginx or Apache would serve static files and uploaded images, and Django would handle application requests only. `--insecure`, and the local media route described below, are used here so the presentation can be opened with one command.

## Configuration and security

The default local settings are in `config/settings.py`. The project currently has `DEBUG = False` so the custom 404 page can be viewed locally, and `ALLOWED_HOSTS` includes `*`. If you change the host or port, update the relevant Django settings as needed.

The repository's development `SECRET_KEY` is a placeholder and must not be used for a public production deployment. For deployment, provide a private secret key through environment configuration, set `DEBUG = False`, configure `ALLOWED_HOSTS` for the deployment domain, and configure production media and static-file serving.

## Useful commands

```zsh
python manage.py check
python manage.py showmigrations
python manage.py migrate
```