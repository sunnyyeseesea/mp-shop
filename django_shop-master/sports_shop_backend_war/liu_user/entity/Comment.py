import datetime

class Comment:
    # 属性
    says_id = int
    says_time = datetime.datetime.now()  # 使用 datetime 对象
    says = str
    goods_id = int
    user_id = int
    username = str
    order_id = int

    # 构造函数
    def __init__(self, says_id, says_time=None, says="", goods_id=0, user_id=0, username="", order_id=0):
        '''评论表: Comment 实体类的构造函数'''
        self.says_id = says_id
        # 如果没有传递 says_time，则使用当前时间
        self.says_time = says_time if says_time else datetime.datetime.now()
        self.says = says
        self.goods_id = goods_id
        self.user_id = user_id
        self.username = username
        self.order_id = order_id

    def __str__(self):
        return f"Comment(says_id={self.says_id}, says_time={self.get_formatted_time()}, says={self.says}, goods_id={self.goods_id}, user_id={self.user_id}, username={self.username}, order_id={self.order_id})"

    def __repr__(self):
        return f"Comment(says_id={self.says_id}, says_time={self.get_formatted_time()}, says={self.says}, goods_id={self.goods_id}, user_id={self.user_id}, username={self.username}, order_id={self.order_id})"

    def __json__(self):
        # 转换时间为字符串（格式：YYYY-MM-DD HH:MM:SS）
        return {
            "says_id": self.says_id,
            "says_time": self.get_formatted_time(),
            "says": self.says,
            "goods_id": self.goods_id,
            "user_id": self.user_id,
            "username": self.username,
            "order_id": self.order_id
        }

    def get_formatted_time(self):
        # 格式化时间为字符串（YYYY-MM-DD HH:MM:SS）
        return self.says_time.strftime("%Y-%m-%d %H:%M:%S")

    def set_time(self, time: datetime.datetime):
        # 设置自定义时间
        self.says_time = time
