from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
import pyrebase
from google.cloud import firestore
import os

# Configuração do Firebase
firebase_config = {
    "apiKey": "AIzaSyDGIpe8MXvlfSf0hlMDQpzYfxqJQW5Slz4",
    "authDomain": "doaacao-d8007.firebaseapp.com",
    "projectId": "doaacao-d8007",
    "storageBucket": "doaacao-d8007.appspot.com",
    "messagingSenderId": "514229025973",
    "appId": "1:514229025973:web:45aeba200277c3281fd2fc",
    "measurementId": "G-XBHH0SL00T",
    "databaseURL": "https://doaacao-d8007.firebaseio.com"
}

# Inicialize Pyrebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Inicialize Firestore
cred_path = "doaacao-d8007-firebase-adminsdk-f1gr1-1ab0f75f14.json"  # Caminho para o arquivo de chave de conta de serviço
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path
firestore_client = firestore.Client()

class SplashScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    dialog = None

    def login_user(self):
        email = self.ids.login_email.text
        password = self.ids.login_password.text

        try:
            auth.sign_in_with_email_and_password(email, password)
            self.manager.current = 'menu_screen'
        except Exception as e:
            self.show_error_dialog("Email ou senha incorretos")

    def show_error_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.text = message
        self.dialog.open()

class RegisterScreen(MDScreen):
    dialog = None

    def register_user(self):
        email = self.ids.email_field.text
        password = self.ids.password_field.text
        confirm_password = self.ids.confirm_password_field.text
        username = self.ids.username_field.text  # Obtendo o nome de usuário

        if password != confirm_password:
            self.show_error_dialog("As senhas não coincidem")
            return
        
        try:
            user = auth.create_user_with_email_and_password(email, password)
            
            # Salvar o nome de usuário, email e senha no Firestore
            user_id = user['localId']
            user_ref = firestore_client.collection("users").document(user_id)
            user_ref.set({
                "username": username,
                "email": email,
                "password": password
            })
            
            self.manager.current = 'login_screen'
        except Exception as e:
            self.show_error_dialog(f"Erro ao criar usuário: {e}")

    # Método show_error_dialog() e outros métodos auxiliares permanecem inalterados...


    def show_error_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.text = message
        self.dialog.open()

class EditarPerfil(MDScreen):
    dialog = None

    def save_profile_changes(self):
        # Acessando os IDs dos widgets dentro da tela EditarPerfil
        new_username = self.ids.new_username.text
        new_email = self.ids.new_email.text
        new_password = self.ids.new_password.text
        
        # Verifica se os valores foram capturados corretamente
        print("Novo nome de usuário:", new_username)
        print("Novo email:", new_email)
        print("Nova senha:", new_password)

        try:
            if new_email:
                user_id = auth.current_user['localId']
                user_ref = firestore_client.collection("users").document(user_id)
                user_ref.update({"email": new_email})
            if new_password:
                user_id = auth.current_user['localId']
                user_ref = firestore_client.collection("users").document(user_id)
                user_ref.update({"password": new_password})
            if new_username:
                # Atualizar dados no Firestore
                user_id = auth.current_user['localId']
                user_ref = firestore_client.collection("users").document(user_id)
                user_ref.update({"username": new_username})

            self.manager.current = 'menu_screen'
        except Exception as e:
            self.show_error_dialog(f"Erro ao atualizar perfil: {e}")

    def show_error_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.text = message
        self.dialog.open()



class MenuScreen(MDScreen):
    pass

class CriacaoCampanha(MDScreen):
    pass

class MinhasCampanhas(MDScreen):
    pass

class MinhasDoacoes(MDScreen):
    pass

class Favoritos(MDScreen):
    pass

class Configuracoes(MDScreen):
    pass


class MyApp(MDApp):
    dialog = None
    
    def build(self):
        Window.size = (dp(300), dp(600))  
        Window.clearcolor = (1, 1, 1, 1)
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file("registerscreen.kv")
        global sm
        sm = MDScreenManager()
        sm.add_widget(SplashScreen(name='splash_screen'))
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(RegisterScreen(name='register_screen'))
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(EditarPerfil(name='editar_perfil'))
        sm.add_widget(MinhasCampanhas(name='minhas_campanhas'))
        sm.add_widget(MinhasDoacoes(name='minhas_doacoes'))
        sm.add_widget(Favoritos(name='favoritos'))
        sm.add_widget(Configuracoes(name='configuracoes'))
        sm.add_widget(CriacaoCampanha(name='criacao_campanha'))

        return sm
    
    def on_start(self):
        Clock.schedule_once(self.change_screen, 3)

    def change_screen(self, dt):
        sm.current = 'login_screen'
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Tem certeza que você quer sair da sua conta?",
                buttons=[
                    MDFlatButton(
                        text="CANCELAR",
                        theme_text_color="Custom",
                        text_color='#008080',
                    ),
                    MDFlatButton(
                        text="SAIR",
                        theme_text_color="Custom",
                        text_color='#008080',
                    ),
                ],
            )
        self.dialog.open()

if __name__ == "__main__":
    MyApp().run()