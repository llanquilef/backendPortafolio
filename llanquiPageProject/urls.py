from django.contrib import admin
from django.urls import include, path

# ====== URLS PATTERNS ======
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('llanquiPageApp.urls')),
]