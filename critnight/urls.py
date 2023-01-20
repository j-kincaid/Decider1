from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from django.conf import settings

def artwork(request):
    return HttpResponse('Here are the artworks')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("artworks.urls")),
]
