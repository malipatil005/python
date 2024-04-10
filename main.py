
class myclass:
    """this is simple class"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print("name=",self.name)
        print("age=",self.age)





if __name__=="__main__":
    c=myclass("deepika",27)
    c.show_details()
