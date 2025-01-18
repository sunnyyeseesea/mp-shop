'''涵盖项目使用到的bean 对应数据库各张表结构'''
from django.db import models
import datetime

# Create your models here.

# 实体类
class Comment:
    '''评论表 实体类
       @attribute: says_id = int
       @attribute: says_time = datetime.datetime.now().strftime("%Y-%m-%d")
       @attribute: says = str
       @attribute: goods_id = int
       @attribute: user_id = int
       @attribute: username = str
       @attribute: order_id = int
    '''
    # 属性
    says_id = int
    says_time = datetime.datetime.now().strftime("%Y-%m-%d")
    says = str
    goods_id = int
    user_id = int
    username = str
    order_id = int

    # 改造python entity
    there = dict()
    #构造函数
    def __init__(self,says_id, says_time, says, goods_id, user_id, username, order_id):
        '''评论表:Comment实体类的构造函数'''
        self.says_id = says_id
        self.says_time = says_time
        self.says = says
        self.goods_id = goods_id
        self.user_id  = user_id
        self.username = username
        self.order_id = order_id
        
    def __str__ (self):
        return f"Comment(says_id={self.says_id},says_time={self.says_time},says={self.says},goods_id={self.goods_id},user_id={self.user_id},username={self.username},order_id={self.order_id})"
    
    def __repr__(self):
        return f"Comment(says_id={self.says_id}, says_time={self.says_time},says={self.says},goods_id={self.goods_id},user_id={self.user_id},tusernameype={self.username},order_id={self.order_id})"

    def __json__(self):
        return {"says_id": self.user_id, 
                "says_time": self.says_time, 
                "says": self.says, 
                "goods_id": self.goods_id, 
                "user_id": self.user_id, 
                "username": self.username,
                "order_id": self.order_id}

class Good:
    '''商品表 实体类
       @attribute: goods_id = int
       @attribute: goods_name = str
       @attribute: goods_price = int
       @attribute: goods_picture = str
       @attribute: goods_describe = str
    
    '''
    # 属性
    goods_id = int
    goods_name = str
    goods_price = int
    goods_picture = str
    goods_describe = str

    # 改造python entity
    there = dict()
    #构造函数
    def __init__(self,goods_id:int, goods_name:str, goods_price:int, goods_picture:str, goods_describe:str):
        '''商品表:Good实体类的构造函数'''
        self.goods_id = goods_id
        self.goods_name = goods_name
        self.goods_price = goods_price
        self.goods_picture = goods_picture
        self.goods_describe  = goods_describe

    def __str__ (self):
        return f"Good(goods_id={self.goods_id},goods_name={self.goods_name},goods_price={self.goods_price},goods_picture={self.goods_picture},goods_describe={self.goods_describe})"
    
    def __repr__(self):
        return f"Good(goods_id={self.goods_id},goods_name={self.goods_name},goods_price={self.goods_price},goods_picture={self.goods_picture},goods_describe={self.goods_describe})"

    def __json__(self):
        return {"goods_id": self.goods_id, 
                "goods_name": self.goods_name, 
                "goods_price": self.goods_price, 
                "goods_picture": self.goods_picture, 
                "goods_describe": self.goods_describe}

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

class Mini_Shopping_cart:
    '''迷你购物车表 实体类
            @attribute: shopping_cart_id = int
            @attribute: goods_id = int
            @attribute: user_id = int
            '''
    # 属性
    shopping_cart_id = int
    goods_id = int
    user_id = int

    #构造函数
    def __init__(self, shopping_cart_id:int, goods_id:int, user_id:int, ):
        '''mini购物车表:Mini_Shopping_cart实体类的构造函数'''
        self.shopping_cart_id = shopping_cart_id
        self.goods_id = goods_id
        self.user_id = user_id

        
    def __str__ (self):
        return f"Mini_Shopping_cart(shopping_cart_id={self.shopping_cart_id},goods_id={self.goods_id},user_id={self.user_id})"
    
    def __repr__(self):
        return f"Mini_Shopping_cart(shopping_cart_id={self.shopping_cart_id},goods_id={self.goods_id},user_id={self.user_id})"

    def __json__(self):
        return {"shopping_cart_id": self.shopping_cart_id, 
                "goods_id": self.goods_id, 
                "user_id": self.user_id}

class Order:
    '''订单实体类
            @attribute: order_id = int
            @attribute: order_time = datetime.datetime.now().strftime("%Y-%m-%d")
            @attribute: order_count = int
            @attribute: order_amount = int
            @attribute: user_id = int
            @attribute: username = str
            @attribute: goods_id = int
            @attribute: goods_name = str
            @attribute: goods_price = int
            @attribute: goods_picture = str
            @attribute: goods_describe = str
            @attribute: says = str
            '''
    # 属性
    order_id = int
    order_time = datetime.datetime.now().strftime("%Y-%m-%d")
    order_count = int
    order_amount = int
    user_id = int
    username = str
    goods_id = int
    goods_name = str
    goods_price = int
    goods_picture = str
    goods_describe = str
    says = str

    #构造函数
    def __init__(self, order_id:int, order_time:datetime.date, order_count:int, order_amount:int, user_id:int, username:str, goods_id:int, goods_name:str, goods_price:int, goods_picture:str, goods_describe:str,says:str):
        '''订单表:Order实体类的构造函数'''
        self.order_id = order_id
        self.order_time = order_time
        self.order_count = order_count
        self.order_amount = order_amount
        self.user_id = user_id
        self.username = username
        self.goods_id = goods_id
        self.goods_name = goods_name
        self.goods_price = goods_price
        self.goods_picture = goods_picture
        self.goods_describe = goods_describe
        self.says = says

    def __str__ (self):
        return f"Order(order_id={self.order_id},order_time={self.order_time},order_count={self.order_count},order_amount={self.order_amount},user_id={self.user_id},username={self.username},goods_id={self.goods_id},goods_name={self.goods_name},goods_price={self.goods_price},goods_picture={self.goods_picture},goods_describe={self.goods_describe},says={self.says})"
    
    def __repr__(self):
        return f"Order(order_id={self.order_id},order_time={self.order_time},order_count={self.order_count},order_amount={self.order_amount},user_id={self.user_id},username={self.username},goods_id={self.goods_id},goods_name={self.goods_name},goods_price={self.goods_price},goods_picture={self.goods_picture},goods_describe={self.goods_describe},says={self.says})"
    def __json__(self):
        return {"order_id": self.order_id, 
                "order_time": self.order_time, 
                "order_count": self.order_count, 
                "order_amount": self.order_amount, 
                "user_id": self.user_id,
                "username": self.username, 
                "goods_id": self.goods_id, 
                "goods_name": self.goods_name,
                "goods_price": self.goods_price, 
                "goods_picture": self.goods_picture,
                "goods_describe": self.goods_describe,
                "says": self.says}

class Shopping_cart:
    '''用户实体类
            @attribute:  shopping_cart_id = int
            @attribute:  shopping_count = int
            @attribute:  shopping_amount = int
            @attribute:  goods_id = int
            @attribute:  goods_name = str
            @attribute:  goods_price = int
            @attribute:  goods_picture = str
            @attribute:  goods_describe = str
            @attribute:  user_id = int
            @attribute:  username = str
            '''
    # 属性
    shopping_cart_id = int
    shopping_count = int
    shopping_amount = int
    goods_id = int
    goods_name = str
    goods_price = int
    goods_picture = str
    goods_describe = str
    user_id = int
    username = str

    #构造函数
    def __init__(self, shopping_cart_id:int, shopping_count:int, shopping_amount:int, goods_id:int, goods_name:str, goods_price:int, goods_picture:str, goods_describe:str, user_id:int, username:str):
        '''购物车表:Shopping_cart实体类的构造函数'''
        self.shopping_cart_id = shopping_cart_id
        self.shopping_count = shopping_count
        self.shopping_amount = shopping_amount
        self.goods_id = goods_id
        self.goods_name = goods_name
        self.goods_price = goods_price
        self.goods_picture = goods_picture
        self.goods_describe = goods_describe
        self.user_id = user_id
        self.username = username

        
    def __str__ (self):
        return f"Shopping_cart(shopping_cart_id={self.shopping_cart_id},shopping_count={self.shopping_count},shopping_amount={self.shopping_amount},goods_id={self.goods_id},goods_name={self.goods_name},goods_price={self.goods_price},goods_picture={self.goods_picture},goods_describe={self.goods_describe},user_id={self.user_id},username={self.username})"
    
    def __repr__(self):
        return f"Shopping_cart(shopping_cart_id={self.shopping_cart_id},shopping_count={self.shopping_count},shopping_amount={self.shopping_amount},goods_id={self.goods_id},goods_name={self.goods_name},goods_price={self.goods_price},goods_picture={self.goods_picture},goods_describe={self.goods_describe},user_id={self.user_id},username={self.username})"

    def __json__(self):
        return {"shopping_cart_id": self.shopping_cart_id, 
                "shopping_count": self.shopping_count, 
                "shopping_amount": self.shopping_amount, 
                "goods_id": self.goods_id,
                "goods_name": self.goods_name, 
                "goods_price": self.goods_price, 
                "goods_picture": self.goods_picture, 
                "goods_describe": self.goods_describe,
                "user_id": self.user_id, 
                "username": self.username}

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

# dao数据访问层
























