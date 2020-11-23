
from os.path import exists
import os
from json import load


def localization(locale: str,):
    dirpath = os.path.dirname(os.path.abspath(__file__))
    path = f'{dirpath}/localization/{locale}.json'

    if not exists(path):
        locale = 'en'
        path = f'{dirpath}/localization/{locale}.json'

    with open(path) as fp:
        strings = load(fp)
        return locale, strings

    return None

def get_data(filepath: str):
    dirpath = os.path.dirname(os.path.abspath(__file__))
    path = f'{dirpath}/data/{filepath}'

    extension = filepath.split(".")[-1]

    if not exists(path):
        return None

    text = ['html', 'markdown', 'text']
    with open(path) as fp:
        if extension in text:
            text = fp.read()
            return text
        elif extension == "json":
            content = load(fp)
            return content
