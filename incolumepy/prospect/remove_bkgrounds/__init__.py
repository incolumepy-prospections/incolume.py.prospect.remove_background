"""
Principal Module.

Update metadata from version by semver
"""
import tomli
from pathlib import Path

versionfile = Path(__file__).parent/'version.txt'

with Path(__file__).parents[3].joinpath('pyproject.toml').open('rb') as f:
    versionfile.write_text(
        f"{tomli.load(f)['tool']['poetry']['version']}\n"
    )

__version__ = versionfile.read_text().strip()
