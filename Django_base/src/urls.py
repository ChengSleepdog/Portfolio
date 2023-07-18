"""Django_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# swagger 介面
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
# apps 引用
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scan/', include('apps.scanner.urls')),# 載入在 apps.scanner 
]

schema_view = get_schema_view(
    openapi.Info(
        title='2023',
        default_version='0.0.1',
        description='有api之url皆需要以`/`做為結尾, 否則可能造成錯誤'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]

# 允許靜態檔案直接透過django取得
urlpatterns += staticfiles_urlpatterns()
