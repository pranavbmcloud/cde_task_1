"""Module handles flattening of nested data formats

Some data formats have nested structures. Such formats need to be flattened.

This module shall handle flattening of the data

Implemented flatteners:

"""


from itertools import chain, starmap
from file_type import DataType


def flatten(dictionary):
    """Flattens a nested json file"""

    def unpack(parent_key, parent_value):
        if isinstance(parent_value, dict):
            for key, value in parent_value.items():
                temp1 = parent_key + '_' + key
                yield temp1, value
        elif isinstance(parent_value, list):
            i = 0
            for value in parent_value:
                temp2 = parent_key + '_' + str(i)
                i += 1
                yield temp2, value
        else:
            yield parent_key, parent_value

    while True:
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
        if not any(isinstance(value, dict) for value in dictionary.values()) and \
                not any(isinstance(value, list) for value in dictionary.values()):
            break

    return dictionary

def already_flat(data):
    return data

flatteners = {DataType.JSON: flatten, DataType.XML: flatten, DataType.TEXT: already_flat}