from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_string('''
<RoundButton>:
    canvas.before:
        Color:
            rgba: 0.4, 0.4, 0.4, 1  # cor do botão
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [20,]
''')


class RoundButton(Button):
    pass


class TestApp(App):
    def build(self):
        return RoundButton(text='Clique aqui', size_hint=(None, None), size=(150, 50),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})


if __name__ == '__main__':
    TestApp().run()
