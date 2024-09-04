from kivy.uix.screenmanager import Screen

# Definir los productos y ubicaciones
ubicaciones = {
    'Shampoo': 'Pasillo 1 - Aseo personal',
    'Jabón': 'Pasillo 1 - Aseo personal',
    'Pasta dental': 'Pasillo 1 - Aseo personal',
    'Crema corporal': 'Pasillo 1 - Aseo personal',
    'Detergente': 'Pasillo 2 - Productos del hogar',
    'Esponja': 'Pasillo 2 - Productos del hogar',
    'Limpiavidrios': 'Pasillo 2 - Productos del hogar',
    'Bolsas de basura': 'Pasillo 2 - Productos del hogar',
    'Chocolates': 'Pasillo 3 - Dulcería',
    'Galletas': 'Pasillo 3 - Dulcería',
    'Caramelos': 'Pasillo 3 - Dulcería',
    'Chicles': 'Pasillo 3 - Dulcería',
    'Refresco': 'Pasillo 4 - Bebidas',
    'Jugo': 'Pasillo 4 - Bebidas',
    'Agua mineral': 'Pasillo 4 - Bebidas',
    'Energizante': 'Pasillo 4 - Bebidas',
    'Vino tinto': 'Pasillo 5 - Licores',
    'Vodka': 'Pasillo 5 - Licores',
    'Whisky': 'Pasillo 5 - Licores',
    'Cerveza': 'Pasillo 5 - Licores',
    'Atún': 'Pasillo 6 - Enlatados',
    'Maíz': 'Pasillo 6 - Enlatados',
    'Chícharos': 'Pasillo 6 - Enlatados',
    'Frijoles': 'Pasillo 6 - Enlatados',
    'Vainilla': 'Pasillo 7 - Helados',
    'Chocolate': 'Pasillo 7 - Helados',
    'Fresa': 'Pasillo 7 - Helados',
    'Limón': 'Pasillo 7 - Helados',
    'Arroz': 'Pasillo 8 - Granos',
    'Frijol': 'Pasillo 8 - Granos',
    'Lentejas': 'Pasillo 8 - Granos',
    'Quinoa': 'Pasillo 8 - Granos'
}

class ProductSearchScreen(Screen):
    def search_product(self, product_name):
        product_name = product_name.strip().lower()
        found_products = [product for product in ubicaciones if product.lower() == product_name]

        if found_products:
            producto_encontrado = found_products[0]
            self.ids.search_result.text = f"Producto '{producto_encontrado}' encontrado en {ubicaciones[producto_encontrado]}."
        else:
            self.ids.search_result.text = "Producto no encontrado. Intente nuevamente."
