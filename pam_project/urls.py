from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('api_app.urls')),
    path('', admin.site.urls),
]
