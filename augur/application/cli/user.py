'''
Augur commands for adding regular users or administrative users
Running the script:
Add Regular user command: augur user add <username> <email> <firstname> <lastname>
Add Admin command: augur user add <username> <email> <firstname> <lastname> --admin 
'''

import os
import click
import logging
from werkzeug.security import generate_password_hash
from augur.application.db.models import User
from augur.application.db.engine import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

logger = logging.getLogger(__name__)

#user subcommand
@click.group('user', short_help='Support for adding regular users or administrative users')
def cli():
    pass
@cli.command('add', short_help="Add a new user")
@click.argument("username")
@click.argument("email")
@click.argument("firstname")
@click.argument("lastname")
@click.option(
    "--phone-number", default=None, help="User phone number"
)
@click.option(
   "--admin", is_flag=True, default=False, help="New user has administrator role"
)
@click.password_option(help="Set password")
def add_user(username, email, firstname, lastname, admin, phone_number, password):
    """Add a new user to the database with email address = EMAIL."""

    session = Session()

    if session.query(User).filter(User.login_name == username).first() is not None:
        return click.echo("username already taken")

    if session.query(User).filter(User.email == email).first() is not None:
        return click.echo("email already signed-up")

    user = session.query(User).filter(User.login_name == username).first()
    if not user:
        password = generate_password_hash(password)
        new_user = User(login_name=username, login_hashword=password, email=email, text_phone=phone_number, first_name=firstname, last_name=lastname, admin=admin, tool_source="User CLI", tool_version=None, data_source="CLI")
        session.add(new_user)
        session.commit()
        user_type = "admin user" if admin else "user"
        message = f"Successfully added new: {username}"
        click.secho(message, bold=True)
        return 0