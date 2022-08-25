#!/usr/bin/python3
"""create .tgz archive of web_static folder using Fabric
"""

from fabric import operations
from datetime import datetime


def do_pack():
    """create a .tgz archive of web_static
    """
    operations.local ('mkdir -p versions')
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "./versions/web_static_" + now + ".tgz"

    try:
        operations.local('tar -cvzf filename web_static')
        return filename
    except Exception:
        return None
