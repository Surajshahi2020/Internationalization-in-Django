from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from language.views import multiple_language

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("home/", multiple_language),
)
