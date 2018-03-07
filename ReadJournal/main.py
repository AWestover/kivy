from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
from os.path import join
import json
import os

# for some reason (probably permission error) you can't create files on the android... :(
data_folder = join(join("..", "Journal"), "test")

jsonf = join(data_folder, "hello.json")
txtf  = join(os.getcwd(), join(data_folder, "test.txt"))


class ReadJournal(GridLayout):
    def __init__(self):
        super(ReadJournal, self).__init__()
        self.cols = 1
        self.row = 1
        with open(jsonf) as f:
            j = json.load(f)
        
        s = ""
        try:
            for entry in j["Alek"]:
                s += entry + "\n\n" + "-"*50 + "\n"
        except KeyError:
            pass
        self.add_widget(Label(text=s))

class ReadJournalApp(App):
	def build(self):
		self.rj = ReadJournal()
		return self.rj

if __name__ == "__main__":
	ReadJournalApp().run()




