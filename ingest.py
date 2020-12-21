"""Module handles ingesting of data from different sources

Data could originate from many sources, exmaples:
File from local file system
File from online url
API response
NoSQL tables

This module shall handle ingesting of the data in raw format into a Python list

Implemented ingesters:
Local file system
"""


from source_type import DataSource


def local_ingest(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

def url_ingest():
    pass


ingesters = {DataSource.LOCAL: local_ingest, DataSource.URL: url_ingest}
