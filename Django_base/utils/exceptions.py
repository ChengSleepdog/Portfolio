import traceback
import logging

from django.utils.encoding import force_str
from rest_framework import status
from rest_framework.exceptions import APIException
from typing import Union, Type, Callable, Tuple

logger = logging.getLogger('debug')  # 常態log
logger_debug = logging.getLogger('debug')  # 開發者實體檔案問題追蹤用

standard_level = ['info', 'debug', 'warning', 'error']

class TracebackApiException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'System internal error.'
    default_code = 'unknown_error'

    def __init__(self,
                 raiser: Tuple[Union[Type, str, None], Union[Callable, str]],
                 detail: Union[list, dict, str] = None,
                 code=None,
                 format=None):

        format = format or dict()
        super().__init__(self.format_detail(detail, **format), code)
        self.traceback = traceback.format_exc()

        raiser_class = raiser[0]
        raiser_func = raiser[1]
        if isinstance(raiser_class, type):
            raiser_class = raiser_class.__name__
        if isinstance(raiser_func, Callable):
            raiser_func = raiser_func.__name__
            
        logger.warning(f'[{raiser_class}] {raiser_func}: {self.__class__}')
        logger_debug.debug(
            f'[{raiser_class}] {raiser_func}: \n{traceback.format_exc()}')

    def format_detail(self, detail=None, **arguments):
        if detail is None:
            detail = self.default_detail
        if isinstance(detail, list):
            for i in range(0, len(detail)):
                detail[i] = force_str(detail[i]).format(**arguments)
            return detail
        if isinstance(detail, dict):
            for key, value in detail.items():
                detail[key] = force_str(value).format(**arguments)
            return detail

        return force_str(detail).format(**arguments)