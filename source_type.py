"""Module handles recognition of type of sources

Data could originate from many sources, examples:
File from local file system
File from online url
API response
NoSQL tables

This module creates a DataSource enum and shall handle recognition of the data source type

Implemented sources:
Local file system
http URLs
"""


import re
from enum import Enum


class DataSource(Enum):
    LOCAL = 1
    URL = 2


def is_url(filepath):
    url_regex = re.compile('http*')
    if url_regex.match(filepath):
        return True
    else:
        return False

def get_source_type(file_source):
    if is_url(file_source):
        data_source = DataSource.URL
    else:
        data_source = DataSource.LOCAL
    return data_source