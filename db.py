import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext

connection = None

def get_db():
  global connection
  if connection is None:
    if 'db' not in g:
        connection = g.db = psycopg2.connect(
          dbname=current_app.config['POSTGRESQL_DATABASE'], 
          user=current_app.config['POSTGRESQL_USER'], 
          password=current_app.config['POSTGRESQL_PASSWORD'], 
          host=current_app.config['POSTGRESQL_HOST'])
  return connection


def close_db(e=None):
    global connection
    db = g.pop('db', None)

    if db is not None:
        db.close()
    connection = None

def init_db():
    # Alembic or Flask-Script would be better
    db = get_db()
    db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    with current_app.open_resource('migrations/0001_schema.sql') as f:
      with db.cursor() as cur:
        cur.execute(f.read().decode('utf8'))
    db.set_session(autocommit=False)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)