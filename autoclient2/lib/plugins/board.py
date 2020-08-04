from .base import BasePlugin
from lib.utils.response import Response
import traceback

class BoardPlugin(BasePlugin):
    '''
    硬盘信息
    '''
    def process(self,ssh,hostname):
        response = Response()
        try:
            result = ssh(hostname,'dmidecode -t1')

            response.data = self.parse(result)
        except Exception as e:
                response.status = False
                response.error = traceback.format_exc()
        # print(response.dict)
        return response.dict

    def parse(self,content):
        result = {}
        key_map = {
            'Manufacturer':'manufacturer',
            'Product Name':'model',
            'Serial Number':'sn',
        }
        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data)==2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]
        return result