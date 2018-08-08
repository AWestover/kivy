from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App


class Journal(GridLayout):
    def __init__(self, **kwargs):
        super(Journal, self).__init__(**kwargs)
        self.cols = 2
        self.row = 2

        self.english_a = Label(text='English')
        self.add_widget(self.english_a)

        self.english = TextInput(multiline=False)
        self.add_widget(self.english)
        
        self.caesar_a = Label(text='Caesar')
        self.add_widget(self.caesar_a)
        
        self.caesar = TextInput(multiline=False)
        self.add_widget(self.caesar)

        self.e_c = Button(text="Encrypt (Binary Inverse Shifter)")
        self.e_c.bind(on_press=self.encrypt)
        self.add_widget(self.e_c)

        self.c_e = Button(text="Encrypt (Mod 26)")
        self.c_e.bind(on_press=self.decrypt)
        self.add_widget(self.c_e)


    def flip_bit(self, bit):
        o = {
            "1":"0",
            "0":"1"
        }
        return o[bit]

    def bin_inverse(self, num):
        inv = ""
        for c in num:
            inv+=flip_bit(c)
        return inv

    def chr_to_bin(self, ch):
        temp = bin(ord(ch)-ord('a'))[2:]
        return "0"*(5-len(temp))+temp
    
    def shift_invert_chr(self, ch):
        temp = 25 - (ord(ch) - ord('a')) # reflect
        temp = bin(temp)[2:]
        return "0"*(5-len(temp))+temp


    def mod_slide_chr(self, ch):
        # if ch == ' ':  # 26th character....
        temp = ((ord(ch) - ord('a')) + 13) % 26
        temp = bin(temp)[2:]
        return "0"*(5-len(temp))+temp

    def bin_to_ch(self, bi):
        return chr(int(bi, 2) + ord('a'))


    def encrypt(self, instance):
        msg = self.english.text
        intermediate = []
        new_msg = ""
        for ch in msg:
            if self.isChar(ch):
                intermediate.append(self.shift_invert_chr(ch))
                new_msg += self.bin_to_ch(intermediate[-1])
            else:
                intermediate.append(ch)
                new_msg += intermediate[-1]

        pp = "".join(intermediate)

        self.english_a.text = new_msg

        popup = Popup(title="Encrypting",
            content=Label(text=pp),
            size=(100, 100),
            size_hint=(0.3, 0.3),
            auto_dismiss=True)
        popup.open()

    def decrypt(self, instance):
        msg = self.caesar.text
        intermediate = []
        new_msg = ""
        for ch in msg:
            if self.isChar(ch):
                intermediate.append(self.mod_slide_chr(ch))
                new_msg += self.bin_to_ch(intermediate[-1])
            else:
                intermediate.append(ch)
                new_msg += intermediate[-1]

        pp = "".join(intermediate)

        self.caesar_a.text = new_msg

        popup = Popup(title="Encrypting",
            content=Label(text=pp),
            size=(100, 100),
            size_hint=(0.3, 0.3),
            auto_dismiss=True)
        popup.open()


    def isChar(self, ch, space_allowed=False):
        if space_allowed:
            if ch == ' ':
                return True
        try:
            ch = str(ch)
        except:
            return False
        if type(ch) != type('a'):
            return False
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            return True
        return False


class JournalApp(App):
    def build(self):
        self.journal = Journal()
        return self.journal

if __name__ == '__main__':
    JournalApp().run()


