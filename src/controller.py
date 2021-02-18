#!/~/.pyenv/versions/3.9.1/bin/python
# -*- coding: <utf-8> -*-

# imports requests module
import requests

class Controller:
    def __init__(self, ip, first_index, second_index):
        self.__ip_address = str(ip)
        self.__digital_output = "rest/output/"
        self.__digital_input = "rest/input/"
        self.first_index = int(first_index)
        self.second_index = int(second_index)

    # gets the circuit that is needed to be used
    def get_circuit(self):
        if self.second_index < 10:
            circuit = f"{self.first_index}_0{self.second_index}"
        else:
            circuit = f"{self.first_index}_{self.second_index}"
        return circuit

    # constructs the uri
    def construct_uri(self):
        uri = f"http://{self.__ip_address}:8080/{self.__digital_output}{Controller.get_circuit(self)}"
        return uri 

    # turns switch on
    def turn_switch_on(self):
        response = requests.post(Controller.construct_uri(self), data={"value": 1, "mode": "Simple"})
        
    # turns switch off
    def turn_switch_off(self):
        response = requests.post(Controller.construct_uri(self), data={"value": 0, "mode": "Simple"})

        return 1
