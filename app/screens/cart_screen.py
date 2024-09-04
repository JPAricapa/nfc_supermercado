from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

class ShoppingCartScreen(Screen):
    carrito = []

    def on_pre_enter(self):
        self.update_cart()

    def update_cart(self):
        self.ids.cart_list.clear_widgets()
        for item in self.carrito:
            self.ids.cart_list.add_widget(Label(text=item))

    def add_to_cart(self, product):
        self.carrito.append(product)
        self.update_cart()
