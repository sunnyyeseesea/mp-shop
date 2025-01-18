
import json
# 自定义实体类1:已实现__str__，__repr用于格式化输出属性；__json__用于json序列化
class Meta:
    '''元信息 在一个http请求完成后与data一起打包成JSON数据发给API调用者
            @attribute: msg = str
            @attribute: status = int
            '''
    # 属性
    msg = str
    status = int

    def __init__(self, msg:str,status:int):
        '''订单表:Order实体类的构造函数'''
        self.msg = msg
        self.status = status
        
    def toString(self):
        return self.__str__()
    
    def __str__ (self):
        return f"Meta(msg={self.msg}, status={self.status})"
    
    def __repr__ (self):
        return f"Meta(msg={self.msg}, status={self.status})"
    
    def __json__(self):
        return {"msg": self.msg, "status": self.status}
    
# 自定义实体类2:已实现__str__，__repr用于格式化输出属性；__json__用于json序列化
class User:
    '''用户实体类
            @attribute:  user_id =str
            @attribute:  username = int
            @attribute:  password = str
            @attribute:  level = int
            @attribute:  grade = str
            @attribute:  type = str
            @attribute:  wallet = int
            @attribute:  user_picture = str
            @attribute:  state_message = str'''
    # 属性
    user_id =str
    username = int
    password = str
    level = int
    grade = str
    type = str
    wallet = int
    user_picture = str
    state_message = str

    #构造函数
    def __init__(self, user_id:int, username:str, password:str, level:int, grade:str, type:str, wallet:int, user_picture:str, state_message:str):
        '''User实体类的构造函数'''
        self.user_id = user_id
        self.username = username
        self.password = password
        self.level = level
        self.grade = grade
        self.type = type
        self.wallet = wallet
        self.user_picture = user_picture
        self.state_message = state_message
  
    def __str__ (self):
        return f"User(user_id={self.user_id}, username={self.username},password={self.password},level={self.level},grade={self.grade},type={self.type},wallet={self.wallet},user_picture={self.user_picture},state_message={self.state_message})"
    
    def __repr__(self):
        return f"User(user_id={self.user_id}, username={self.username},password={self.password},level={self.level},grade={self.grade},type={self.type},wallet={self.wallet},user_picture={self.user_picture},state_message={self.state_message})"

    def __json__(self):
        return {"user_id": self.user_id, 
                "username": self.username, 
                "password": self.password, 
                "level": self.level, 
                "grade": self.grade, 
                "type": self.type,
                "wallet": self.wallet,
                "user_picture": self.user_picture,
                "state_message": self.state_message}

# 执行过程:
data = User(1,'admin','123',1,"vip","kk",100,"http://127.0.0.1:8080/user.jpg","这个人很懒，什么都没有留下")
meta = Meta("登录成功",200)

# 将上面两个对象存于dict字典中
response = {
    'data':data,
    'meta':meta
}

# ensure_ascii=False用于禁止中文encode加密,效果是保留原中文输出
print('=======================User对象转JSON====================================')
print(json.dumps(data.__json__(),ensure_ascii=False))
print('=======================Meta对象JSON======================================')
print(json.dumps(meta.__json__(),ensure_ascii=False))

print('========================response字典转JSON===============================')
print(json.dumps(response, default=lambda o: o.__json__() if isinstance(o, (User, Meta)) else None, ensure_ascii=False))