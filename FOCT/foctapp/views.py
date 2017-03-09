from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.db.models import Q
from rest_framework import viewsets
from .serializers import UserSerializer,GroupSerializer
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import Collector,Mirror
from .serializers import CollectorSerializer,MirrorSerializer
from rest_framework import generics
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import time
import re
import json



#用户处理

def home(request):
    if request.user.is_authenticated():
        username=request.user.username
        content={'login':username,
             'logout':"注销",
             }
    else:
        content={'login':"登录",
             'logout':"注销",
             }
    return render(request,'foctapp/home.html',content)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('../home')
    if request.method =='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        remember_me=request.POST.get('remember_me')
        print(remember_me)
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                return render(request,'foctapp/home.html')
            else:
                return HttpResponse("disable account")
        else:
            return  HttpResponse('invalid login')
    else:
        return render(request,'foctapp/login.html')
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('../login')


#保存数据
def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        content = {'login': username,
               'logout': "",
               }
    else:
        content = {'login': "登录",

           }
    return render(request,'foctapp/index.html',content)
def cjq_test(request):
    username=request.user.username
    if request.method == 'POST':
        name=request.POST.get('cjqtest_name')
        phase_error=request.POST.get('cjqtest_phaseerror')
        current_error=request.POST.get('cjqtest_currenterror')
        cjqtest_current=request.POST.get('cjqtest_current')
        light_power=request.POST.get('cjqtest_lightpower')
        ref=request.POST.get('cjqtest_ref')
        composite_error=request.POST.get('cjqtest_Inputcomposite_error')
        # timenow=time.strftime('%Y-%m-%d',time.localtime())
        collector=Collector(name=name,phase_error=phase_error,current_error=current_error,rated_primary_current=cjqtest_current,light_power=light_power,
                            composite_error=composite_error,ref=ref,foct_id=1
                            )
        collector.save()

    if username=='':
        content={"login":'登录',
                 "logout":"注销"
                 }
    else:
        content={"login":username,
                 "logout":"注销"
                 }
    return render(request,'foctapp/cjq.html',content)
def fsj_test(request):
    if request.method =='POST':
        name=request.POST.get('fsjtest_name')
        fsjtest_number=request.POST.get('fsjtest_number')
        fsj_reflectivity=request.POST.get('fsj_reflectivity')
        fsj_lenth=request.POST.get('fsj_lenth')
        fsj_project=request.POST.get('fsj_project')
        Inputproducter=request.POST.get('Inputproducter')
        Inputrecorder=request.POST.get('Inputrecorder')
        photo=request.FILES.get('image')
        timenow=time.strftime('%Y-%m-%d',time.localtime())
        fsj=Mirror(name=name,fsj_number=fsjtest_number,
                                         fsj_lenth=fsj_lenth,reflectivity=fsj_reflectivity,fsj_testproject=fsj_project,
                                         fsj_producter=Inputproducter,fsj_recoder=Inputrecorder,current_error=photo,
                                         )
        fsj.save()
    return render(request,'foctapp/fsj.html')

#数据处理

def connected(request):
    a=[]
    foct_collector=Collector.objects.filter(foct__name__exact='1')
    for i in foct_collector:
        a.append(i.light_power)
    return HttpResponse(json.dumps(a),content_type='application/json')


@csrf_exempt
def fsj_qurry(request):
    if request.method =='POST':
        data_raw=request.POST.get('fsj')
        kwargs={}
        fsj_l_1=re.search(r'1m以下',data_raw) is not None and  True or None
        fsj_l_2=re.search(r'1m-2m',data_raw) is not None and True or None
        fsj_l_3=re.search(r'2m以上',data_raw) is not None and True or None
        fsj_r_1=re.search(r'95%以上',data_raw) is not None and True or None
        fsj_r_2=re.search(r'90%-95%',data_raw) is not None and True or None
        fsj_r_3=re.search(r'90%以下',data_raw) is not None and True or None
        timenow=time.strftime('%Y-%m-%d',time.localtime())
        time_month=time.strftime('%m',time.localtime())
        time_year=time.strftime('%Y',time.localtime())
        fsj_d_1=re.search(r'本日',data_raw) is not None and True or None
        fsj_d_2=re.search(r'本月',data_raw) is not None and True or None
        fsj_d_3=re.search(r'本年度',data_raw) is not None and True or None
        if fsj_l_1 is True:
            kwargs['fsj_lenth__lt']=1
        if fsj_l_2 is True:
            kwargs['fsj_lenth__gte']=1
            kwargs['fsj_lenth__lte']=2
        if fsj_l_3 is True:
            kwargs['fsj_lenth__gt']=2
        if fsj_r_1 is True:
            kwargs['reflectivity__gt']=95
        if fsj_r_2 is True:
            kwargs['reflectivity__gte']=90
            kwargs['reflectivity__lte']=95
        if fsj_r_3 is True:
            kwargs['reflectivity__lt']=90
        if fsj_d_1 is True:
            kwargs['test_time']=timenow
        if fsj_d_2 is True:
            kwargs['test_time__month']=time_month
        if fsj_d_3 is True:
            kwargs['test_time__year']=time_year
        results=Mirror.objects.filter(Q(id__gte=1),**kwargs)
    return render(request,'foctapp/index.html',context=results)
@csrf_exempt
def statistics(request):
    modelmap=['反射镜','采集器']
    mirrormap=[['反射率','reflectivity'],['反射镜实际长度','fsj_lenth']]
    if request.method=='POST':
        fsj_statistics_data=request.POST.get('fsj_statistics')
        search_data=fsj_statistics_data.split(' ')[0:2]
        for k in mirrormap:
            if k[0]==search_data[1]:
                search_y=k[1]
        for i in modelmap:
            if i ==search_data[0]:
                fsj_y_list=[]
                fsj_model={}
                results=Mirror.objects.all()
                fsj_y=results.values_list(search_y)
                fsj_data=results.values_list('name','reflectivity','fsj_lenth','fsj_number')
                for y in fsj_y:
                    fsj_y_list.append(y[0])
                for i,data in enumerate(fsj_data):
                    fsj_model['r'+str(i)]=list(data)
                content={'chart_y':fsj_y_list,
                         'chart_point':fsj_model
                         }
                return JsonResponse(content,safe=False)
    return render(request,'foctapp/data_statistics.html')


#序列化
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class Collector_list(generics.ListCreateAPIView):
    queryset=Collector.objects.all()
    serializer_class=CollectorSerializer
class CollectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collector.objects.all()
    serializer_class = CollectorSerializer
class Mirror_list(generics.ListCreateAPIView):
    queryset=Mirror.objects.all()
    serializer_class=MirrorSerializer
class MirrorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mirror.objects.all()
    serializer_class = MirrorSerializer
