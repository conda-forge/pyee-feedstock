import os
import pkg_resources


assert pkg_resources.get_distribution("pyee").version == os.environ["PKG_VERSION"], \
    "package version does not match expected version"
