from django.db import models

# Create your models here.
class BusinessUnit(models.Model):
    '''
    业务线
    '''
    name = models.CharField('业务线',max_length=64,unique=True)
    def __str__(self):
        return self.name

class IDC(models.Model):
    '''
    机房信息
    '''
    name = models.CharField('机房',max_length=32)
    floor = models.IntegerField('楼层',default=1)
    def __str__(self):
        return self.name

class Server(models.Model):
    '''
    主机服务器
    '''
    bussiness_unit = models.ForeignKey(verbose_name='业务线',to='BusinessUnit',null=True,blank=True,on_delete=models.CASCADE)

    idc = models.ForeignKey(verbose_name='机房',to='IDC',null=True,blank=True,on_delete=models.CASCADE)
    cabinet_num = models.CharField('机柜号',max_length=32,null=True,blank=True)
    cabinet_order = models.CharField('机柜中序号',max_length=32,null=True,blank=True)

    hostname = models.CharField(verbose_name='主机名',max_length=32)
    last_date = models.DateTimeField(verbose_name='最近汇报时间',null=True,blank=True)

    '''
    主机信息
    '''
    uname = models.CharField(verbose_name="主机", max_length=32,null=True,blank=True)
    version = models.CharField(verbose_name="版本", max_length=32,null=True,blank=True)

class Board(models.Model):
    '''
    主板信息
    '''
    manufacturer = models.CharField(verbose_name="厂商",max_length=32)
    model = models.CharField(verbose_name="类型",max_length=32)
    sn = models.CharField(verbose_name="序列号",max_length=32)
    server = models.ForeignKey(verbose_name='服务器',to=Server,on_delete=models.CASCADE)

class Memory(models.Model):
    '''
    内存信息
    '''
    capacity = models.CharField(verbose_name="容量", max_length=32)
    slot = models.CharField(verbose_name="槽口", max_length=32)
    model = models.CharField(verbose_name="模型", max_length=32)
    speed = models.CharField(verbose_name="速率", max_length=32)
    manufacturer = models.CharField(verbose_name="厂商", max_length=32)
    sn = models.CharField(verbose_name="序列号", max_length=32)
    server = models.ForeignKey(verbose_name='服务器', to=Server, on_delete=models.CASCADE)


class AssetsRecord(models.Model):
    '''
    资产变更记录
    '''
    content = models.TextField(verbose_name='内容')
    server = models.ForeignKey(verbose_name='服务器', to=Server, on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name='时间',auto_now_add=True)