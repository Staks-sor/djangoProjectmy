class MyMixin(object):
    mixin_prop = "https://itchief.ru/assets/images/covers/html-and-css-wave-divider-using-svg.jpg"

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()