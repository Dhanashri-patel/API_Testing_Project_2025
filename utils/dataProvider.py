import csv
import json
import os

import openpyxl
from pygments.lexers import data


def read_with_json(filepath):
    base_dir= os.path.dirname(os.path.abspath(__file__))
    fullpath = os.path.join(base_dir,filepath)

    with open(fullpath, "r") as json_file:
        data = json.load(json_file)

    return [(item,)for item in data]

def read_with_excel(filepath,sheetname):

    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook[sheetname]

    header = [cell.value for cell in sheet[1]]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if any(row):
            data.append(dict(zip(header,row)))

    return data

def read_with_csv(filepath):
    base_dir= os.path.dirname(os.path.abspath(__file__))
    fullpath = os.path.join(base_dir,filepath)

    data= []
    with open(fullpath, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        for row in reader:
            data.append(dict(zip(header,row)))

    return data

#read_with_csv(os.path.abspath(os.path.join(os.path.dirname(__file__),"../testdata/products_data.csv")))



