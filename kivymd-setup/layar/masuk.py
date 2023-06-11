from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder



class Masuk(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("kv/masuk.kv")
        super().__init__(*args, **kwargs)