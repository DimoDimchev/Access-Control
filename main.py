#!/~/.pyenv/versions/3.9.1/bin/python
# -*- coding: <utf-8> -*-

import time
from controller import Controller
from reader import Reader

# reads an ip address from a text file and saves it in a variable
ip_data = open("ip_data.txt", "r")
ip_to_use = str(ip_data.readline())

# read all cards from a text file and add them to a list of card id's
card_id_data = open("card_id_data.txt", "r")
card_list = card_id_data.readlines()

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
        