from django.shortcuts import render,redirect
from api import models
# Create your views here.
def index(request):
    '''

    :param request:
    :return:
    '''
    server_list = models.Server.objects.all()
    return render(request,'index.html',locals())

from django import forms
class ServerModelform(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = ['hostname','bussiness_unit','idc','cabinet_num','cabinet_order']

    def __init__(self,*args,**kwargs):
        super(ServerModelform,self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form_control'

def create_server(request):
    '''
    新增服务器
    :param request:
    :return:
    '''
    if request.method=='GET':
        form = ServerModelform()

        return render(request,'create_server.html',locals())
    form = ServerModelform(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request,'create_server.html',locals())