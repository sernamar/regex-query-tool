import re


def get_matches(pattern, string):
    return re.findall(pattern, string)
