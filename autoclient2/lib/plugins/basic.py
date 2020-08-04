from .base import BasePlugin
from lib.utils.response import Response
import traceback


class BasicPlugin(BasePlugin):
    '''
    基本信息
    '''

    def process(self, ssh, hostname):
        response = Response()
        try:
            uname = ssh(hostname, 'uname').strip()
            version = ssh(hostname,'cat /proc/version').strip().split()[2]
            response.data = {
                'uname':uname,
                'version':version,
            }

        except Exception as e:
            response.status = False
            response.error = traceback.format_exc()
        # print(response.dict)
        return response.dict
