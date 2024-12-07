"""
URL configuration for fuelguardapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from users.views import UserLoginAPIView, UserLogoutAPIView, UserLogoutAllAPIView

# Configuración de drf-yasg para Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="FuelGuard API",
        default_version="v1",
        description="Documentación de la API para el monitoreo de combustible.",
        contact=openapi.Contact(email="soporte@fuelguard.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/login/", UserLoginAPIView.as_view(), name="custom_login"),
    path("accounts/login/", UserLoginAPIView.as_view(), name="custom_login"),
    path("api/logout/", UserLogoutAPIView.as_view(), name="custom_logout"),
    path("api/logoutall/", UserLogoutAllAPIView.as_view(), name="custom_logoutall"),
    path("api/", include("FuelSensor.urls", namespace="FuelSensor")),
    re_path(
        r"^$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
