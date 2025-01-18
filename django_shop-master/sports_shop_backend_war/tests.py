import datetime
from django.test import TestCase
# 实体类
from models import User
from models import Order
from models import Shopping_cart
from models import Good
from models import Comment
# from entity.User import User
# from entity.Order import Order
# from entity.Shopping_cart import Shopping_cart
# from entity.Good import Good
# from entity.Comment import Comment
# from entity.Mini_entity import Mini_Shopping_cart
# MySQL连接工具测试
# from  dao.MysqlHelper import Mysql_Static_Factory
from  dao import Mysql_Static_Factory
# dao数据访问测试
# from dao.UserDao import UserDaoImpl
# from dao.Shopping_cartDao import Shopping_cartDaoImpl
# from dao.OrderDao import OrderDaoImpl
# from dao.GoodsDao import GoodsDaoImpl
# from dao.CommentDao import CommentDaoImpl
from dao import UserDaoImpl
from dao import Shopping_cartDaoImpl
from dao import OrderDaoImpl
from dao import GoodsDaoImpl
from dao import CommentDaoImpl
# Create your tests here.


# +++++++++++++++++++++++++ |实体类测试|++++++++++++++++++++++++++++++++
my_date = datetime.datetime.strptime("2024-09-26", "%Y-%m-%d")
myUser = User(1,'admin','123',1,"vip","kk",100,"http://127.0.0.1:8080/user.jpg","这个人很懒，什么都没有留下")
myComment = Comment(1,my_date,'哈哈哈',2,3,'admin',4)
myGood = Good(1,'admin',27,"http://127.jpghttp://127.jpg",'啥也没留下')
myOrder = Order(93,my_date,1,1,1,'kk',1,'xiaomi',27,"http://127.0.0.1:8080/user.jpg",'啥也没有','哎哟，不错哦')
myShopping_cart = Shopping_cart(1,2,3,4,'admin',5,"http://12.jpg","啥也没留下",6,'admin')

# print(myUser.__str__())
# print(myComment.__str__())
# print(myGood.__str__())
# print(myShopping_cart.__str__())
# print(myOrder.__str__())


'''==================|MySQL连接工具|========================'''
# conn = Mysql_Static_Factory.get_connection()
# cur = conn.cursor()
# print(conn)
# print(cur)
# conn.close()
# cur.close()


'''====================|dao数据访问|========================='''


'''--------------------UserDaoImpl测试-----------------------'''
# print(UserDaoImpl().selectByNamePWD('海边的小海鸥','123456'))
# print(UserDaoImpl().selectByID(9).__str__())
# print(UserDaoImpl().inserUser(myUser))
# print(UserDaoImpl().selectWalletByUserId(1))
# print(UserDaoImpl().updateUserWallet(6,1300))


'''--------------Shopping_cartDaoImpl测试-------------------'''
# print(Shopping_cartDaoImpl().insertGoodTOCart(myShopping_cart))

# print(Shopping_cartDaoImpl().selectReturnInfo(1,4).__str__())

# list_shop = Shopping_cartDaoImpl().selectAllShopCartByUserId(1)
# for shop in list_shop:
#     print(shop.__str__())

# print(Shopping_cartDaoImpl().deleteById(100))

# orders = OrderDaoImpl().selectOrderByUserId(1)
# for order in orders:
#     print(order.__str__())
# print(OrderDaoImpl().addOrderBySingleShopCart(myOrder))
# print(myOrder.__str__())
# print(OrderDaoImpl().updateOrderSays(myOrder))

# print(OrderDaoImpl().deleteOrderById(92))


'''--------------GoodDaoImpl测试-------------------'''
# list_goods = GoodsDaoImpl().selectGoodList()
# for good in list_goods:
#     print(good.__str__())
# print(GoodsDaoImpl().selectGoodByGoodId(1).__str__())


'''--------------CommentDaoImpl测试-------------------'''
# print(CommentDaoImpl().addComment(myComment))

# comments = CommentDaoImpl().selectCommentByGoodId(1)
# for comment in comments:
#     print(comment.__str__())

# print(CommentDaoImpl().selectHasCommentByOrderId(3))

# print(CommentDaoImpl().updateSaysByOrderId(4,"超级棒，一定要买啊"))