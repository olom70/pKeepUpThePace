import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
import kivy.properties
from kivy.lang import Observable
from os.path import join, dirname
import gettext


class Lang(Observable):
    observers = []
    lang = None

    def __init__(self, defaultlang):
        super(Lang, self).__init__()
        self.ugettext = None
        self.lang = defaultlang
        self.switch_lang(self.lang)

    def _(self, text):
        return self.ugettext(text)

    def fbind(self, name, func, args, **kwargs):
        if name == "_":
            self.observers.append((func, args, kwargs))
        else:
            return super(Lang, self).fbind(name, func, *args, **kwargs)

    def funbind(self, name, func, args, **kwargs):
        if name == "_":
            key = (func, args, kwargs)
            if key in self.observers:
                self.observers.remove(key)
        else:
            return super(Lang, self).funbind(name, func, *args, **kwargs)

    def switch_lang(self, lang):
        # get the right locales directory, and instanciate a gettext
        locale_dir = join(dirname(__file__), 'data', 'locales')
        locales = gettext.translation('keepupthepaceapp', locale_dir, languages=[lang])
        self.ugettext = locales.gettext

        # update all the kv rules attached to this text
        for func, largs, kwargs in self.observers:
            func(largs, None, None)


tr = Lang("en")


class Front1(PageLayout):
    pass


class KeepUpThepaceApp(App):

    lang = kivy.properties.StringProperty('en')

    def build(self):
        return Front1()

    def on_lang(self, instance, lang):
        tr.switch_lang(lang)


if __name__ == "__main__":
    KeepUpThepaceApp().run()