from kivy.config import Config
Config.set('graphics', 'width', '440')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class TelaInicio(Screen):
    def __init__(self, **kwargs):
        super(TelaInicio, self).__init__(**kwargs)

        # Adicionando imagem clicável
        self.imagem = ImageButton(
            source="/Users/mateu/Downloads/add-bell-notification--notification-alarm-alert-bell-add.png",
            size_hint=(None, None),  # Define o tamanho da imagem
            size=(50, 50),         # Define o tamanho da imagem
            pos_hint={'top': 1, 'right': 1}  # Posiciona a imagem no canto superior direito
        )
        self.imagem.bind(on_release=self.on_icon_click)  # Ligando o evento on_release da imagem a on_icon_click
        self.add_widget(self.imagem)

        # Adicionando caixa de pesquisa com imagem da lupa
        self.pesquisa = TextInput(hint_text="Pesquisar", multiline=False, size_hint=(None, None), size=(350, 30), 
                                  pos_hint={'top': 0.9, 'right': .9}, background_active="/Users/mateu/Downloads/Rectangle 5.png", 
                                  background_normal='/Users/mateu/Downloads/Rectangle 5.png',)
        self.add_widget(self.pesquisa)

        # Adicionando ScrollView como um widget na tela
        scroll_layout = GridLayout(cols=1, spacing=20, size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))
        scroll_view = ScrollView(size_hint=(None, None), size=(300, 400), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        scroll_view.add_widget(scroll_layout)
        self.add_widget(scroll_view)

        # Adicionando 20 instâncias de ImageButtonWithImage
        for i in range(20):
            image_button = ImageButtonWithImage(image_source='/Users/mateu/Downloads/doação.png',  size_hint_y=None, height=150)
            scroll_layout.add_widget(image_button)

        # Adicionando a barra de ícones na parte inferior
        bottom_bar_layout = GridLayout(cols=5, size_hint_y=None, height=100)
        self.add_widget(bottom_bar_layout)

        # Adicionando os ícones separados na barra inferior
        lista=['perfil.png','chats.png','mais.png','home.png']
        for icon_name in lista:
            icon_button = ImageButton(source=icon_name, size_hint=(None,None), size=(100,40))
            icon_button.bind(on_press=self.on_icon_click)  # Adicionando a função de clique
            bottom_bar_layout.add_widget(icon_button)

    def on_icon_click(self, instance):
        app = App.get_running_app()
        if instance.source == 'home.png':
            app.root.current = 'tela_home'
        elif instance.source == 'mais.png':
            app.root.current = 'tela_mais'
        elif instance.source == 'perfil.png':
            app.root.current = 'tela_perfil'
        elif instance.source == 'chats.png':
            app.root.current = 'tela_chats'

class ImageButton(ButtonBehavior, Image):
    pass

class ImageButtonWithImage(ButtonBehavior, BoxLayout):
    def __init__(self, image_source, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        # Adicionando uma imagem ao layout da caixa
        self.image = Image(source=image_source)
        self.add_widget(self.image)

class TelaHome(Screen):
    pass

class TelaMais(Screen):
    pass

class TelaPerfil(Screen):
    pass

class TelaChats(Screen):
    pass

class GerenciadorTelas(ScreenManager):
    pass

class Umatela(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.root = GerenciadorTelas()

        # Criando as telas
        tela_inicio = TelaInicio(name='tela_inicio')
        tela_home = TelaHome(name='tela_home')
        tela_mais = TelaMais(name='tela_mais')
        tela_perfil = TelaPerfil(name='tela_perfil')
        tela_chats = TelaChats(name='tela_chats')

        # Adicionando as telas ao gerenciador
        self.root.add_widget(tela_inicio)
        self.root.add_widget(tela_home)
        self.root.add_widget(tela_mais)
        self.root.add_widget(tela_perfil)
        self.root.add_widget(tela_chats)

        # Retornando a tela inicial
        return self.root

if __name__ == '__main__':
    Umatela().run()