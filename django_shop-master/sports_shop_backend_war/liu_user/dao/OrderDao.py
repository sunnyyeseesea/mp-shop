from  dao.MysqlHelper import Mysql_Static_Factory
from entity.Order import Order

class OrderDaoImpl:
    '''订单表 数据访问'''
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























