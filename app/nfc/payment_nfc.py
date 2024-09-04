# payment_nfc.py
from .nfc_manager import NFCManager

class PaymentNFC:
    def __init__(self):
        self.nfc_manager = NFCManager()

    def process_payment(self):
        # Lógica para procesar el pago mediante NFC
        pass
