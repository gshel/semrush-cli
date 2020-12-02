#import os
#import click

#__version__ = open(os.path.join(".", "VERSION")).read().strip() # TODO figure out how to include version at build time because pypi wheels do not include non-code files like VERSION