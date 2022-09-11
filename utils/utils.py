import re

CLEANER = re.compile("<.*?>")  # global, to avoid compiling it every time the "remove_style" function is called


def get_matches(pattern, string):
    return re.findall(pattern, string)


def style_word(word):
    """"
    Adds a "bold" and "color red" style to the word.
    """
    return '<span style="font-weight: bold; color: red;">' + word + '</span>'


def create_html_paragraphs(sentences_list):
    return "".join(["<p>" + sentence + "</p>" for sentence in sentences_list])


def add_style(string, matches):
    paragraphs = string.split("\n")
    sentence_list = []
    for paragraph in paragraphs:
        words_list = [style_word(word) if word in matches else word for word in paragraph.split()]
        sentence = " ".join(words_list)
        sentence_list.append(sentence)
    return create_html_paragraphs(sentence_list)


def remove_style(string):
    return re.sub(CLEANER, "", string)
