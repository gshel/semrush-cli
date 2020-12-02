import click
import requests
import semrush.resources


API_ENDPOINT = "https://api.semrush.com/?"


@click.group()
@click.argument("domain")
@click.pass_context
def domain(ctx, domain: str):
    """Domain Reports
    \f
    :param domain: A unique name of a website you’d like to investigate.
    :type domain: str
    """
    ctx.ensure_object(dict)
    ctx.obj['domain'] = domain


@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def adwords(ctx, **kwargs):
    """Lists keywords that bring users to a domain via Google's paid search results.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_adwords'
    required_params['domain'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def adwords_adwords(ctx, **kwargs):
    """Lists a domain’s competition in paid search results.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_adwords_adwords'
    required_params['domain'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def adwords_historical(ctx, **kwargs):
    """Shows keywords a domain has bid on in the last 12 months and its positions in paid search results.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_adwords_historical'
    required_params['domain'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def adwords_unique(ctx, **kwargs):
    """Shows unique ad copies SEMrush noticed when the domain ranked in Google's paid search results for keywords from our databases.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_adwords_unique'
    required_params['domain'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def domains(ctx, **kwargs):
    """Compares up to five domains by common keywords, unique keywords, all keywords, or search terms that are unique to the first domain.
    \f
    :param domains: A URL-encoded string that contains domains in a specified format, separated by "|".
    :type domains: str
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_domains'
    required_params['domains'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def shopping(ctx, **kwargs):
    """Lists keywords that trigger a domain’s product listing ads to appear in Google's paid search results.
    \f
    :param domains: A URL-encoded string that contains domains in a specified format, separated by "|".
    :type domains: str
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_shopping'
    required_params['domains'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)
    

@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def shopping_unique(ctx, **kwargs):
    """Shows product listing ad copies SEMrush noticed when the domain ranked in Google's paid search results for keywords from our databases.
    \f
    :param domains: A URL-encoded string that contains domains in a specified format, separated by "|".
    :type domains: str
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_shopping_unique'
    required_params['domains'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def organic(ctx, **kwargs):
    """List keywords that bring users to a domain via Google's top 100 organic search results.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_organic'
    required_params['domain'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)

@domain.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def organic_organic(ctx, **kwargs):
    """Lists a domain’s competition in organic search results.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'domain_organic_organic'
    required_params['domain'] = ctx.obj['domain']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@click.group()
@click.argument("keyword")
@click.pass_context
def keyword(ctx, keyword: str):
    """Keyword Reports
    \f
    :param keyword: A keyword or keyword expression you'd like to investigate.
    :type keyword: str
    """
    ctx.ensure_object(dict)
    ctx.obj['phrase'] = keyword


@keyword.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def overview(ctx, **kwargs):
    """Provides a summary of a keyword, including its volume, CPC, competition, and the number of results in a chosen regional database.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'phrase_this'
    required_params['phrase'] = ctx.obj['phrase']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@keyword.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def related(ctx, **kwargs):
    """Provides an extended list of related keywords, synonyms, and variations relevant to a queried term in a chosen database.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'phrase_related'
    required_params['phrase'] = ctx.obj['phrase']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


@keyword.command()
@click.option("-db", "--database", default="us")
@click.option("--display-limit", default=1)
@click.option("--export-escape", default=1)
@click.pass_context
def fullsearch(ctx, **kwargs):
    """Provides a list of broad matches and alternate search queries, including particular keywords or keyword expressions.
    \f
    :Keyword Arguments:
        * *database* (``str``) -- 
        * *display_limit* (``int``) -- 
        * *export_escape* (``int``) -- 
    """
    required_params = dict()
    required_params['type'] = 'phrase_fullsearch'
    required_params['phrase'] = ctx.obj['phrase']
    for i in kwargs:
        required_params[i] = kwargs[i]
    query_string = semrush.resources.assemble_query_string(**required_params)
    resp = requests.get(API_ENDPOINT+query_string)
    click.echo(resp.text)


if __name__ == "__main__":
    import subprocess
    # command = """semrush keyword 'baby goat' fullsearch"""
    # subprocess.run(['semrush', 'keyword', 'baby goat', 'fullsearch'])
    command = "semrush domain www.montrealgazette.com organic-competition"
    subprocess.run(command.split(' '))