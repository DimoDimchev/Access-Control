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


class Controller:
    def __init__(self, url_address):
        self.url_address = url_address
    
    def card_accepted(self):
        response = requests.post(self.url_address, data={"value": 1, "mode": "Simple"})
        time.sleep(5)
        response = requests.post(self.url_address, data={"value": 0, "mode": "Simple"})

        return 1
    
    def card_unaccepted(self):
        return 0


# reads an ip address from a text file and saves it in a variable
ip_data = open("ip_data.txt", "r")
ip_to_use = str(ip_data.readline())

# read all cards from a text file and add them to a list of card id's
card_id_data = open("card_id_data.txt", "r")
card_list = card_id_data.readlines()

reader = Reader()
controller = Controller(f"http://{ip_to_use}:8080/rest/output/1_01")

while True:
    card_id = reader.get_card_id()
    if card_id in card_list:
        print(controller.card_accepted())
    elif card_id not in card_list and card_id is not None:
        print(controller.card_unaccepted())
        
        