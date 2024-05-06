from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label

class MyLabel(Label):
    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def on_pos(self, *args):
        self.rect.pos = self.pos

    def on_size(self, *args):
        self.rect.size = self.size

        
class MyApp(App):
    def build(self):
        return MyLabel(text='Hello world',)

if __name__ == '__main__':
    MyApp().run()