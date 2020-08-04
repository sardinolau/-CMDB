from concurrent.futures import ThreadPoolExecutor
from settings import PLUGING_CLASS_DICT
from lib.plugins import get_server_info
import settings
import importlib
import requests
import json

#与虚拟机连接并且用指令采集原始数据
def ssh(hostname,cmd):
    import paramiko
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, password=settings.SSH_PASSWORD)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    result = stdout.read()
    # 关闭连接
    ssh.close()
    # print(result)
    return result.decode('utf-8')

def task(host):
    server_info = get_server_info(ssh,host)
    result = requests.post(
        url=settings.API_URL,
        json={"host": host, "info": server_info})
    print('把资产信息发送到：', result.text)

#获取服务器列表数据并返回
def get_server_list():
    response = requests.get(url=settings.API_URL)
    print(response.json())
    return response.json()['data']

#主运行程序，利用多线程
def run():
    # host_name = get_server_list()
    pool = ThreadPoolExecutor(10)
    host_name = ['192.168.241.129']
    # task(hostname)
    for host in host_name:
        pool.submit(task,host)

if __name__=='__main__':
    run()


