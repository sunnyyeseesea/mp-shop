import datetime
class Shopping_cart:
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

    there = dict()

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