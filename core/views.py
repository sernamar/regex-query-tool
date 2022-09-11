from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

from utils.utils import get_matches

initial_text = "Some random text"
initial_pattern = "[A-Z]\\w+"


def index(request):
    if request.htmx:
        text = request.POST.get("text")
        request.session["text"] = text

        pattern = request.session.get("pattern")
        print("Pattern in session:", pattern)
        matches = get_matches(pattern, text)
        return render(request, "matches.html", {"text": text, "matches": matches})
    else:
        if request.session.get("pattern") is None:
            request.session["pattern"] = initial_pattern
        pattern = request.session.get("pattern")
        if request.session.get("text") is None:
            request.session["text"] = initial_text
        text = request.session.get("text")
        matches = get_matches(pattern, text)
        return render(request, "index.html", {"pattern": pattern, "text": text, "matches": matches})


def render_matches(request):
    pattern = request.POST.get("pattern")
    request.session["pattern"] = pattern

    text = request.session.get("text")
    matches = get_matches(pattern, text)
    return render(request, "matches.html", {"text": text, "matches": matches})
