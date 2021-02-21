from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

KV = """
MDScreen:

    FitImage:
        source: 'fon.jpg'

    MDRaisedButton:
        text: "CLICK ME"
        pos_hint: {"center_x": .5, "center_y": .5}
"""
class Container(BoxLayout):

    pass

class MainApp(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)


MainApp().run()