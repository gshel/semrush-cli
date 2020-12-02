import os
import click

click.echo(os.getcwd())
__version__ = open(os.path.join("..", "VERSION")).read().strip()
