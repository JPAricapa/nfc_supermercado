from kivy.uix.screenmanager import Screen

class PaymentScreen(Screen):
    def process_payment(self):
        print("Procesando pago con tarjeta NFC...")
        self.ids.payment_result.text = "Pago realizado con éxito."
