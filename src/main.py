#!/~/.pyenv/versions/3.9.1/bin/python
# -*- coding: <utf-8> -*-

# imports time and yaml modules
import time
import yaml
# imports Controller and Reader class from controller.py and reader.py
from controller import Controller
from reader import Reader

def main():
    # opens data.yaml and parses it
    data_yaml = open("data/data.yaml", "r")
    parsed_data = yaml.load(data_yaml, Loader=yaml.FullLoader)

    # reads an ip address from the yaml file and saves it in a variable
    ip_to_use = parsed_data.get("ip_address")

    # read all cards from a yaml file and add them to a list of card ids
    card_list = parsed_data.get("cards_with_access")

    controller = Controller(ip_to_use, 1, 1)
    reader = Reader()

    # while loop to keep the program running indefinetely
    while True:
        card_id = reader.get_card_id()
        if card_id in card_list:
            controller.turn_switch_on()
            time.sleep(5)
            controller.turn_switch_off()
        elif card_id not in card_list and card_id is not None:
            print("0")


if __name__== "__main__":
  main()