from .nfc_manager import NFCManager

class PaymentNFC:
    def __init__(self):
        self.nfc_manager = NFCManager()

    def process_payment(self):
        # Lógica para procesar el pago mediante NFC
        print("Procesando pago con NFC...")
