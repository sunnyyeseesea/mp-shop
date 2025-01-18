# import datetime
# my_date = datetime.datetime.now()
# formatted_date = my_date.strftime("%Y-%m-%d")
class Good:
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