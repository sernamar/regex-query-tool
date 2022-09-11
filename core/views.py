from django.shortcuts import render

from utils.utils import get_matches, add_style

initial_text = """
Now is the winter of our discontent. Made glorious summer by this sun of York. And all the clouds that lour'd upon our house. In the deep bosom of the ocean buried.

Now are our brows bound with victorious wreaths. Our bruised arms hung up for monuments. Our stern alarums changed to merry meetings. Our dreadful marches to delightful measures.
"""
initial_pattern = "[A-Z]\\w+"


def index(request):
    if request.htmx:
        text = request.POST.get("text")
        request.session["text"] = text

        pattern = request.session.get("pattern")
        matches = get_matches(pattern, text)
        matches = add_style(text, matches)
        return render(request, "matches.html", {"text": text, "matches": matches})
    else:
        if request.session.get("pattern") is None:
            request.session["pattern"] = initial_pattern
        pattern = request.session.get("pattern")
        if request.session.get("text") is None:
            request.session["text"] = initial_text
        text = request.session.get("text")
        matches = get_matches(pattern, text)
        matches = add_style(text, matches)
        return render(request, "index.html", {"pattern": pattern, "text": text, "matches": matches})


def render_matches(request):
    pattern = request.POST.get("pattern")
    request.session["pattern"] = pattern

    text = request.session.get("text")
    matches = get_matches(pattern, text)
    matches = add_style(text, matches)
    return render(request, "matches.html", {"text": text, "matches": matches})
