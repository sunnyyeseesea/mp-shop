from  dao.MysqlHelper import Mysql_Static_Factory
from entity.Comment import Comment

class CommentDaoImpl:
    '''评论表数据访问'''
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
