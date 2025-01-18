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