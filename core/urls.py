from django.urls import path

from core import views
from core.forms import PasswordChangeView

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("matches/", views.render_matches, name="matches"),

    # password change path to redirect to "index" after success
    path("accounts/password/change/", PasswordChangeView.as_view(), name="account_change_password"),
]
