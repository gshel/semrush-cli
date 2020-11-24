import click

from semrush import _logging
from semrush.commands import accounts, analytics, projects


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Enable DEBUG level logging.")
@click.option("-vv", "--very-verbose", is_flag=True, help="Enable DEBUG level logging and import library logging.")
def entry_point(verbose: bool, very_verbose: bool):
    _logging.set_verbosity(__name__, verbose, very_verbose)

entry_point.add_command(accounts.accounts)
entry_point.add_command(analytics.domain)
entry_point.add_command(analytics.keyword)
