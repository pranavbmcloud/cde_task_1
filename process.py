"""Module handles processing of data

Some data formats provide easy to process methods to read data, example:
json.loads()
xml.etree.ElementTree.parse()

This module shall handle processing of the data

Implemented processors:
json.loads
xml.etree.ElementTree.parse()
"""


import json
import xml.etree.ElementTree as ET
from file_type import DataType


def json_process(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return [json.loads(line) for line in data]


# def xml_process(file):
#     tree = ET.parse(file)
#     root = tree.getroot()
#     return XmlDictConfig(root)


def text_process(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data

processors = {DataType.JSON: json_process, DataType.XML: json_process, DataType.TEXT: text_process}