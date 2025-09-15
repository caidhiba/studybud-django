
from django.contrib import admin
from django.urls import path, include






urlpatterns = [
    path('admin/', admin.site.urls),
    # using include means sending the user to the base.urls file and then match the urls there
    path('', include('base.urls')),
]
