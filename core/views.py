from django.shortcuts import render
from django.views.decorators.http import require_GET

from utils.utils import get_matches


@require_GET
def index(request):
    if request.htmx:
        pattern = request.GET.get("pattern")
        string = request.GET.get("test-string")
        matches = get_matches(pattern, string)
        return render(request, "matches.html", {"matches": matches})
    else:
        return render(request, "index.html")
