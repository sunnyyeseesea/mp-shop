'''涵盖项目需要使用到的数据访问类,开始CURD吧!'''
import pymysql
# 实体类导包
from .models import User
from .models import Order
from .models import Shopping_cart
from .models import Good
from .models import Comment
from .models import Mini_Shopping_cart

# 数据库访问静态工厂
class Mysql_Static_Factory:
    '''数据库静态工厂 提供如下方法:
    @staticmethod: get_connecttion()
    @return: connection连接对象,供CURD操作
    '''
    @staticmethod
    def get_connection():
        try:
            connection = pymysql.connect(host="localhost",
                                         user='root',
                                         password='123456',
                                         db='sports_shop',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection
        except Exception as e:
            print(e)

# 用户表
class UserDaoImpl:
    '''用户表 数据访问 提供如下方法
       @methoad: selectByNamePWD() 用于登录验证
       @methoad: selectByID() 查询用户的所有数据
       @methoad: inserUser() 添加用户
       @methoad: selectWalletByUserId() 查询用户余额
       @methoad: updateUserWallet() 更新用户余额
    '''
    # 用于登录验证
    def selectByNamePWD (self,username:str, password:str) :
        '''查询是否有该用户
            @param 用户名
            @param 密码
            @return user_id'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        user_id = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "SELECT * FROM users WHERE username = %s AND password = %s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (username, password))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    # 存在该用户密码，登录成功
                    result = cursor.fetchone()
                    user_id = result['user_id']
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return user_id

    # 查询用户的所有数据
    def selectByID (self,user_id:int) :
        '''通过用户ID查询用户信息
            @param 用户ID
            @return 用户实体类'''
        connection = Mysql_Static_Factory.get_connection()
        user = User
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "SELECT * FROM users WHERE user_id = %s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (user_id))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    result = cursor.fetchone()
                    user = User(result['user_id'],
                                result['username'],
                                result['password'],
                                result['level'],
                                result['grade'],
                                result['type'],
                                result['wallet'],
                                result['user_picture'], 
                                result['state_message'])
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return user
    
    # 添加用户
    def inserUser (self,user:User) :
        '''添加一个新用户
            @param User实体类
            @return 布尔值True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "INSERT  INTO  users (username, password,user_picture,type,level,grade,wallet,state_message) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (user.username,
                                                    user.password,
                                                    user.user_picture,
                                                    user.type,
                                                    user.level,
                                                    user.grade,
                                                    user.wallet,                                            
                                                    user.state_message))
                # print('affect_num={}'.format(affected_num))
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)
                    
    # 查询用户余额
    def selectWalletByUserId (self,user_id:int) :
        '''查询用户余额
            @param 用户ID
            @return 金额Wallet'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        wallet = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "select wallet from users where user_id= %s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (user_id))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    # 存在该用户密码，登录成功
                    result = cursor.fetchone()
                    wallet = result['wallet']
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return wallet
    
    # 更新用户余额
    def updateUserWallet (self,user_id:int,wallet:int) :
        '''更新用户余额
            @param 用户ID
            @param 金额wallet
            @return 布尔值True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "update users set wallet = %s where user_id= %s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (wallet,user_id))
                # print('affect_num={}'.format(affected_num))
                
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)
    
# 评论表
class CommentDaoImpl:
    '''评论表 数据访问 提供如下方法
       @methoad: addComment() 添加评论信息
       @methoad: selectCommentByGoodId() 通过商品ID获取相关评论信息
       @methoad: selectHasCommentByOrderId() 根据order_id 查看是否有评论信息
       @methoad: updateSaysByOrderId() 根据根据order_id 修改 评论信息
    '''
    # 添加评论信息
    def addComment (self,comment:Comment) :
        '''添加一条评论记录
            @param 评论表实体类Comment
            @return 布尔值 True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        list_orders = []
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "INSERT  INTO  comment (says_time, says, goods_id, user_id, username,order_id) VALUES (%s,%s,%s,%s,%s,%s)"
                affected_num = cursor.execute(sql, (comment.says_time,
                                                    comment.says,
                                                    comment.goods_id,
                                                    comment.user_id,
                                                    comment.username,
                                                    comment.order_id
                                                    ))
                # print('affect_num={}'.format(affected_num))
                
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)
    
    # 通过商品ID获取相关评论信息
    def selectCommentByGoodId (self,order_id:int) :
        '''通过商品ID获取相关评论信息
            @param 商品ID
            @return 评论集合 list_comments'''
        connection = Mysql_Static_Factory.get_connection()
        list_comments = []
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "select * from comment where goods_id=%s"
                affected_num = cursor.execute(sql, (order_id))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    results = cursor.fetchall()
                    for result in results:
                        comment = Comment(result['says_id'],
                                          result['says_time'],
                                          result['says'],
                                          result['goods_id'],
                                          result['user_id'],
                                          result['username'],
                                          result['order_id'],
                                          )
                        list_comments.append(comment)
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
        return list_comments
    
    # 根据order_id 查看是否有评论信息
    def selectHasCommentByOrderId (self,order_id:int) :
        '''根据order_id获取评论信息
            @param 商品ID
            @return 布尔值 True代表有'''
        connection = Mysql_Static_Factory.get_connection()
        has = False
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "select * from comment where order_id =%s"
                affected_num = cursor.execute(sql, (order_id))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    has = True
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
        return has
    
    # 根据根据order_id 修改 评论信息
    def updateSaysByOrderId (self,order_id:int,says:str) :
        '''根据根据order_id 修改 评论信息
            @param 商品ID
            @param 评论数据
            @return 布尔值 True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "UPDATE comment SET says = %s WHERE order_id = %s"
                affected_num = cursor.execute(sql, (says,order_id))
                # print('affect_num={}'.format(affected_num))
                
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
        return (affected_num > 0)
    
# 商品表
class GoodsDaoImpl:
    '''商品表 数据访问 提供如下方法
       @methoad: selectGoodList() 查询所有商品信息
       @methoad: selectGoodByGoodId() 根据商品Id获取商品信息
    '''
    # 查询所有商品信息
    def selectGoodList (self) :
        '''查询所有商品信息
            @return 商品列表 list_goods'''
        connection = Mysql_Static_Factory.get_connection()
        list_goods = []
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "select * from goods"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql)
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    results = cursor.fetchall()
                    for result in results:

                        good = Good(result['goods_id'],
                                    result['goods_name'],
                                    result['goods_price'],
                                    result['goods_picture'],
                                    result['goods_describe'])
                        list_goods.append(good)
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return list_goods
    
    # 根据商品Id获取商品信息
    def selectGoodByGoodId (self,goods_id:int) :
        '''根据商品Id获取商品信息
            @param 商品ID goods_id
            @return 商品实体类 good'''
        connection = Mysql_Static_Factory.get_connection()
        good = Good
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "select * from goods where goods_id=%s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql,(goods_id))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    result = cursor.fetchone()
                    
                    good = Good(result['goods_id'],
                                result['goods_name'],
                                result['goods_price'],
                                result['goods_picture'],
                                result['goods_describe'])
                    
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return good

# 订单表
class OrderDaoImpl:
    '''订单表 数据访问 提供如下方法
       @methoad: selectOrderByUserId() 通过用户ID 从订单表里获取数据
       @methoad: insertCartToOder() 将购物车记录生成为订单记录
       @methoad: addOrderBySingleShopCart() 将购物车记录生成为订单记录
       @methoad: updateOrderSays() 修改评论数据
       @methoad: deleteOrderById() 删除订单记录
    '''
    # 通过用户ID 从订单表里获取数据
    def selectOrderByUserId (self,user_id:int) :
        '''通过用户ID 从订单表里获取数据
            @param 用户ID
            @return 列表list_orders 内装填Order实体类'''
        connection = Mysql_Static_Factory.get_connection()
        list_orders = []
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "select * from orders where user_id=%s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (user_id))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    results = cursor.fetchall()
                    for result in results:

                        order = Order(result['order_id'],
                                      result['order_time'],
                                      result['order_count'],
                                      result['order_amount'],
                                      result['user_id'],
                                      result['username'],
                                      result['goods_id'],
                                      result['goods_name'],
                                      result['goods_price'],
                                      result['goods_picture'],
                                      result['goods_describe'],
                                      result['says'])
                        list_orders.append(order)
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return list_orders

    # 将购物车记录生成为订单记录
    def insertCartToOder (self,order:Order) :
        '''将购物车记录生成为订单记录
            @param Order实体类
            @return 布尔值 True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                # print(order.__str__)
                sql = "insert into orders(order_time,order_count,order_amount,user_id,username,goods_id,goods_name,goods_price,goods_picture,goods_describe) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (order.order_time,
                                                    order.order_count,
                                                    order.order_amount,
                                                    order.user_id,
                                                    order.username,
                                                    order.goods_id,
                                                    order.goods_name,
                                                    order.goods_price,
                                                    order.goods_picture,
                                                    order.goods_describe,))
                # print('affect_num={}'.format(affected_num))
                
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)

    # 将购物车记录生成为订单记录
    def addOrderBySingleShopCart (self,order:Order) :
        '''将购物车记录生成为订单记录
            @param Order实体类
            @return 布尔值 True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "insert into orders(order_time,order_count,order_amount,user_id,username,goods_id,goods_name,goods_price,goods_picture,goods_describe) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (order.order_time,
                                                    order.order_count,
                                                    order.order_amount,
                                                    order.user_id,
                                                    order.username,
                                                    order.goods_id,
                                                    order.goods_name,
                                                    order.goods_price,
                                                    order.goods_picture,
                                                    order.goods_describe,))
                # print('affect_num={}'.format(affected_num))
                
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)

    # 修改评论数据
    def updateOrderSays (self,order:Order) :
        '''通过order_id和says修改评论数据
            @param Order实体类
            @return 布尔值 True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "UPDATE orders SET says = %s WHERE order_id = %s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (order.says,
                                                    order.order_id))
                # print('affect_num={}'.format(affected_num))
                
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)
    
    # 删除订单记录
    def deleteOrderById (self,order_id:int) :
        '''删除订单记录
            @param 订单ID order_id
            @return 布尔值 True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "DELETE  FROM orders  WHERE order_id =%s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (order_id))
                # print('affect_num={}'.format(affected_num))
                
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)

# 购物车表
class Shopping_cartDaoImpl:
    '''购物车表 数据访问 提供以下方法：
       @methoad: insertGoodTOCart() 添加一条购物车记录
       @methoad: selectReturnInfo() 得到购物车id,商品id,用户id
       @methoad: selectAllShopCartByUserId() 通过用户id,获取该用户购物车的所有数据
       @methoad: deleteById() 通过购物车id,删除对应一行购物车数据
    '''

    # 添加一条购物车记录
    def insertGoodTOCart (self,shopping_cart:Shopping_cart) :
        '''添加一条购物车记录
            @param Shopping_cart实体类
            @return 布尔值True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "insert into shopping_cart(shopping_count,shopping_amount,goods_id,goods_name,goods_price,goods_picture,goods_describe,user_id,username) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (shopping_cart.shopping_count,
                                                    shopping_cart.shopping_amount,
                                                    shopping_cart.goods_id,
                                                    shopping_cart.goods_name,
                                                    shopping_cart.goods_price,
                                                    shopping_cart.goods_picture,
                                                    shopping_cart.goods_describe,                                            
                                                    shopping_cart.user_id,
                                                    shopping_cart.username))
                print('affect_num={}'.format(affected_num))
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)

    # 啥玩意？定义了一个新类属于购物车实体类的子类，用商品id和用户id去查询购物车，得到购物车id，商品id，用户id
    def selectReturnInfo (self,goods_id:int,user_id:int) :
        '''通过用户ID,商品ID 查询购物车内的购物车单条ID
            @param 商品ID
            @param 用户ID
            @return Mini_Shopping_cart实体类'''
        connection = Mysql_Static_Factory.get_connection()
        mini_Shopping_cart = Mini_Shopping_cart
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "select shopping_cart_id,goods_id,user_id from shopping_cart where goods_id=%s and user_id=%s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (goods_id,user_id))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    result = cursor.fetchone()
                    mini_Shopping_cart = Mini_Shopping_cart(result['shopping_cart_id'],
                                                            goods_id,
                                                            user_id)
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return mini_Shopping_cart

    # 通过用户id,获取该用户购物车的所有数据
    def selectAllShopCartByUserId (self,user_id:int) :
        '''通过用户id,获取该用户购物车的所有数据
            @param 用户ID
            @return 购物车列表 list_Shopping_cart'''
        connection = Mysql_Static_Factory.get_connection()
        list_Shopping_cart = []
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "select * from shopping_cart where user_id = %s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (user_id))
                # print('affect_num={}'.format(affected_num))
                if affected_num > 0:
                    results = cursor.fetchall()
                    for result in results:

                        shopping_cart = Shopping_cart(result['shopping_cart_id'],
                                                      result['shopping_count'],
                                                      result['shopping_amount'],
                                                      result['goods_id'],
                                                      result['goods_name'],
                                                      result['goods_price'],
                                                      result['goods_picture'],
                                                      result['goods_describe'],
                                                      result['user_id'], 
                                                      result['username'],
                                                      )
                        list_Shopping_cart.append(shopping_cart)
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return list_Shopping_cart
    
    # 通过购物车id,删除对应一行购物车数据
    def deleteById (self,shopping_cart_id:int) :
        '''通过购物车ID,删除对应一行购物车数据
            @param shopping_cart_id
            @return 布尔值 True代表成功'''
        connection = Mysql_Static_Factory.get_connection()
        affected_num = 0
        try:
            with  connection.cursor() as cursor:
                # 创建一条预编译的 SQL 语句
                sql = "DELETE FROM shopping_cart WHERE shopping_cart_id =%s"
                # 执行预编译的 SQL 语句并传入参数
                affected_num = cursor.execute(sql, (shopping_cart_id))
                # print('affect_num={}'.format(affected_num))
                
                # 提交事务
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

        return (affected_num > 0)



