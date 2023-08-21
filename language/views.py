from django.shortcuts import render
from django.utils.translation import gettext as _


# Create your views here.
def multiple_language(request):
    context = {
        "greeting": _("Welcome to Programming World"),
    }
    return render(request, "index.html", context)
