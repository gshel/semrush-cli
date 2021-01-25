# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib
import os

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")
version = {}
with open(os.path.join(".", "semrush", "__init__.py")) as fp:
    exec(fp.read(), version)

setup(
    name="semrush-cli",
    version=version['__version__'],
    description="A command-line tool for interacting with the SEMRush API v3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="",
    author_email="",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="semrush, command-line, command-line interface",
    package_dir={"": "."},
    packages=find_packages(where="."),
    include_package_data=True,
    python_requires=">=3.8, <4",
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # list _abstract_ dependencies here (https://caremad.io/posts/2013/07/setup-vs-requirement/)
    install_requires=[
        "click",
        "pathlib",
        "pbr",
        "requests",
    ],
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={
        "test": [
            "black",
            "pytest",
            "pytest-cov",
            ], 
        },  # Optional
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points='''
        [console_scripts]
        semrush=semrush.cli:entry_point
    ''',
    project_urls={
        "Bug Reports": "https://github.com/gshel/semrush-cli/issues",
        "Source": "https://github.com/gshel/semrush-cli",
    },
)