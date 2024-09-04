from kivy.uix.screenmanager import Screen

class ProductSearchScreen(Screen):
    def search_product(self, product_name):
        product_name = product_name.strip().lower()
        # Lógica para buscar productos
        self.ids.search_result.text = f"Buscando {product_name}..."
