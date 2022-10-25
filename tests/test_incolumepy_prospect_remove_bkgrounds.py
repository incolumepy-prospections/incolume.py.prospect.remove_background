import re

import pytest
from incolumepy.prospect.remove_bkgrounds import __version__


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ("1.1.1-rc-0", False),
        ("1.0.1-dev0", False),
        ("1.1.1-rc0", False),
        ("1.1.1-a0", False),
        ('1.0', False),
        ('1', False),
        ("0.1.0", True),
        ("1.0.0", True),
        ("1.0.1", True),
        ("1.1.1", True),
        ("1.1.1-rc.0", True),
        ("1.0.1-dev.0", True),
        ("1.0.1-dev.1", True),
        ("1.0.1-dev.2", True),
        ("1.0.1-alpha.0", True),
        ("1.0.1-alpha.266", True),
        ("1.0.1-dev.0", True),
        ("1.0.1-beta.0", True),
        ("1.1.1-alpha.99999", True),
        ("99999999999.1.1-alpha.99999", True),
        ("1.1.1-rc.99999", True),
        ("1.1.99999", True),
        ("1.999999.1", True),
        (__version__, True),
    )
)
def test_version(entrance, expected):
    """
    Test for semantic versioning.

    :param entrance: entrance parameter
    :param expected: expected parameter
    :return: assert result
    """
    assert bool(
        re.fullmatch(r"\d+(\.\d+){2}(-\w+\.\d+)?", entrance, flags=re.I)
    ) == expected
