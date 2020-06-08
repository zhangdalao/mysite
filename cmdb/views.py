from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your views here.

def index(requset):
    return HttpResponse('Index')


# def login(request):
#     #包含用户提交的所有信息
#
#     #获取用户提交方法
#     #print(request.method)
#
#     error_msg = ''
#     if request.method == 'POST':
#         #获取用户通过post提交的数据
#         user = request.POST.get('user',None)
#         pwd = request.POST.get('pwd',None)
#         if user == 'root' and pwd =='123':
#             #跳转到指定
#             return redirect('http://www.baidu.com')
#         # user = request.POST['user']
#         # pwd = request.POST['pwd']
#         #print(user,pwd)
#         else:
#             #用户名密码不匹配
#             error_msg = '用户名或密码错误'
#
#     return render(request,'login.html',{'error_msg':error_msg})  #再定义一个字典 把html里面替换为error_msg

def login(request):
    # 包含用户提交的所有信息

    # 获取用户提交方法
    # print(request.method)
    # g = request.POST.get('gender')
    # print(g)
    # f = request.POST.getlist('favor')
    # print(f)
    # c = request.POST.getlist('city')
    # print(c)
    if request.method == "POST":

        obj = request.FILES.get('fafafa')
        #print(obj,type(obj),obj.name)

        file_path = os.path.join('upload', obj.name)
        f = open(file_path,'wb')
        for item in obj.chunks():
            f.write(item)
        f.close()
        return render(request, 'login.html')
    elif request.method == "GET":
        return render(request,'login.html')