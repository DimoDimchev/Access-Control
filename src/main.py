#!/~/.pyenv/versions/3.9.1/bin/python
# -*- coding: <utf-8> -*-

# imports the yaml module
import yaml
# imports Controller, Timer and Reader class from controller.py and reader.py
from controller import Controller
from reader import Reader
from timer import Timer

def main():
    # opens data.yaml and parses it
    data_yaml = open("data/data.yaml", "r")
    parsed_data = yaml.load(data_yaml, Loader=yaml.FullLoader)

    # read an ip address from the data.yaml file and save it in a variable
    ip_to_use = parsed_data.get("ip_address")

    # read all cards from the data.yaml file and save them to a list
    card_list = parsed_data.get("cards_with_access")

    # read the port that will be used from the data.yaml file and save it in a variable
    port_to_use = parsed_data.get("port")

    controller = Controller(ip_to_use, 1, 1)
    reader = Reader(port_to_use)
    timer = Timer(5)

    # while loop to keep the program running indefinetely
    while True:
        card_id = reader.get_card_id()
        if card_id in card_list:
            controller.turn_switch_on()
            # checks if the required time has elapsed
            if timer.update():
                controller.turn_switch_off()
                break
        elif card_id not in card_list and card_id is not None:
            print("0")


if __name__== "__main__":
  main()