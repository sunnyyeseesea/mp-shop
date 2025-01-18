class Mini_Shopping_cart:
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

    