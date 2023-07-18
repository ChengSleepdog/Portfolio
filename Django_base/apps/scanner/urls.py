from rest_framework import routers

from apps.scanner.views import NmapScanViewSet

router = routers.DefaultRouter()

router.register('nmap-scan', NmapScanViewSet, basename='nmap-scan')

urlpatterns = []
urlpatterns += router.urls