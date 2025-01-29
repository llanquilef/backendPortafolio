from rest_framework import routers
from llanquiPageApp import views
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from django.views.generic import RedirectView

# ROUTERS
router = routers.DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'recomendacionespersonales', views.R_PersonalViewSet)
router.register(r'recomendacionesusuarios', views.R_UsuarioViewSet)

# URLS 
urlpatterns = [
    path('', RedirectView.as_view(url='/api/v1/', permanent=False)),
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='LlanquiAPI')),
    path('send-email/', views.EmailCreateView.as_view(), name='send_email'),

]
