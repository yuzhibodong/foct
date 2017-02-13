from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import UserSerializer,GroupSerializer
from django.http import HttpResponse,HttpResponseRedirect
from .models import Collector
from .serializers import CollectorSerializer
from django.http import JsonResponse
from rest_framework import mixins,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth import authenticate,login
import time

#auth界面视图

def my_view(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return render(request,'foctapp/index.html')
        else:
            return HttpResponse("disable account")
    else:
        return  HttpResponse('invalid login')

def home(request):
    return render(request,'foctapp/home.html')




# 数据处理视图.
def index(request):
    return render(request,'foctapp/index.html')
def cjq_test(request):
    if request.method == 'POST':
        name=request.POST.get('cjqtest_name')
        phase_error=request.POST.get('cjqtest_phaseerror')
        current_error=request.POST.get('cjqtest_currenterror')
        cjqtest_current=request.POST.get('cjqtest_current')
        light_power=request.POST.get('cjqtest_lightpower')
        ref=request.POST.get('cjqtest_ref')
        composite_error=request.POST.get('cjqtest_Inputcomposite_error')
        timenow=time.strftime('%Y-%m-%d',time.localtime())
        collector=Collector(name=name,phase_error=phase_error,current_error=current_error,rated_primary_current=cjqtest_current,light_power=light_power,
                            composite_error=composite_error,ref=ref,foct_id=1,test_time=timenow
                            )
        collector.save()
    return render(request,'foctapp/cjq_test.html')

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
