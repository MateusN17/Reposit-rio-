from kivy.app import App
from kivy.uix.image import Image

class MinhaApp(App):
    def build(self):
        return Image(source="/Users/mateu/OneDrive/Imagens/Saved Pictures/foto1.jpg")
    
if __name__=="__main__":
    MinhaApp().run()