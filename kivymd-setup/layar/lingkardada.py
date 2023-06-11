from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from plyer import filechooser
from kivy.properties import ObjectProperty, ListProperty,NumericProperty
from PIL import Image
from kivy.graphics import Line, Color

class Lingkardada(MDScreen):
    img1 = ObjectProperty(None)
    points = ListProperty([])
    lines = ListProperty([])
    circumference_cm = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        Builder.load_file("kv/lingkardada.kv") 
        super().__init__(*args, **kwargs)
        self.img1 = self.ids.img1

    def file_chooser(self, img):
        filechooser.open_file(on_selection=lambda x: self.selected(x,img))

    def selected(self, selection, img):
        if selection:
            img.source = selection[0]

    def clear(self):
        self.img1.source = ''
        self.points = []
        self.circumference_cm = 0
        self.ids.circumference_label.text = "Lingkar dada: 0.0 Cm"
        for line in self.lines:
            self.img1.canvas.remove(line)
        self.lines = []

    def on_touch_down(self, touch):
        if self.img1.collide_point(*touch.pos):
            self.points.append(touch.pos)
            with self.img1.canvas:
                Color(1, 0, 0) 
                line = Line(points=(touch.pos[0]-5, touch.pos[1]-5), width=3)
                self.lines.append(line)
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.img1.collide_point(*touch.pos):
            self.points.append(touch.pos)
            with self.img1.canvas:
                Color(1, 0, 0) 
                line = Line(points=self.points, width=3)
                self.lines.append(line)
        return super().on_touch_up(touch)
    
    def calculate_circumference(self):
        if len(self.points) > 2:
            circumference = 0
            for i in range(len(self.points)-1):
                x1, y1 = self.points[i]
                x2, y2 = self.points[i+1]
                diameter = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                circumference += diameter

            x1, y1 = self.points[-1]
            x2, y2 = self.points[0]
            diameter = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            circumference += diameter
           
            cm_per_pixel = 0.65
            self.circumference_cm = circumference * cm_per_pixel          
            self.ids.circumference_label.text = f"Lingkar dada: {self.circumference_cm:.2f} Cm"
    