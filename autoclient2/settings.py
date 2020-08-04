import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


SSH_PORT=22
SSH_USER='root'
SSH_PASSWORD='1'

PLUGING_CLASS_DICT = {
    'basic':'lib.plugins.basic.BasicPlugin',
    'board':'lib.plugins.board.BoardPlugin',
    'memory':'lib.plugins.memory.MemoryPlugin',
    'network':'lib.plugins.network.NetworkPlugin',
}

# LOCAL_DISK_FILE_PATH = os.path.join(BASE_DIR,'files/disk.out')

API_URL = 'http://127.0.0.1:8000/api/v1/server/'