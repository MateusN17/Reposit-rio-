from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
class MinhaApp(App):
    def build(self):
        return Label(text="Olá, SENAI!",font_size=50,halign="left",
                      valign="top", size_hint=(None, None), size=(300,100),text_size=(300,None),
                        font_name="Arial", color=get_color_from_hex("#FF5733"))
    
if __name__=="__main__":
    MinhaApp().run()