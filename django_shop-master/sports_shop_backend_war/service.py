import json

# bean实体类
from .models import User
from .models import Meta
from .models import Order
from .models import Shopping_cart
from .models import Good
from .models import Comment
# dao数据访问层
from .dao import Mysql_Static_Factory
from .dao import UserDaoImpl
from .dao import Shopping_cartDaoImpl
from .dao import OrderDaoImpl
from .dao import GoodsDaoImpl
from .dao import CommentDaoImpl
# 这一句代码——大宝贝：多个自定义类存与字典中，如何把该字典转换为JSON
# json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (User, Meta)) else None, ensure_ascii=False)

class UserService:
    '''提供User功能服务'''
    def login (self,username:str,password:str):
        '''通过用户ID查询用户信息
            @param 用户名,
            @param 密码,
            @return {User+Meta} 字典数据'''
        user_id = UserDaoImpl().selectByNamePWD(username,password)
        data = UserDaoImpl().selectByID(user_id)

        meta = Meta("登录成功",200)
        
        response = { 
            'data': data,
            'meta': meta
        }

        json_str = json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (User, Meta)) else None, ensure_ascii=False)
        
        print(json_str)
         
        return (json_str)
    
'''完美分层实在太痛苦了,肝不动了,其他的全部一股脑写models.py里面了,既当control又当service,哪天肝和腰养好了再来继续分离'''