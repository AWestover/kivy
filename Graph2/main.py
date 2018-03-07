from kivy.graphics import Color, Ellipse, Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from random import random
from kivy.app import App
import math
import pdb

updates_per_sec = 10
pix_per_update = 10
freq = 10

"""
Note: do fourier transform too!!!
text: str(root.area)
"""

class GraphShow(Widget):
    area = NumericProperty(0)

    def init(self):
        self.time = 0
        self.exp_avg = 0
        self.alpha = 0.2
        self.last_pos = [0,0]

    def update(self, dt):
        x = self.time*pix_per_update
        y = random()*self.size[1]*1/3 + math.sin(self.time * 2 * math.pi / freq) * self.size[1]/(2*3) + self.size[1]*1/3
        self.exp_avg = self.alpha * y + (1-self.alpha) * self.exp_avg
        self.data.points += [x, y]
        self.data_o.points += [x, self.exp_avg]
        self.time += 1

        self.area += ((self.last_pos[1]+y) / 2) * (x-self.last_pos[0])
        self.area = round(self.area, 3)
        self.last_pos = [x, y]

        if self.time*pix_per_update > self.size[0]:
            self.canvas.clear()
            with self.canvas:
                Color(self.rand_color)
                self.data = Line(points=(0,0))
                Color(1,0,0)
                self.data_o = Line(points=(0,0))
            self.area = 0
            self.time = 0

    def rand_color(self):
        return (random(), random(), random())

class GraphApp(App):
    def build(self):
        self.icon = "shark.png"
        self.game = GraphShow()
        self.game.init()
        with self.game.canvas:
            Color(0,0,1)
            self.game.data = Line(points=(0,0))
            Color(1, 0, 0)
            self.game.data_o = Line(points=(0,0))
        Clock.schedule_interval(self.game.update, 1.0 / updates_per_sec)
        return self.game

if __name__ == "__main__":
    GraphApp().run()


