from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
from plyer import filechooser
from kivy.properties import (ObjectProperty, NumericProperty)
from PIL import Image
import cv2
import numpy as np
from kivy.uix.button import Button

class Panjangsapi(MDScreen):
    img1 = ObjectProperty(None)
    img2 = ObjectProperty(None)
    length_cm = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        Builder.load_file("kv/panjangsapi.kv")
        super().__init__(*args, **kwargs)
        self.img1 = self.ids.img1
        self.img2 = self.ids.img2
        self.length_label = self.ids.length_label

    def file_chooser(self, img):
        filechooser.open_file(on_selection=lambda x: self.selected(x,img))

    def selected(self, selection, img):
        if selection:
            img.source = selection[0]

    def clear(self):
        self.img1.source = ''
        self.img2.source = ''
        self.length_label.text = ''
    def proses_gambar(self):
        if not self.img1.source:
            return
        with Image.open(self.img1.source) as im:
            im = np.array(im)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)            
            kernel = np.ones((5,5), np.uint8)
            morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)

            contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            cow_contour = max(contours, key=cv2.contourArea)
            rect = cv2.minAreaRect(cow_contour)

            box = cv2.boxPoints(rect)
            box = np.intp(box)
            cv2.drawContours(im,[box],0,(0,0,255),2)

            length = max(rect[1])

            scale_factor = 0.15
            length_cm = length * scale_factor
            self.length_cm = length_cm
            self.length_label.text="Panjang Sapi : {:.2f} Cm".format(length_cm)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            cv2.imwrite('hasil.png', im)
            self.img2.source = 'hasil.png'
            self.img2.reload()