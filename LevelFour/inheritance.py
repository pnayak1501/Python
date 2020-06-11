class Samsung:
    def __int__(self):
        print("Hello from samsung")

    def mobile(self):
        print("I am a samsung phone")

    def tab(self):
        print("I am a tab")


class Iphone(Samsung):
    def __init__(self):
        print("Hello from Iphone")

    def ipad(self):
        print("I am a ipad")
        super().tab()


i = Iphone()
i.ipad()

i.mobile()
