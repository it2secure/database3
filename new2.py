from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

import random

root_widget = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'Hello'  #How to define it?
        font_size: 30
    Button:
        size: root.width/2, 15
        text: 'next random'
        font_size: 30
#        on_release:  #How to define it?
''')

class TestApp(App):
    def build(self):
        return root_widget

if __name__ == '__main__':
    TestApp().run()