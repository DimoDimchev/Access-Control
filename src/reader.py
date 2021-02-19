#!/~/.pyenv/versions/3.9.1/bin/python
# -*- coding: <utf-8> -*-

# imports serial module
import serial

class Reader:
    def __init__(self, port):
        # declares and opens the port
        self.port = port
        self.ser = serial.Serial(str(self.port), baudrate=9600, timeout=0.1)
        self.card_id = None
    
    # checks if the port is open and if it is - closes it
    def close(self):
        if self.ser.is_open():
            self.ser.close()
        
    # reads the current card's id
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

