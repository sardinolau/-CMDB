from .base import BasePlugin
from lib.utils.response import Response
import traceback
from lib.utils.convert import convert_mb_to_gb




class MemoryPlugin(BasePlugin):
    '''
    内存信息
    '''
    def process(self,ssh,hostname):
        response = Response()
        try:
            result = ssh(hostname, 'dmidecode -q -t 17 2>/dev/null')

            response.data = self.parse(result)
        except Exception as e:
            response.status = False
            response.error = traceback.format_exc()
        # print(response.dict)
        return response.dict

    def parse(self,content):
        ram_dict ={}
        key_map = {
            'Size':'capacity',
            'Locator':'slot',
            'Type':'model',
            'Speed':'speed',
            'Manufacturer':'manufacturer',
            'Serial Number':'sn',
        }
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':'))>1:
                    key,value = line.split(':')
                else:
                    key =line.split(';')[0]
                    value = ''
                if key in key_map:
                    if key =='Size':
                        segment[key_map['Size']] = convert_mb_to_gb(value,0)
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']]=segment

        return ram_dict