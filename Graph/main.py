from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.clock import Clock
from random import random
from kivy.app import App

updates_per_sec = 10
pix_per_update = 10

class GraphShow(Widget):
    def update(self, dt):
        self.data.points += [self.time*pix_per_update, random()*self.size[1]]
        self.time += 1
        if self.time*pix_per_update > self.size[0]:
            self.canvas.clear()
            with self.canvas:
                self.data = Line(points=(0,0))
                self.time = 0


class GraphApp(App):
    def build(self):
        self.game = GraphShow()
        with self.game.canvas:
            self.game.time = 0
            self.game.data = Line(points=(0,0))
        Clock.schedule_interval(self.game.update, 1.0 / updates_per_sec)
        return self.game

if __name__ == "__main__":
    GraphApp().run()

