from PIL import Image, ImageFilter

before = Image.open("London-Bridge.jpg")
after = before.filter(ImageFilter.BLUR)
after.save("out.jpg")


