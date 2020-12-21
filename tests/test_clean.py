"""Module tests the methods defined in clean.py module"""


import unittest
from clean import cleaners, json_clean, xml_clean, text_clean
from file_type import DataType


class FileTypeTest(unittest.TestCase):
    """Tests methods in clean.py module"""

    def test_cleaners_DataType_JSON(self):
        self.assertEqual(cleaners[DataType.JSON], json_clean)

    def test_cleaners_DataType_XML(self):
        self.assertEqual(cleaners[DataType.XML], xml_clean)

    def test_cleaners_DataType_TEXT(self):
        self.assertEqual(cleaners[DataType.TEXT], text_clean)

