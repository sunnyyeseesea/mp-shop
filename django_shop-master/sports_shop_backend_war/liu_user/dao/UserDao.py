from  dao.MysqlHelper import Mysql_Static_Factory
from entity.User import User
# from models import User
# from MysqlHelper import Mysql_Static_Factory
class UserDaoImpl:

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
                print('affect_num={}'.format(affected_num))
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
