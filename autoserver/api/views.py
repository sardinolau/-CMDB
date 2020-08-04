

from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import datetime

from rest_framework.views import APIView
from rest_framework.views import View
from api.service.memory import process_memory_info
from api import models





# Create your views here.


# @method_decorator(csrf_exempt,name='dispatch')
# class ServerView(View):
class ServerView(APIView):
    def get(self,request,*args,**kwargs):
        '''
            获取未采集的服务器
            :return:
            '''

        today = datetime.date.today()
        # 最近汇报时间小于今天or最近汇报时间
        server_queryset = models.Server.objects.filter(Q(last_date__lt=today) | Q(last_date__isnull=True)).values_list(
            'hostname')
        server_list = [item[0] for item in server_queryset]
        return JsonResponse({'status': True, 'data': server_list})


    def post(self,request,*args,**kwargs):
        '''
        获取中控机获取的资产信息，并入库更新信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        server_info_dict = request.data
        hostname = server_info_dict['host']
        info_dict = server_info_dict['info']
        host_object = models.Server.objects.filter(hostname=hostname).first()
        if not host_object:
            return HttpResponse('服务器不存在')
        process_memory_info(host_object,info_dict['memory'])
        host_object.last_date = datetime.date.today()
        host_object.save()
        # print(server_info_dict)
        return HttpResponse('成功')