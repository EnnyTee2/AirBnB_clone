#!/usr/bin/env python3
"""Instantiates a storage object by initialising
a file storage engine (FileStorage).
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
