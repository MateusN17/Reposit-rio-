from kivy.app import App
from kivy.uix.video import Video

class VideoPlayer(App):
    def build(self):
        return Video(source='', state='play')

if __name__ == '__main__':
    VideoPlayer().run()