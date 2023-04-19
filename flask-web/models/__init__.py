#!/bin/env python3
"""the init file"""

from models.engine.db import DBStorage


storage = DBStorage()
storage.reload()
