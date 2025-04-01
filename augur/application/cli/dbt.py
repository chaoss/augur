# SPDX-License-Identifier: MIT
"""
Augur CLI integration for DBT (Data Build Tool): https://www.getdbt.com
"""
import os
import subprocess
import click

@click.group("dbt", short_help="DBT commands integrated into Augur CLI.")
def cli():
    """Manage DBT workflows from Augur CLI."""
    pass

def run_dbt_command(command):
    """ Run a DBT command with the given arguments. """
    dbt_venv_path = os.getenv("DBT_VENV_PATH", os.path.expanduser("~/.virtualenvs/dbt_venv/bin"))
    dbt_executable = os.path.join(dbt_venv_path, "dbt")

    dbt_profiles_path = os.path.abspath("augur/application/dbt") 
    
    if not os.path.isfile(dbt_executable):
        click.echo(f"DBT executable not found at {dbt_executable}. Ensure DBT is installed.", err=True)
        return False

    try:
        result = subprocess.run([dbt_executable] + command + ["--profiles-dir", dbt_profiles_path], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        click.echo(f"DBT command failed: {e}", err=True)
        return False

@cli.command("run")
def run_dbt():
    """Run DBT models."""
    if run_dbt_command(["run", "--profiles-dir", "/augur/application/dbt"]):
        click.echo("DBT models executed successfully!")

@cli.command("debug")
def debug_dbt():
    """Debug DBT setup."""
    if run_dbt_command(["debug", "--profiles-dir", "/augur/application/dbt"]):
        click.echo("DBT debug completed successfully!")

@cli.command("test")
def test_dbt():
    """Run DBT tests."""
    if run_dbt_command(["test", "--profiles-dir", "/augur/application/dbt"]):
        click.echo("DBT tests executed successfully!")

@cli.command("compile")
def compile_dbt():
    """Compile DBT models."""
    if run_dbt_command(["compile", "--profiles-dir", "/augur/application/dbt"]):
        click.echo("DBT models compiled successfully!")
