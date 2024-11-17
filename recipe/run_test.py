import os
from importlib.metadata import version


assert version("pyee") == os.environ["PKG_VERSION"], \
    "package version does not match expected version"
