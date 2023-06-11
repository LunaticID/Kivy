from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder



class Signup(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("kv/signup.kv")
        super().__init__(*args, **kwargs)