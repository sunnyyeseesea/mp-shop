from  dao.MysqlHelper import Mysql_Static_Factory
from entity.Good import Good

class GoodsDaoImpl:
    '''商品表 数据访问'''
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