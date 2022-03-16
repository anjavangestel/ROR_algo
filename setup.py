from os import path
from codecs import open
from setuptools import setup, find_packages

# get current directory
here = path.abspath(path.dirname(__file__))

# get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# setup the package
setup(
    name='v6-ROR_algo-py',
    version="1.0.0",
    description='vantage6 ROR algorithm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/anjavangestel/v6-ROR_algo-py',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # 'vantage6-client'
    ]
    # ,
    # extras_require={
    # },
    # package_data={
    #     'vantage6.tools': [
    #         'VERSION'
    #     ],
    # }
)
