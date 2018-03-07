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
data_folder = "test"

jsonf = join(data_folder, "hello.json")
txtf  = join(os.getcwd(), join(data_folder, "test.txt"))

class Journal(GridLayout):
    def __init__(self, **kwargs):
        super(Journal, self).__init__(**kwargs)
        self.cols = 2
        self.row = 2
        self.add_widget(Label(text='Entry'))
        self.entry = TextInput(multiline=False)
        self.add_widget(self.entry)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.hello = Button(text="hello")
        self.hello.bind(on_press=self.auth)
        self.add_widget(self.hello)

    def auth(self, instance):
        if self.password.text == "alek":
            self.write_entry()
            popup = Popup(title="success",
                content=Label(text="Howdy !"),
                size=(100, 100),
                size_hint=(0.3, 0.3),
                auto_dismiss=True)
            popup.open()

    def write_entry(self):
        with open(jsonf) as f:
            j = json.load(f)
        try:
            j["Alek"].append(self.entry.text)
        except KeyError:
            j["Alek"] = [self.entry.text]
        with open(jsonf, "w") as f:
            json.dump(j, f, indent=4)


class JournalApp(App):
    def build(self):
        self.journal = Journal()
        # with open(jsonf, "w") as f:
        #     json.dump({'x':4, 'y':5}, f, indent=4)
        with open(txtf, "w") as f:
            f.write("please or not")
        return self.journal

if __name__ == '__main__':
    JournalApp().run()


