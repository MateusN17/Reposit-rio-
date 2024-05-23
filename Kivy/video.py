from kivy.app import App
from kivy.uix.video import Video

class VideoPlayer(App):
    def build(self):
        video.state="play"
        video= Video(source="/Users/mateu/Downloads/ok.mp4")

if __name__ == '__main__':
    VideoPlayer().run()