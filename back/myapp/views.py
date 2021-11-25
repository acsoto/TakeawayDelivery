import json
from django.http import JsonResponse, FileResponse, StreamingHttpResponse, HttpResponse
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
                new_user.user_password = new_pwd
                new_user.user_nickname = new_nickname
                new_user.user_tel = new_tel
                new_user.user_address = new_address
                new_user.save()
                return JsonResponse({'success': True, 'message': '注册成功', 'userID': new_user.user_id})

    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def getOrders(user):
    orders = Order.objects.filter(order_user_id=user.user_id)
    orders_json = []
    for order in orders:
        order_json = {"orderCompleted": order.order_completed,
                      "deliveryUserName": order.delivery_user.user_name
                      }
        foods_json = []
        order_foods = OrderFood.objects.filter(order_id=order.order_id)
        count = 0
        for order_food in order_foods:
            food = order_food.food
            food_num = order_food.food_num
            count += food.food_price * food_num
            food_json = {
                "foodName": food.food_name,
                "foodPrice": food.food_price,
                "foodUrl": food.food_url,
                "foodNum": food_num
            }
            foods_json.append(food_json)
        order_json["food"] = foods_json
        order_json['totalPrice'] = count
        orders_json.append(order_json)
    return orders_json


def getStars(user):
    stars = Star.objects.filter(user_id=user.user_id)
    stars_json = []
    for star in stars:
        star_foods = StarFood.objects.filter(star_id=star.star_id)
        for star_food in star_foods:
            food = star_food.food
            food_json = {
                "foodName": food.food_name,
                "foodPrice": food.food_price,
                "foodUrl": food.food_url
            }
            stars_json.append(food_json)
    return stars_json


def getInformation(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        user = User.objects.get(user_id=user_id)
        orders = getOrders(user)
        stars = getStars(user)
        return JsonResponse({'success': True,
                             'message': '查询成功',
                             'userName': user.user_name,
                             'userNickName': user.user_nickname,
                             'userAddress': user.user_address,
                             'userTel': user.user_tel,
                             'userOrders': orders,
                             'userStars': stars
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def changeInformation(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        user = User.objects.get(user_id=user_id)
        user.user_nickname = data_json.get('userNickName')
        user.user_tel = data_json.get('userTel')
        user.user_address = data_json.get('userAddress')
        user.save()
        return JsonResponse({'success': True, 'message': '修改成功'})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def changePassword(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        user = User.objects.get(user_id=user_id)
        user.user_password = data_json.get('userPassword')
        user.save()
        return JsonResponse({'success': True, 'message': '修改成功'})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def getStoreInformation(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        store_id = data_json.get('storeID')
        store = Store.objects.get(store_id=store_id)
        food_json = []
        foods = Food.objects.filter(store_id=store_id)
        for food in foods:
            food_json.append({
                "foodName": food.food_name,
                "foodPrice": food.food_price,
                "foodUrl": food.food_url
            })
        return JsonResponse({'success': True,
                             'message': '查询成功',
                             'storeName': store.store_name,
                             'storeAddress': store.store_address,
                             'storeTel': store.store_tel,
                             'food': food_json
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def deleteUser(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        User.objects.get(user_id=user_id).delete()
        return JsonResponse({'success': True, 'message': '注销成功'})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def getEvaluateAboutFood(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        food_id = data_json.get('foodID')
        food_evaluate_json = []
        food_evaluates = FoodEvaluate.objects.filter(food_id=food_id)
        for evaluate in food_evaluates:
            food_evaluate_json.append({
                'evaluateText': evaluate.food_evaluate_text,
                'evaluateScore': evaluate.food_evaluate_score
            })
        return JsonResponse({'success': True, 'message': '注销成功',
                             'foodEvaluate': food_evaluate_json})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def getEvaluateAboutUser(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        user_evaluate_json = []
        user_evaluates = UserEvaluate.objects.filter(user_id=user_id)
        for evaluate in user_evaluates:
            user_evaluate_json.append({
                'evaluateText': evaluate.food_evaluate_text,
                'evaluateScore': evaluate.food_evaluate_score
            })
        return JsonResponse({'success': True, 'message': '注销成功',
                             'userEvaluate': user_evaluate_json})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})
