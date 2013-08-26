__author__ = 'mriegel'

import re


def clear_quotation_marks(string_to_clear):
    #return re.sub('^\"(.*)\"$', lambda m: "%s" % m.group(0), string_to_clear)
    if string_to_clear == '-':
        return None

    if string_to_clear[0] == '"':
        string_to_clear = string_to_clear[1:]

    if string_to_clear[-1] == '"':
        string_to_clear = string_to_clear[:-1]

    return string_to_clear


def is_wkn(string):
    return re.match(r'^[0-9A-Z]{6}$', string)


def is_isin(string):
    return re.match(r'^([A-Z]{2})([0-9A-Z]{10})$', string)