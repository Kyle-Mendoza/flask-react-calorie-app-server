from flask import Flask 
from flask.cli import with_appcontext

import click 
from app.extensions import db
from app.models.admin import Admin 

@click.command("seed")
@with_appcontext
def seed():

    # Create the database and tables if they don't exist
    click.echo("Creating database and tables...")
    db.create_all()

    if not Admin.query.filter_by(username="admin").first():
        admin = Admin(username="admin")
        admin.set_password("password")
        db.session.add(admin)
        db.session.commit() 

        click.echo("Admin user created successfully!")
    else:
        click.echo("Admin user already exists.")

