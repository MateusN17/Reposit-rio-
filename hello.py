from kivy.app import App
#Nesta linha, você está importando a classe do App do módulo kivy.app. A classe App é fundamental para criar aplicativos Kivy.
from kivy.uix.button import Button
#Aqui, você está importando a classe Button do módulo kivy.uix.button. Essa classe representa um botão na interface gráfica.
class MyApp(App):
#Você está criando uma nova classe chamada MyApp que herda da classe App. Isso significa que MyApp é um aplicativo Kivy.
    def build(self):
    #Este é um método dentro da classe MyApp. O método build é obrigatório em qualquer aplicativo Kivy. Ele é chamdo quando o aplicativo é iniciado e deve retornar o widget raiz (interface original) do aplicativo
        return Button(text="Hello World! This is my first program in kivy \n I'm a SESIANO Student, and I love my teacher.")
    #Dentro do método build, você está criando um widget do tipo Button com o "texto" e retornando-o como widget raiz do seu aplicativo.
if __name__=="__main__":
    #esta linha verifica se o script está sendo executado diretamente (não importado como um módulo). Se for o caso, será executado
    MyApp().run()