import click
import requests
import semrush.resources

API_ENDPOINT = "http://www.semrush.com/users/countapiunits.html?"

@click.group(invoke_without_command=True)
@click.pass_context
def accounts(ctx):
    """Check API Units Balance
    """
    if ctx.invoked_subcommand is None:
        get()

def get():
    query_string = semrush.resources.assemble_query_string()
    response = requests.get(API_ENDPOINT+query_string)
    click.echo(f"Current API Balance: {response.text}")
    return response

if __name__ == "__main__":
    get()