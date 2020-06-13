from PIL import Image, ImageFilter

before = Image.open("London-Bridge.jpg")
before.rotate(45).show()