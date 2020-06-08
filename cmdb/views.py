from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your views here.

# USER_DICT = {
#     'k1':'root1',
#     'k2': 'root2',
#     'k3': 'root3',
#     'k4': 'root4',
# }
USER_DICT = {
    '1':{'name' : 'root1', 'email': 'root@live.com'},
    '2': {'name': 'root2', 'email': 'root@live.com'},
    '3': {'name': 'root3', 'email': 'root@live.com'},
    '4': {'name': 'root4', 'email': 'root@live.com'},

}

def index(requset):
    #return HttpResponse('Index')

    return render(requset,'index.html',{'user_dict':USER_DICT})

def detail(request,nid):
    #return HttpResponse(nid)

    # nid = request.GET.get('nid')
    #
    detail_info = USER_DICT[nid]

    return render(request,'detail.html',{'detail_info':detail_info})


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


from django.views import View
class Home(View):
    def dispatch(self, request, *args, **kwargs):
        # return HttpResponse('ok')
        print('Before')
        result = super(Home,self).dispatch(request, *args, **kwargs)
        print('After')
        return result

    def get(self,request):
        print(request.method)
        return render(request,'home.html')

    def post(self,request):

        self.obj = request.FILES.get('fafa')
        file_path_1 = os.path.join('upload',self.obj.name)
        f = open(file_path_1,'wb')
        for i in self.obj.chunks():
            f.write(i)
        f.close()

        #print(request.method,'POST')
        return render(request,'home.html')