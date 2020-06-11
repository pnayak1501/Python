
class Phone:
    company = "Apple"
    model = "iPhone 11"
    user = ""

    def __init__(self,user_name):
        self.user = user_name
        print("Hello")

    def pri(self):
        print(self.company)
        print(self.model)
        print(self.user)


obj = Phone("Prahlad")
obj.pri()
