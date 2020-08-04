from .base import BasePlugin
from lib.utils.response import Response
from lib.utils.convert import convert_mb_to_gb
import traceback


class NetworkPlugin(BasePlugin):
    '''
    网络信息
    '''

    def process(self, ssh, hostname):
        response = Response()
        try:
            response.data = 'network'

        except Exception as e:
            response.status = False
            response.error = traceback.format_exc()
        # print(response.dict)
        return response.dict