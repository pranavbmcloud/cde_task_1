"""Module handles writing of data

Data might have multiple destinations, example:
Local file system
Web endpoints
Exposed as a REST API

This module shall handle writing of the data based on the output format

Implemented writers:
Local file system
"""

import csv
from enum import Enum
from file_type import DataType


class OutputType(Enum):
    LOCAL = 1


def simple_writer(data, output_file):
    with open(output_file, 'w') as f:
        for line in data:
            f.writelines(line)

def text_writer(data, output_file):
    with open(output_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t')
        for line in data:
            r_stripped = line.rstrip()
            split_line = r_stripped.split(sep=",")
            csvwriter.writerow(split_line)


def dict_writer(data, output_file):
    with open(output_file, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\t')
        keys = []
        values = []
        for item in data.keys():
            keys.append(item)
        spamwriter.writerow(keys)
        for item in data.values():
            values.append(item)
        spamwriter.writerow(values)

def list_writer(data, output_file):
    for item in data:
        dict_writer(item, output_file)


writers = {DataType.JSON: list_writer, DataType.XML: list_writer, DataType.TEXT: text_writer}

