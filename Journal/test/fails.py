from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os
class MyApp(App):
    def build(self):
        # r = self.initilize_global_vars()
        with open(os.path.join(os.getcwd(), "t.txt"), "w") as f:
        	f.write("please")
        return Button(text=os.getcwd())
        # return screen_manager

    # def initiliz/e_global_vars(self):
        # root_folder = self.user_data_dir
        # cache_folder = os.path.join(root_folder, 'test')
        # if not os.path.exists(cache_folder):
        #     os.makedirs(cache_folder)

        # with open(os.path.join(os.getcwd(), "t.txt"), "w") as f:
        # 	f.write("please")

        # return cache_folder

if __name__ == '__main__':
    MyApp().run()

# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# import os

# Builder.load_string('''
# <MenuScreen>:
#     BoxLayout:
#         Button:
#             text: '{}'
#             on_press: root.manager.current = 'add_staff'
#         Button:
#             text: 'View Staff Profile'
#         Button:
#             text: 'Salary report'

# <Add_new_staff>:
#     nam: str(name_input)
#     job: job_input
#     GridLayout:
#         cols: 2
#         Label:
#             text: 'Name'
#         TextInput:
#             id: name_input
#             multiline: False
#         Label:
#             text: 'Job'
#         TextInput:
#             id: job_input
#         Label:
#             text: 'Salary'
#         TextInput:
#         Label:
#             text: 'Date of Joining'
#         TextInput:
#         Button:
#             text: 'Back to menu'
#             on_press: root.manager.current = 'menu'
#         Button:
#             text: 'Save'
#             on_press: app.save(name_input.text, job_input.text)
# '''.format(os.getcwd()))


# class MenuScreen(Screen):
#     pass

# class Add_new_staff(Screen):
#     pass

# sm = ScreenManager()
# sm.add_widget(MenuScreen(name='menu'))
# sm.add_widget(Add_new_staff(name='add_staff'))

# class TestApp(App):
#     def build(self):
#         return sm

#     def save(self, name, job):
#         fob = open('test.txt','w')
#         fob.write(name + "\n")
#         fob.write(job)
#         fob.close()    

# if __name__ == '__main__':
#     TestApp().run()
# # # from kivy.storage.jsonstore import JsonStore
# # # from random import random
# # import kivy
# # kivy.require('1.0.0')

# # from kivy.app import App
# # from kivy.uix.button import Button

# # class MyApp(App):
# # 	def build(self):
# # 		# store = JsonStore("test.json")
# # 		# store.put('name', x=str(random()))
# # 		with open("test.txt", "w") as f:
# # 			f.write('x')
# # 		t="not found"
# # 		# if store.exists('name'):
# # 		# 	# print(store.get('name'))
# # 		# 	t = str(store.get('name'))
# # 		return Button(text=t)

# # if __name__ in ('__android__', '__main__'):
# # 	MyApp().run()



# # """

# # from kivy.app import App
# # from kivy.uix.gridlayout import GridLayout
# # from kivy.uix.label import Label
# # from kivy.graphics import Line, Color, Rectangle
# # from kivy.core.window import Window
# # from kivy.storage.jsonstore import JsonStore

# # from random import random

# # class JournalApp(App):
# # 	def build(self):
# # 		store = JsonStore("test.json")
# # 		store['ex'] = {'name': str(random())}
		
# # if __name__ == '__main__':
# # 	JournalApp().run()

# # class JournalUI(Widget):
# # 	pass

# # # jui = JournalUI()
# # # return jui
# # """
