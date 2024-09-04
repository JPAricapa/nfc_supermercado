from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kv_string = '''
<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: '¡Bienvenido a la aplicación NFC!'
        Button:
            text: 'Escanear Producto'
            on_press: print('Escanear Producto presionado')
        Button:
            text: 'Ver Carrito de Compras'
            on_press: print('Ver Carrito de Compras presionado')
        Button:
            text: 'Ir a Pago'
            on_press: print('Ir a Pago presionado')
'''

class HomeScreen(Screen):
    pass

class NFCApp(App):
    def build(self):
        Builder.load_string(kv_string)  # Cargar desde la cadena

        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(HomeScreen(name="home"))
        return self.screen_manager

if __name__ == "__main__":
    NFCApp().run()
