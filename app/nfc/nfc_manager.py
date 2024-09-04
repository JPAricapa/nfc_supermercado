import nfc

class NFCManager:
    def __init__(self):
        self.clf = nfc.ContactlessFrontend('usb')  # Cambiar 'usb' por la interfaz apropiada

    def read_nfc_tag(self, on_connect_callback):
        try:
            self.clf.connect(rdwr={'on-connect': on_connect_callback})
        except Exception as e:
            print("Error al leer la etiqueta NFC:", e)
