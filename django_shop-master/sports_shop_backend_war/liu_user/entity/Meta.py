class Meta:
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