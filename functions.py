import re

def rejoined(src, sep='-', _split=re.compile('..').findall):
    return sep.join(_split(src))
