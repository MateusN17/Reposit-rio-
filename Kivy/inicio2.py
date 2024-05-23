from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp

class YourApp(MDApp):
    def build(self):
        return Builder.load_file("mainscreen.kv")

if __name__ == "__main__":
    YourApp().run()
