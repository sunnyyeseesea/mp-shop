from  dao.MysqlHelper import Mysql_Static_Factory
from entity.Shopping_cart import Shopping_cart
from entity.Mini_entity import Mini_Shopping_cart
# from MysqlHelper import Mysql_Static_Factory

class Shopping_cartDaoImpl:
    '''购物车表 数据访问'''

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














