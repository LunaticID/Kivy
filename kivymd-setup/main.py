from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.text import LabelBase
from layar.screens import *
from kivymd.app import MDApp


class WindoManager(ScreenManager):
    pass

class Test(MDApp):
    DEBUG = 1
    #untuk hotreload
    CLASSES = {
        'Welcome':'layar.welcome',
        'Masuk':'layar.masuk',
        'Signup':'layar.signup',
        'Panjangsapi':'layar.panjangsapi',
        'Lingkardada':'layar.lingkardada',
        'Rumus' : 'layar.rumus'
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]
    KV_FILES = [
        'kv/welcome.kv',
        'kv/masuk.kv',
        'kv/signup.kv',
        'kv/panjangsapi.kv',
        'kv/lingkardada.kv',
        'kv/rumus.kv'
    ]
    def build(self):
        self.wm = WindoManager()
        screens = [
            Welcome(name ="welcome"),
            Masuk(name= "masuk"),
            Signup(name="signup"),
            Panjangsapi(name="panjangsapi"),
            Lingkardada(name="lingkardada"),
            Rumus(name="rumus")                        
        ]
        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm

if __name__ == '__main__':
    LabelBase.register(name="MPoppins", fn_regular="aset/font/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="aset/font/Poppins-SemiBold.ttf")
    Test().run() 