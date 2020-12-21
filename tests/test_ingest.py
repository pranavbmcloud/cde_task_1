"""Module tests the methods defined in ingest.py module"""


import unittest
from ingest import local_ingest, url_ingest, ingesters
from source_type import DataSource


class FileTypeTest(unittest.TestCase):
    """Tests methods in ingest.py module"""

    def test_ingesters_DataSource_local(self):
        self.assertEqual(ingesters[DataSource.LOCAL], local_ingest)

    def test_ingesters_DataSource_url(self):
        self.assertEqual(ingesters[DataSource.URL], url_ingest)

    def test_local_ingest(self):
        self.assertEqual(local_ingest('./tests/ingest_test.txt'), ['This is a file\n', 'With some text\n', 'To be used\n', 'for testing'])

