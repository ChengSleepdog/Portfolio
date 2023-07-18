import logging
logger = logging.getLogger('debug')

from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework import viewsets
from drf_yasg2.utils import swagger_auto_schema

from apps.scanner.nmap.nmmain import Scanner
from apps.scanner.exceptions import NmapScanParameterError, UnException
from apps.scanner.serializers import ScanParameterSerializer

# Create your views here.

class NmapScanViewSet(viewsets.GenericViewSet):
    serializer_class = ScanParameterSerializer

    @swagger_auto_schema(methods=['post'],
                         operation_summary='Nmap Scan',
                         operation_description='''
    ''',
                         request_body=ScanParameterSerializer)
    @action(methods=['post'], detail=False, url_path='scan')
    def nmap_scan(self, request):
        try:
            serializer = ScanParameterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            req = serializer.data
        except ValidationError:
            logger.info(" nmap 給予型別不符合規定 ")
            raise NmapScanParameterError()

        try:
            # 將掃描範圍型態從 list -> str
            # ------------------------------
            range_list = req.get("scan_host_range", ['127.0.0.1'])
            range_str = ' '.join(range_list)
            req.update({"scan_host_range": range_str})
            # ------------------------------

            scanner = Scanner()
            res = scanner.nmap_scan(condition=req)
        except:
            logger.info(" nmap_scan 掃描程序發生意外錯誤 ")
            raise UnException(
                raiser=(self.__class__, self.nmap_scan))

        return JsonResponse(res, status=status.HTTP_200_OK)

    @swagger_auto_schema(methods=['get'], operation_summary='Nmap Scan(fast)')
    @action(methods=['get'], detail=False, url_path=r'fast-scan/(?P<network>[\/.\d]+)')
    def fast_scan(self, request, network):
        condition = {
            'scan_host_range': f'{network}',
            'scan_mod': 'custom',
            'scan_args': " -sn -n "
        }
        try:
            scanner = Scanner()
            res = scanner.nmap_scan(condition=condition)
        except:
            logger.info(" fast_nmap 掃描程序發生意外錯誤 ")
            raise UnException(
                raiser=(self.__class__, self.fast_scan))

        # 回傳結果
        data = {'up': [list(i.keys())[0] for i in res['scan_result']]}
        return JsonResponse(data, status=status.HTTP_200_OK)