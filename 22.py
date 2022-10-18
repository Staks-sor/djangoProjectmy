
from PIL import Image


list_photo = ['/home/staks/Изображения/phoenix.png', 'fdsff', '23fdw']

for i in list_photo:
    print(i)
    if i == '/home/staks/Изображения/phoenix.png':
        im = Image.open(i)
        im.show()
        print(im)
