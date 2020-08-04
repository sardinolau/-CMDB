#初始化采集信息方法


import importlib
from settings import PLUGING_CLASS_DICT


def get_server_info(ssh,hostname):
    server_info={}
    for key,path in PLUGING_CLASS_DICT.items():
        module_path,class_name = path.rsplit('.',maxsplit=1)
        module = importlib.import_module(module_path)

        cls = getattr(module,class_name)
        plugin_object = cls()
        info = plugin_object.process(ssh,hostname)
        # print(key,info)
        server_info[key]=info
    return server_info