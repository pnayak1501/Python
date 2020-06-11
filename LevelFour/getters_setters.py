
class Phone:
    user = ""
    model = "iPhone"

    def __init__(self,user_name):
        self.user = user_name

    def get_model(self):
        return self.model

    def set_model(self,val):
        self.model =self.model+val


obj = Phone("Prahlad")
obj.set_model("S10")
print(obj.get_model())
