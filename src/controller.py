#!/~/.pyenv/versions/3.9.1/bin/python
# -*- coding: <utf-8> -*-

# imports requests module
import requests

class Controller:
    def __init__(self, ip, major_index, minor_index, network_port):
        self.__ip_address = ip
        self.__digital_output = "rest/output/"
        self.__digital_input = "rest/input/"
        self.__network_port = network_port
        self.major_index = major_index
        self.minor_index = minor_index

    # gets the circuit that is needed to be used
    def get_circuit(self):
        if self.second_index < 10:
            circuit = f"{self.major_index}_0{self.minor_index}"
        else:
            circuit = f"{self.major_index}_{self.minor_index}"
        return circuit

    # constructs the uri
    def construct_uri(self):
        uri = f"http://{self.__ip_address}:{self.__network_port}/{self.__digital_output}{Controller.get_circuit(self)}"
        return uri 

    # turns switch on
    def turn_switch_on(self):
        response = requests.post(Controller.construct_uri(self), data={"value": 1, "mode": "Simple"})
        
    # turns switch off
    def turn_switch_off(self):
        response = requests.post(Controller.construct_uri(self), data={"value": 0, "mode": "Simple"})

        return 1
