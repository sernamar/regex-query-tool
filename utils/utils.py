import re

CLEANER = re.compile("<.*?>")  # global, to avoid compiling it every time the "remove_style" function is called


def get_matches(pattern, string):
    return re.findall(pattern, string)


def style_word(word):
    """"
    Adds a "color red" style to the word.
    """
    return '<span style="color: red;">' + word + '</span>'


def add_style(string, matches):
    words_list = [style_word(word) if word in matches else word
                  for word in string.split()]
    return " ".join(words_list)


def remove_style(string):
    return re.sub(CLEANER, "", string)
