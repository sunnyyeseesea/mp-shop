# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),# 1、登录验证
    path("CreateUser", views.CreateUser, name="CreateUser"),# 2、注册用户
    path("getAllGoods", views.getAllGoods, name="getAllGoods"),# 3、获取商品数据
    path("getGoodAndComment", views.getGoodAndComment, name="getGoodAndComment"),# 4、查看指定商品的详细信息
    path("addShopCartToOrders", views.addShopCartToOrders, name="addShopCartToOrders"),# 5、添加购物车数据结算成订单
    path("settlement", views.settlement, name="settlement"),# 6、结算购物车数据成订单
    path("getOrdersByUserID", views.getOrdersByUserID, name="getOrdersByUserID"),# 7、获取用户对应的订单数据
    path("addComment", views.addComment, name="addComment"),# 8、添加商品评论信息
    path("getUserInfo", views.getUserInfo, name="getUserInfo"),# 9、获取个人信息
    path("getShopCartById", views.getShopCartById, name="getShopCartById"),# 10、user_id获取购物车数据
    path("simpleBuy", views.simpleBuy, name="simpleBuy"),# 11、购物车单独结算
    path("updateOrderSays", views.updateOrderSays, name="updateOrderSays"),# 12、修改评论数据（订单表和评论表）
    path("deleteOrdersById", views.deleteOrdersById, name="deleteOrdersById"),# 13、删除单条 订单记录
    path("deleteShoppingCartById", views.deleteShoppingCartById, name="deleteShoppingCartById"),# 14、删除单条 购物车 记录
    path("UserPicture", views.UserPicture, name="UserPicture")# 15、上传用户头像
]