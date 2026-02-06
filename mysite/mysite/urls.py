from django.urls import path, include
from mysite.admin import admin_site

urlpatterns = [
    path("admin/", admin_site.urls),
    path("polls/", include("polls.urls")),
    path("contacts/", include("contacts.urls")),
]
