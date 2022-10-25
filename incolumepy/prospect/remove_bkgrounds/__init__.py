import tomli
from pathlib import Path


with Path(__file__).parents[3].joinpath('pyproject.toml').open('rb') as f:
    __version__ = tomli.load(f)['tool']['poetry']['version']
