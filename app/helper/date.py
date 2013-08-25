__author__ = 'mriegel'

from datetime import datetime as dt


def string_to_datetime(s):
    if s is None:
        return s

    try:
        return dt.strptime(s, "%m/%d/%Y")
    except ValueError:
        return None