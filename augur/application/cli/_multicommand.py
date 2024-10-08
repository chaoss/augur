#SPDX-License-Identifier: MIT
"""
Runs Augur with Gunicorn when called
"""

import os
import click
import importlib
import traceback

from pathlib import Path
# import augur.application

CONTEXT_SETTINGS = dict(auto_envvar_prefix='AUGUR')

class AugurMultiCommand(click.MultiCommand):
    def __commands_folder(self):
        return os.path.abspath(os.path.dirname(__file__))

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(self.__commands_folder()):
            if not filename.startswith('_') and filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        cmdfile = "augur/application/cli" / Path(name + ".py")

        # Check that the command exists before importing
        if not cmdfile.is_file():
            return

        # Prefer to raise exception instead of silcencing it
        module = importlib.import_module('.' + name, 'augur.application.cli')
        return module.cli

@click.command(cls=AugurMultiCommand, context_settings=CONTEXT_SETTINGS)
@click.pass_context
def run(ctx):
    """
    Augur is an application for open source community health analytics
    """
    return ctx
