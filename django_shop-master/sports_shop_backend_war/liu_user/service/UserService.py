import json
# from entity.User import User
# from entity.Meta import Meta
from dao import UserDaoImpl
from models import User
from models import Meta
class UserService:

    def login (self,username:str,password:str):
        '''通过用户ID查询用户信息
            @param 用户名,
            @param 密码,
            @return 用户实体类'''
        user_id = UserDaoImpl().selectByNamePWD(username,password)
        user = UserDaoImpl().selectByID(user_id)

        meta = Meta("登录成功",200)
        resp = {
            'data':user,
            'meta':meta
            }

        print(json.dumps(resp,default=str))


'''心累了,奇葩导包,直接在sports_shop_backedn_war这个django的app目录下定义一个service.py写了'''

