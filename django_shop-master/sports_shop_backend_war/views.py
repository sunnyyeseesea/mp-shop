# 强制设置CSRF令牌cookie
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import datetime
# 用于图片上传的路径定位
import os
'''
   ---------------------------------------------------
   -优雅的程序员，优雅的编码，优雅的注释，优雅太优雅了-
   --------------------现在---------------------------
   --------------开始优雅的阅读源码吧-----------------
   -移动你可爱的鼠标,停留在包、类、方法上,即可查看含义-
   ---------------------------------------------------
'''
# bean实体类
from .models import User
from .models import Order
from .models import Shopping_cart
from .models import Good
from .models import Comment
from .models import Meta
from .models import Mini_Shopping_cart
# dao数据访问层
from .dao import Mysql_Static_Factory
from .dao import UserDaoImpl
from .dao import Shopping_cartDaoImpl
from .dao import OrderDaoImpl
from .dao import GoodsDaoImpl
from .dao import CommentDaoImpl
# service服务层
from .service import UserService
# 以下乃 control控制层(当然记得带上咱urls.py小弟)

def index(request):
    return HttpResponse('欢迎测试')

# 1、登录验证
def login(request):

    username = request.GET.get('username')
    password = request.GET.get('password')
    
    return HttpResponse(UserService().login(username,password),content_type="application/json")


# 2、注册用户
def CreateUser(request):

    # 获取前端传递过来的数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    user_picture = request.GET.get('user_picture')
    type = request.GET.get('type')

    user = User(0,username,password,1,'vip',type,1000,user_picture,"这个人很懒，什么都没有留下")
    print(user.__str__)
    userDaoImpl = UserDaoImpl()

    isok = False
    # 尝试添加用户
    try:
        isok = userDaoImpl.inserUser(user)
    except Exception as e:
        print('创建用户失败')
        print(e)
        
    meta = Meta

    # 创建成功，收集用户数据准备返回给前端
    if isok:
        user_id = userDaoImpl.selectByNamePWD(username,password)
        data = userDaoImpl.selectByID(user_id)
        meta = Meta('添加用户成功',201)

        response = { 
            'data': data,
            'meta': meta
        }

        json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (User, Meta)) else None, ensure_ascii=False)
        return HttpResponse(json_str,content_type="application/json")
    # 创建失败，制作假数据，并且设置meta
    else:
        meta = Meta('添加用户失败',200)
        response = {
            'fackUser': User,
            'meta': meta
        }
        json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (User, Meta)) else None, ensure_ascii=False)
        return HttpResponse(json_str,content_type="application/json")


# 3、获取商品数据
def getAllGoods(request):
    # 直接查询所以商品记录
    goodDao = GoodsDaoImpl()
    data = goodDao.selectGoodList()
    meta = Meta('获取商品数据成功',200)
    response = {
            'data': data,
            'meta': meta
        }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (Good, Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 4、查看指定商品的详细信息
def getGoodAndComment(request):
    # 获取商品ID
    goods_id = request.GET.get('goods_id')
    # 获取商品数据
    good = GoodsDaoImpl().selectGoodByGoodId(goods_id)
    # 获取该商品的评论数据
    comments = CommentDaoImpl().selectCommentByGoodId(goods_id)

    # 制作返回数据
    data = {
        'comment':comments,
        'goods_describe':good.goods_describe,
        'goods_id':good.goods_id,
        'goods_name':good.goods_name,
        'goods_picture':good.goods_picture,
        'goods_price':good.goods_price
    }
    meta = Meta('获取商品信息成功',200)
    response = {
            'data': data,
            'meta': meta
        }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (Comment, Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 5、添加购物车数据结算成订单
def addShopCartToOrders(request):
    # 获取前端传送过来的数据
    shopping_count = request.GET.get('shopping_count')
    shopping_amount = request.GET.get('shopping_amount')
    goods_id = request.GET.get('goods_id')
    goods_name = request.GET.get('goods_name')
    goods_price = request.GET.get('goods_price')
    goods_picture = request.GET.get('goods_picture')
    goods_describe = request.GET.get('goods_describe')
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')

    # 创建一个购物车对象，对应一条记录
    shopping_cart = Shopping_cart(0,shopping_count,shopping_amount,goods_id,goods_name,goods_price,goods_picture,goods_describe,user_id,username)
    # 插入一条购物车记录
    insertCartFlag = Shopping_cartDaoImpl().insertGoodTOCart(shopping_cart)
    # 根据商品id和用户id获取购物车信息，以此作为data
    data = Shopping_cartDaoImpl().selectReturnInfo(shopping_cart.goods_id,shopping_cart.user_id)
    meta = Meta('添加购物车成功',200)
    response = {
            'data': data,
            'meta': meta
        }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (Mini_Shopping_cart, Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 6、结算购物车数据成订单
def settlement(request):
    # 接收前端发送过来的数据
    orderCount = request.GET.get('order_count')
    orderAmount = request.GET.get('order_amount')
    userID = request.GET.get('user_id')
    username = request.GET.get('username')
    goodId = request.GET.get('goods_id')
    goodName = request.GET.get('goods_name')
    goodPrice = request.GET.get('goods_price')
    goodPicture = request.GET.get('goods_picture')
    goodDescribe = request.GET.get('goods_describe')
    order_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # 创建order对象 对应一条记录
    
    order = Order(0,order_time,orderCount,orderAmount,userID,username,goodId,goodName,goodPrice,goodPicture,goodDescribe,'没有评价')
    # print(order.__str__)
    # 生成订单记录
    flagAdd = OrderDaoImpl().insertCartToOder(order)
    data = {}
    meta = Meta
    if flagAdd:
        data = {
            'thanks':'没有别的意思，谢谢老板'
        }
        meta = Meta('结算商品成功',201)
    else:
        meta = Meta('结算商品失败',200)
    response = {
            'data': data,
            'meta': meta
        }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 7、获取用户对应的订单数据
def getOrdersByUserID(request):
    # 获取前端发送过来的数据
    user_id = request.GET.get('user_id')
    # 调用OrderDao的方法获取对应订单
    orders = OrderDaoImpl().selectOrderByUserId(user_id)
    meta = Meta('获取商品信息成功',200)

    response = {
            'data': orders,
            'meta': meta
        }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (Order,Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 8、添加商品评论信息
def addComment(request):
    # 获取前端传送过来的数据
    says = request.GET.get('says')
    goods_id = request.GET.get('goods_id')
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')
    order_id = request.GET.get('order_id')
    says_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # 创建评论对象，对应一条记录
    comment = Comment(0,says_time,says,goods_id,user_id,username,order_id)
    # 调用addComment方法，添加一条评论
    flag = CommentDaoImpl().addComment(comment)
    data = ''
    meta = Meta

    if flag:
        data = says
        meta = Meta('添加评论成功',200)
    else:
        data = '添加评论失败'
        meta = Meta('添加评论失败',500)
    
    response = {
            'data': data,
            'meta': meta
        }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 9、获取个人信息
def getUserInfo(request):
    # 获取前端发送过来的数据
    user_id = request.GET.get('user_id')
    # 调用UserDao的方法获取用户信息
    userinfo = UserDaoImpl().selectByID(user_id)
    meta = Meta('获取用户信息成功',200)

    response = {
            'data': userinfo,
            'meta': meta
        }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (User,Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 10、user_id获取购物车数据 获取用户相关购物车
def getShopCartById(request):
    # 获取前端发送过来的数据
    user_id = request.GET.get('user_id')
    # 调用UserDao的方法获取用户信息
    shopping_carts = Shopping_cartDaoImpl().selectAllShopCartByUserId(user_id)
    meta = Meta('获取用户相关购物车成功',200)

    response = {
            'data': shopping_carts,
            'meta': meta
        }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (Shopping_cart,Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 11、购物车单独结算
def simpleBuy(request):
    # 获取前端传送过来的数据
    goods_id = request.GET.get('goods_id')
    goods_name = request.GET.get('goods_name')
    goods_picture = request.GET.get('goods_picture')
    goods_price = request.GET.get('goods_price')
    shopping_amount = request.GET.get('shopping_amount')
    shopping_cart_id = request.GET.get('shopping_cart_id')
    shopping_count = request.GET.get('shopping_count')
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')
    goods_describe = request.GET.get('goods_describe')
    order_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # 制作order对象，对应一条记录
    order = Order(0,order_time,shopping_count,shopping_amount,user_id,username,goods_id,goods_name,goods_price,goods_picture,goods_describe,'买家未作出评价')
    # 执行OrderDao 添加一条记录
    flag = OrderDaoImpl().addOrderBySingleShopCart(order)
    # 此变量用于判断是否走完整个流程
    userFlag = False
    # 成功添加订单记录。 进一步操作shoping_cartDao 通过id号删除记录
    if flag:
        # 根据购物车id删除购物车记录
        deleteFlag = Shopping_cartDaoImpl().deleteById(shopping_cart_id)
        # 根据用户id获取用户余额
        have_money = UserDaoImpl().selectWalletByUserId(user_id)
        # 现有金额扣除商品总价
        wallet = have_money - eval(shopping_amount)
        # 根据用户ID和订单总金额修改用户钱包余额
        userFlag = UserDaoImpl().updateUserWallet(user_id,wallet)
    # 走完整个流程
    meta = Meta
    if userFlag:
        meta = Meta('购买成功。1、添加订单记录2、删除购物车记录3、扣除用户金额',200)
    else:
        meta = Meta('购买失败',500)
    
    # response = {
    #         'meta': meta
    #     }
    json_str = json.dumps(meta, default=lambda o: o.__json__() if isinstance(o, (Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 12、修改评论数据（订单表和评论表）
def updateOrderSays(request):
    # 接收前端传递过来的数据
    order_id = request.GET.get('order_id')
    says = request.GET.get('says')
    goods_id = request.GET.get('goods_id')
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # 生成Order对象 对应一条记录
    order = Order(order_id,now_time,0,0,0,'cloud',0,'cloud',0,0,'no descibe',says)
    # 生成Comment对象 对应一条记录
    comment = Comment(0,now_time,says,goods_id,user_id,username,order_id)

    # 写这里 提升meta作用域
    meta = Meta
    # 修改order表的评论数据
    orderFlag = OrderDaoImpl().updateOrderSays(order)

    # 修改order数据成功，继续操作comment表
    if orderFlag:
        hasCommentDataFlag = CommentDaoImpl().selectHasCommentByOrderId(order_id)

        # 有数据，进行update操作
        if hasCommentDataFlag:
            updateStatus = CommentDaoImpl().updateSaysByOrderId(order_id,says)

            # 根据结果制作返回数据
            if updateStatus:
                meta = Meta('修改order表says成功，修改comment表says成功',200)
            else:
                meta = Meta('修改order表says成功，修改comment表says失败',500)

        # 没有数据为comment表新增一条数据
        else:

            addStatus = CommentDaoImpl().addComment(comment)

            if addStatus:
                meta = Meta('修改order表says成功，修改comment表says成功',200)
            else:
                meta = Meta('修改order表says成功，修改comment表says失败',500)
    # 第一步 修改订单评论就失败的响应
    else:
            meta = Meta('修改评论数据失败——order表Update【可能是says评论数据与以往一样】',500)
    # response = {
    #         'meta': meta
    # }

    json_str = json.dumps(meta, default=lambda o: o.__json__() if isinstance(o, (Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 13、删除单条 订单记录
def deleteOrdersById(request):
    # 获取前端传递过来的数据
    order_id = request.GET.get('order_id')
    # 通过OrderDao 利用order_id 对表中记录进行删除
    flag = OrderDaoImpl().deleteOrderById(order_id)
    meta = Meta
    # 删除成功
    if flag:
        meta = Meta('订单号：{}，该记录删除成功'.format(order_id),200)
    else:
        meta = Meta('订单号：{}，该记录删除失败'.format(order_id),500)
    
    # response = {
    #         'meta': meta
    # }

    json_str = json.dumps(meta, default=lambda o: o.__json__() if isinstance(o, (Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 14、删除单条 购物车 记录
def deleteShoppingCartById(request):
    # 获取前端传递过来的数据
    shopping_cart_id = request.GET.get('shopping_cart_id')
    # 通过OrderDao 利用order_id 对表中记录进行删除
    flag = Shopping_cartDaoImpl().deleteById(shopping_cart_id)
    meta = Meta
    # 删除成功
    if flag:
        meta = Meta('购物车号：{}，该记录删除成功'.format(shopping_cart_id),200)
    else:
        meta = Meta('购物车号：{}，该记录删除失败'.format(shopping_cart_id),500)
    
    # response = {
    #         'meta': meta
    # }

    json_str = json.dumps(meta, default=lambda o: o.__json__() if isinstance(o, (Meta)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")


# 15 上传用户头像 http://127.0.0.1:8888/static/picture/xXxX.jpg
def UserPicture(request):
    if request.method == 'POST':
        fileName = request.FILES.get('file').name
        # 当前脚本的绝对路径
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        upload_path = BASE_DIR + '/static/picture/'+fileName
        
        fileData = request.FILES.get('file').read()
        with open(upload_path, "wb+") as f:
            f.write(fileData)

    # do something else with the image if needed
    response = {
    'img': "http://127.0.0.1:8888/static/picture/"+fileName
    }
    json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (str)) else None, ensure_ascii=False)
    return HttpResponse(json_str,content_type="application/json")