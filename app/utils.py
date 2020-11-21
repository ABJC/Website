
from os.path import exists
import os
from json import load


def localization(locale: str, page: str = None):
    urlpath = page.split('.')
    dirpath = os.path.dirname(os.path.abspath(__file__))
    path = f'{dirpath}/localization/{locale}.json'

    print(path)
    if not exists(path):
        locale = 'en'
        path = f'{dirpath}/localization/{locale}.json'

    with open(path) as fp:
        strings = load(fp)
        if page == None:
            return locale, strings
        else: 
            for page in urlpath:
                strings = strings[page]
            return locale, strings

    return None