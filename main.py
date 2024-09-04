from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Definición de las pantallas de la aplicación
class MainMenu(Screen):
    pass

class ScanProductScreen(Screen):
    pass

class SearchProductScreen(Screen):
    pass

class CartScreen(Screen):
    pass

# Clase principal de la aplicación
class SupermercadoApp(App):
    def build(self):
        # Crear el ScreenManager
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(ScanProductScreen(name='scan_product'))
        sm.add_widget(SearchProductScreen(name='search_product'))
        sm.add_widget(CartScreen(name='cart'))
        return sm

if __name__ == '__main__':
    SupermercadoApp().run()
