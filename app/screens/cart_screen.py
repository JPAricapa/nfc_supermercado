from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

class ShoppingCartScreen(Screen):
    carrito = []

    def on_pre_enter(self):
        self.update_cart()

    def update_cart(self):
        # Limpia el contenido anterior del carrito
        self.ids.cart_list.clear_widgets()
        for item in self.carrito:
            # Añade cada item al layout de la lista del carrito
            self.ids.cart_list.add_widget(Label(text=item))

    def add_to_cart(self, product):
        # Añadir producto al carrito
        self.carrito.append(product)
        self.update_cart()
