from django.contrib import admin
from django.urls import include, path

app_name = 'entries'
urlpatterns = [
    path('entries/', include('entries.urls')),
    path('admin/', admin.site.urls),
]