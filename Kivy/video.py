from kivy.app import App
from kivy.uix.video import Video
class MinhaApp(App):
    def build(self):
        return Video(source="\Users\mateu\Downloads\PXL_20240417_160011210~2.mp4")

if __name__=="__main__":
    MinhaApp().run()