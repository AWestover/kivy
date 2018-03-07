# a clicking game
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from random import random
from random import gauss
from kivy.app import App
import datetime
import os
from os.path import join


"""
NOte
the file making issue I thought existed might not exist...
"""

updates_per_sec = 10
TRIALS = 3
data_folder = "data"
txtf  = join(os.getcwd(), join(data_folder, "test.txt"))

class ClickObj(Widget):
    r = NumericProperty(1)
    g = NumericProperty(1)
    b = NumericProperty(1)
    t = StringProperty('')

    def __init__(self):
        super(ClickObj, self).__init__()
        self.x = 10
        self.y = 10
        self.time = 0
        self.mu = 10  # average difference (time steps)
        self.sigma = 1 # standard deviation (time steps)
        self.shots = [self.set_next_shot(0)]
        self.clicks = []

    """
    Other functions include
    on_touch_down
    on_touch_move
    """
    def on_touch_up(self, touch):
        darkest = 0.4
        self.r=random()*(1-darkest)+darkest
        self.g=random()*(1-darkest)+darkest
        self.b=random()*(1-darkest)+darkest
        if len(self.clicks) < len(self.shots) - 1:
            self.clicks.append(self.time)
            # print(self.clicks, self.shots)

    def set_next_shot(self, last):
        return last + int(gauss(self.mu, self.sigma))

    def update(self, dt):
        # print("update")
        if len(self.clicks) == TRIALS:
            if 'done' not in self.t:
                self.write_out()
                print(self.clicks, self.shots)
        else:
            self.time += 1
            if self.time >= self.shots[-1]:
                if len(self.clicks) < len(self.shots) - 1:
                    self.clicks.append(self.time)  # worst possible score
                    # print(self.clicks, self.shots)
                # print("SHOOT")
                self.x = random()*self.size[0]
                self.y = random()*self.size[1]
                self.shots.append(self.set_next_shot(self.shots[-1]))
                # print(self.clicks, self.shots)

    def write_out(self):
        now = datetime.datetime.now()
        c_id = "year: {} month: {} day: {} hour: {} minute: {} ".format(\
            now.year, now.month, now.day, now.hour, now.minute)
        self.t = 'done'
        errors = []
        for i in range(0, TRIALS):
            errors.append(str(self.clicks[i]-self.shots[i]))
        next_row = [c_id] + errors
        nr = ",".join(next_row)

        with open('data.csv', 'a') as f:
            f.write("\n")
            f.write(nr)

        ct = 0
        with open('data.csv') as f:
            for r in f:
                ct+=1
        self.t='done: '+str(ct)

class ClickApp(App):
    def build(self):
        self.ti = ClickObj()
        with open(txtf, "w") as f:
            f.write("kk")

        Clock.schedule_interval(self.ti.update, 1.0 / updates_per_sec)
        return self.ti

if __name__ == "__main__":
    ClickApp().run()
