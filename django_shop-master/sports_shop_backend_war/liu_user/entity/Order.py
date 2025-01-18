import datetime
class Order:
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

    there = dict()

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