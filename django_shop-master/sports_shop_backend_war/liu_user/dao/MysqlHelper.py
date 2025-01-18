import pymysql

class Mysql_Static_Factory:

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
        

# 测试区域
# conn = MysqlHelper.get_connection()
# cur = conn.cursor()
# print(conn)
# print(cur)
# conn.close()
# cur.close()
