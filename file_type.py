"""Module handles recognition of data format

Data could be of different formats, examples:
Text files
Binaries
JSON
XML
YAML
sql

This module creates a DataType enum and shall handle recognition of the data format

Implemented sources:
.json
.xml
.txt
"""


from enum import Enum


class DataType(Enum):
    JSON = 1
    XML = 2
    TEXT = 3


def get_data_type(file_source):
    if file_source.endswith('json'):
        data_type = DataType.JSON
    elif file_source.endswith('xml'):
        data_type = DataType.XML
    elif file_source.endswith('txt'):
        data_type = DataType.TEXT
    else:
        raise ValueError('Cannot extract data from {}'.format(file_source))
    return data_type