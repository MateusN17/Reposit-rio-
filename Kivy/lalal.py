from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

# Carregando o arquivo KV
Builder.load_file('lalal.kv')

class MyScrollView(ScrollView):
    pass

class ScrollViewApp(App):
    def build(self):
        return MyScrollView()

if __name__ == '__main__':
    ScrollViewApp().run()