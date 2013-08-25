__author__ = 'mriegel'


def clear_number(s):
    if s == '-' or s == 'N/A':
        return None

    if s[-1] == 'M':
        s = float(s[:-1])*1000000

    if s[-1] == 'B':
        s = float(s[:-1])*1000000000

    return int(s)


def clear_float(s):
    if s == '-':
        return None

    return float(s)