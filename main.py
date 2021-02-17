#!/~/.pyenv/versions/3.9.1/bin/python
# -*- coding: <utf-8> -*-

import time
import yaml
from controller import Controller
from reader import Reader

# opens data.yaml and parses it
data_yaml = open("data.yaml", "r")
parsed_data = yaml.load(data_yaml, Loader=yaml.FullLoader)

# reads an ip address from the yaml file and saves it in a variable
ip_to_use = parsed_data.get("ip_address")

# read all cards from a yaml file and add them to a list of card id's
card_list = parsed_data.get("cards_with_access")

controller = Controller(ip_to_use)
reader = Reader()

while True:
    card_id = reader.get_card_id()
    if card_id in card_list:
        controller.turn_switch_on()
        time.sleep(5)
        controller.turn_switch_off()
    elif card_id not in card_list and card_id is not None:
        print("0")
        