from random import *
class MyMixin(object):
    mixin_prop = "https://itchief.ru/assets/images/covers/html-and-css-wave-divider-using-svg.jpg"

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()

    def get_random(self):
        random_photo_list = ['https://klike.net/uploads/posts/2019-05/1556945364_1.jpg',
                             'https://img2.reactor.cc/pics/post/art-%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B5'
                             '-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D0%BC%D0%B8%D1%80-%D0%9C%D0%BE%D1%8F'
                             '-%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0-7240293.jpeg ',
                             'https://img2.joyreactor.cc/pics/post/Sci-Fi-art-cyberpunk-Nivanh-Chanthara-7645174.jpeg'
                             ]
        return choice(random_photo_list)