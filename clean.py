"""Module handles cleaning of raw data Python list created in the ingest.py module

Data might need to be cleaned, exmaples:
Single quotes instead of double quotes in JSON
Response spanning multiple lines instead of a single line in text files


This module shall handle cleaning of the raw data Python list and return a cleaned Python list

Implemented cleaners:
Replace single quotes in json with double quotes
"""

import re, ast
from file_type import DataType


def json_clean(data):
    # return [ast.literal_eval(line) for line in data]
    return [line.replace("'", '"') for line in data]


def xml_clean(data):
    return data


def text_clean(data):
    order_id = re.compile(r'\d\d\d\d\d\d\d')

    header = [item.replace('"', "") for item in data[0].split(sep=",")]
    new_header = ",".join(item for item in header)
    formatted_header = new_header.rstrip()

    product_data_double_quotes_cleaned = [item.replace('"', "") for item in data[1:]]
    product_data = [item.rstrip() for item in product_data_double_quotes_cleaned]

    def clean_data(data):
        my_list = []
        for i, item in enumerate(data):
            if order_id.match(item):
                my_list.append(item)
            else:
                my_list[-1] += item
        return my_list

    new_data = clean_data(product_data)

    new_data.insert(0, formatted_header)

    final_data = [item+"\n" for item in new_data]
    return final_data



cleaners = {DataType.JSON: json_clean, DataType.XML: xml_clean, DataType.TEXT: text_clean}