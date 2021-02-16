import serial
import requests
import time

class Reader:
    def __init__(self):
        self.ser = serial.Serial('/dev/cu.usbserial-A703G1E6', baudrate=9600, timeout=0.1)
        self.card_id = None
    

    def close(self):
        if self.ser.is_open():
            self.ser.close()
        

    def get_card_id(self):
        card_id_size = self.ser.in_waiting

        if card_id_size == 19:
            read_data = self.ser.read(card_id_size)

            # decodes the bytes to strings
            self.card_id = str(read_data, 'utf-8')
            self.card_id = self.card_id.encode("unicode_escape").decode("utf-8")

            # strips string from "?", "\n" and "\r"
            self.card_id = self.card_id.replace("?", '')
            self.card_id = self.card_id.replace("\\n", '')
            self.card_id = self.card_id.replace("\\r", '')

            return self.card_id


reader_test = Reader()

while True:
    card_id = reader_test.get_card_id()
    if card_id == "6E536046010080FF":
        # here will be the code that controls UniPy Neuron S103
        url = "http://192.168.0.53:8080/rest/output/1_01"
        response = requests.post(url, data={"value": 1, "mode": "Simple"})
        time.sleep(5)
        response = requests.post(url, data={"value": 0, "mode": "Simple"})