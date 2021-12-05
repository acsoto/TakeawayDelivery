import datetime
import json

from django.http import JsonResponse

from myapp.models import *


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
                new_user.user_icon_url = "https://img0.baidu.com/it/u=3730772664,138405132&fm=26&fmt=auto"
                new_user.save()
                return JsonResponse({'success': True, 'message': '注册成功', 'userID': new_user.user_id})

    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def fill_order_json(orders):
    orders_json = []
    for order in orders:
        order_json = {}
        if order.delivery_user:
            order_json["deliveryUserNickName"] = order.delivery_user.user_nickname
            order_json["deliveryUserTel"] = order.delivery_user.user_tel
            order_json["deliveryUserIcon"] = order.delivery_user.user_icon_url
            order_json["deliveryUserAddress"] = order.delivery_user.user_address
        else:
            order_json["orderUserNickName"] = ""
            order_json["orderUserTel"] = ""
            order_json["orderUserIcon"] = ""
            order_json["deliveryUserAddress"] = ""
        if order.order_user:
            order_json["orderUserNickName"] = order.order_user.user_nickname
            order_json["orderUserTel"] = order.order_user.user_tel
            order_json["orderUserIcon"] = order.order_user.user_icon_url
            order_json["orderUserAddress"] = order.order_user.user_address
        else:
            order_json["orderUserNickName"] = ""
            order_json["orderUserTel"] = ""
            order_json["orderUserIcon"] = ""
            order_json["orderUserAddress"] = ""
        foods_json = []
        order_foods = OrderFood.objects.filter(order_id=order.order_id)
        count = 0
        for order_food in order_foods:
            food = order_food.food
            food_num = order_food.food_num
            count += food.food_price * food_num
            food_json = {
                "foodID": food.food_id,
                "foodName": food.food_name,
                "foodPrice": food.food_price,
                "foodUrl": food.food_url,
                "foodNum": food_num
            }
            foods_json.append(food_json)
            order_json["storeName"] = food.store.store_name
            order_json["storeID"] = food.store.store_id
        order_json["orderID"] = order.order_id
        order_json["orderDate"] = order.order_date.strftime('%Y-%m-%d %H:%M:%S')
        order_json["orderCompleted"] = order.order_completed
        order_json["food"] = foods_json
        order_json['totalPrice'] = count
        orders_json.append(order_json)
    return orders_json


def get_orders(user, is_delivery):
    if is_delivery:
        orders = Order.objects.filter(delivery_user_id=user.user_id).order_by('-order_date')
    else:
        orders = Order.objects.filter(order_user_id=user.user_id).order_by('-order_date')
    return fill_order_json(orders)


def get_all_orders(request):
    if request.method == 'POST':
        orders = Order.objects.filter(order_completed=0).order_by('order_date')
        orders_json = fill_order_json(orders)
        return JsonResponse({'success': True,
                             'message': '获取成功',
                             'orders': orders_json,
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def finish_order(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        order_id = data_json.get('orderID')
        Order.objects.filter(order_id=order_id).update(order_completed=2)
        return JsonResponse({'success': True,
                             'message': '配送完成',
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def take_order(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        order_id = data_json.get('orderID')
        user_id = data_json.get('userID')
        delivery_user = User.objects.get(user_id=user_id)
        order = Order.objects.get(order_id=order_id)
        order.order_completed = 1
        order.delivery_user = delivery_user
        order.save()
        return JsonResponse({'success': True,
                             'message': '接下订单',
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def set_orders(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        food_list = data_json.get('foodList')
        order = Order(order_completed=0, order_user_id=user_id, order_date=datetime.datetime.now())
        order.save()

        for food in food_list:
            if food.get('foodNum') and food.get('foodNum') > 0:
                food_order = OrderFood(food_id=food.get('foodID'), order_id=order.order_id,
                                       food_num=food.get('foodNum'))
                food_order.save()
        return JsonResponse({'success': True,
                             'message': '下单成功',
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def get_stars(user):
    stars = Star.objects.filter(user_id=user.user_id)
    stars_json = []
    for star in stars:
        star_foods = StarFood.objects.filter(star_id=star.star_id)
        for star_food in star_foods:
            food = star_food.food
            food_json = {
                "foodID": food.food_id,
                "foodName": food.food_name,
                "foodPrice": food.food_price,
                "foodUrl": food.food_url
            }
            stars_json.append(food_json)
    return stars_json


def un_star(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        food_id = data_json.get('foodID')
        stars = Star.objects.filter(user_id=user_id)
        for star in stars:
            StarFood.objects.filter(star_id=star.star_id, food__food_id=food_id).delete()
        return JsonResponse({'success': True,
                             'message': '取消收藏成功',
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def get_information(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        user = User.objects.get(user_id=user_id)
        orders1 = get_orders(user, False)
        orders2 = get_orders(user, True)
        stars = get_stars(user)
        return JsonResponse({'success': True,
                             'message': '查询成功',
                             'userName': user.user_name,
                             'userNickName': user.user_nickname,
                             'userAddress': user.user_address,
                             'userTel': user.user_tel,
                             'userOrders': orders1,
                             'userDeliveryOrders': orders2,
                             'userStars': stars,
                             'userIconUrl': user.user_icon_url,
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def change_information(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        user = User.objects.get(user_id=user_id)
        user.user_nickname = data_json.get('userNickName')
        user.user_tel = data_json.get('userTel')
        user.user_address = data_json.get('userAddress')
        user.user_icon_url = data_json.get('userIconUrl')
        user.save()
        return JsonResponse({'success': True, 'message': '修改成功'})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def change_password(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        user = User.objects.get(user_id=user_id)
        if user.user_password != data_json.get('userOldPassword'):
            return JsonResponse({'success': False, 'message': '原密码错误'})
        user.user_password = data_json.get('userPassword')
        user.save()
        return JsonResponse({'success': True, 'message': '修改成功'})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def get_stores(request):
    if request.method == 'POST':

        stores = Store.objects.filter()
        store_json = []
        for store in stores:
            food_json = []
            foods = Food.objects.filter(store_id=store.store_id)
            score = 0
            count = 0
            three_foods = Food.objects.filter(store_id=store.store_id)[:3]
            for food in three_foods:
                food_json.append({
                    "foodID": food.food_id,
                    "foodName": food.food_name,
                    "foodPrice": food.food_price,
                    "foodUrl": food.food_url
                })
            for food in foods:
                evaluates = FoodEvaluate.objects.filter(food__food_id=food.food_id)
                for evaluate in evaluates:
                    count += 1
                    score += evaluate.food_evaluate_score

            if count != 0:
                score = score / count
            store_json.append({
                "storeID": store.store_id,
                "storeName": store.store_name,
                "storeAddress": store.store_address,
                "storeTel": store.store_tel,
                "storeUrl": store.store_url,
                "score": score,
                "count": count,
                "food": food_json,
                "foodSize": three_foods.count(),
            })
        return JsonResponse({'success': True,
                             'message': '查询成功',
                             'store': store_json
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def get_store_information(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        store_id = data_json.get('storeID')
        store = Store.objects.get(store_id=store_id)
        food_json = []
        score = 0
        count = 0
        foods = Food.objects.filter(store_id=store_id)
        for food in foods:
            food_count = 0
            food_score = 0

            evaluates = FoodEvaluate.objects.filter(food__food_id=food.food_id)
            for evaluate in evaluates:
                count += 1
                food_count += 1
                food_score += evaluate.food_evaluate_score
                score += evaluate.food_evaluate_score

            if food_count != 0:
                food_score = food_score / food_count
            food_json.append({
                "foodID": food.food_id,
                "foodName": food.food_name,
                "foodPrice": food.food_price,
                "foodUrl": food.food_url,
                "foodScore": food_score,
                "foodCount": food_count,
            })

        if count != 0:
            score = score / count
        return JsonResponse({'success': True,
                             'message': '查询成功',
                             'storeName': store.store_name,
                             'storeAddress': store.store_address,
                             'storeTel': store.store_tel,
                             "storeUrl": store.store_url,
                             'food': food_json,
                             "score": score,
                             "count": count,
                             })
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def delete_user(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        User.objects.get(user_id=user_id).delete()
        return JsonResponse({'success': True, 'message': '注销成功'})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def get_evaluate_food(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        food_id = data_json.get('foodID')
        user_id = data_json.get('userID')
        user = User.objects.get(user_id=user_id)
        food_evaluate_json = []
        food = Food.objects.get(food_id=food_id)
        food_evaluates = FoodEvaluate.objects.filter(food_id=food_id)
        food_count = 0
        food_score = 0
        has_commented = False
        for evaluate in food_evaluates:
            if evaluate.post_user.user_id == user_id:
                has_commented = True
            food_evaluate_json.append({
                'evaluateText': evaluate.food_evaluate_text,
                'evaluateScore': evaluate.food_evaluate_score,
                'userNickName': evaluate.post_user.user_nickname,
                'userID': evaluate.post_user.user_id,
                'userIconUrl': evaluate.post_user.user_icon_url,
                'evaluateDate': evaluate.food_evaluate_date,
            })
            food_count += 1
            food_score += evaluate.food_evaluate_score
        if food_count != 0:
            food_score = food_score / food_count
        food_json = {
            "hasCommented": has_commented,
            "foodID": food.food_id,
            "foodName": food.food_name,
            "foodPrice": food.food_price,
            "foodUrl": food.food_url,
            "foodScore": food_score,
            "foodCount": food_count,
        }
        comment_json = {
            'evaluateText': "",
            'evaluateScore': None,
            'userNickName': user.user_nickname,
            'userID': user.user_id,
            'userIconUrl': user.user_icon_url,
        }
        return JsonResponse({'success': True, 'message': '获取成功',
                             'foodEvaluate': food_evaluate_json,
                             'food': food_json,
                             'comment': comment_json})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


def get_evaluate_user(request):
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
        return JsonResponse({'success': True, 'message': '获取成功',
                             'userEvaluate': user_evaluate_json})
    else:
        JsonResponse({'success': False, 'message': '请求异常'})


# Android
def android_get_orders(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        user_id = data_json.get('userID')
        user = User.objects.get(user_id=user_id)
        orders = get_orders(user, False)
        return JsonResponse({'success': True, 'message': '请求成功',
                             'orders': orders})
