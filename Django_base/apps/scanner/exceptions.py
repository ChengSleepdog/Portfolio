from rest_framework import status
from rest_framework.exceptions import APIException
from utils.exceptions import TracebackApiException
from django.utils.translation import gettext_lazy as _

# TracebackApiException
# ----------------------------------------------------------------

class UnException(TracebackApiException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _(' Unexcept error happend ')
    default_code = ' unexcept_error_happened '

# APIException
# ----------------------------------------------------------------

class NmapScanParameterError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _(' Nmap scan parameter is invalid ')
    default_code = ' nmap_scan_parameter_is_invalid '
