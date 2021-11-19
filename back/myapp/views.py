import json
from django.http import JsonResponse, FileResponse, StreamingHttpResponse,HttpResponse
from myapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
# Create your views here.

def login(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        username = data_json.get('userName')
        password = data_json.get('userPassword')
        user = User.objects.filter(user_name=username)
        if len(user) == 0:
            return JsonResponse({'success': False, 'message': '用户不存在'})
        if len(user) > 0:
            if (user[0]).user_password == password:
                return JsonResponse({'success': True, 'message': '登录成功', 'userID': user[0].user_id})
            else:
                return JsonResponse({'success': False, 'message': '密码错误', 'userID': user[0].user_id})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})

def register(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        new_name = data_json.get('userName')
        new_pwd = data_json.get('userPassword')
        new_nickname = data_json.get('userNickname')
        new_tel = data_json.get('userTel')
        new_address = data_json.get('userAddress')
        if new_name is None:
            return JsonResponse({'success': False, 'message': '未输入'})
        else:
            space = User.objects.filter(user_name=new_name)
            if len(space) > 0:
                return JsonResponse({'success': False, 'message': '用户名已存在'})
            else:
                new_user = User()
                new_user.user_name = new_name
                new_user.user_password= new_pwd
                new_user.user_nickname = new_nickname
                new_user.user_tel = new_tel
                new_user.user_address = new_address
                new_user.save()
                return JsonResponse({'success': True, 'message': '注册成功','userID': new_user.user_id})

    else:
        JsonResponse({'success': False, 'message': '请求异常'})




