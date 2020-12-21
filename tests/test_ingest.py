"""Module tests the methods defined in ingest.py module"""


import unittest
from ingest import local_ingest, url_ingest, ingesters
from source_type import DataSource


class FileTypeTest(unittest.TestCase):
    """Tests methods in ingest.py module"""

    def setUp(self) -> None:
        self.test_file_path_for_ingest = './tests/test_files/ingest_test.txt'
        self.data_in_ingest_test_file = ['This is a file\n', 'With some text\n', 'To be used\n', 'for testing']

    def test_ingesters_DataSource_local(self):
        self.assertEqual(ingesters[DataSource.LOCAL], local_ingest)

    def test_ingesters_DataSource_url(self):
        self.assertEqual(ingesters[DataSource.URL], url_ingest)

    def test_local_ingest(self):
        self.assertEqual(local_ingest(self.test_file_path_for_ingest), self.data_in_ingest_test_file)

