from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class Rumus(MDScreen):
    lingkar_dada = NumericProperty()
    panjang_badan = NumericProperty()

    def __init__(self, **kwargs):
        Builder.load_file("kv/rumus.kv")
        super().__init__(**kwargs)
        
    def on_pre_enter(self, *args):
        lingkardada = self.manager.get_screen("lingkardada")
        circumference_cm = lingkardada.circumference_cm
        self.ids.circumference_label.text = "Lingkar dada : {:.2f} Cm".format(circumference_cm)
    
        panjangsapi = self.manager.get_screen("panjangsapi")
        length_cm = panjangsapi.length_cm
        self.ids. length_label.text = "Panjang sapi : {:.2f} Cm".format(length_cm)

    def hitung_bobot_sapi(self):
        bb = round(((self.lingkar_dada ** 2) + (self.panjang_badan ** 2)) / 10815.15, 2)
        self.ids.bobot_sapi.text = "Berat Badan Sapi : {} kg".format(str(bb).replace('.', ''))



    def set_lingkar_dada(self, value):
        if value:
            self.lingkar_dada = float(value)
        else:
            self.lingkar_dada = 0.0

    def set_panjang_badan(self, value):
        if value:
            self.panjang_badan = float(value)
        else:
            self.panjang_badan = 0.0

    