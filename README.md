# Access-Control

## Introduction
This is my first real world project and it is part of an assesment of mine. Its purpose is to read a *card ID* using a card reader and depending on whether or not the card ID is present in a list of acceptable cards, a switch is turned on/off on a *UniPi Neuron S103* controller.

## Used technologies
The project is written entirely in the Python programming language using different modules such as `requests` and `serial`. The project follows an OOP structure.

## How to set it up
All of the information needed for the program to work can be adjusted in the `data.yaml` file. There you will find fields to enter the IP Adress of the controller, the network port that will be used, the major and minor indices of the circuit you want to run the program on, the port of the controller itself and a list of card IDs that have granted access.

The data.yaml will look something like this:
```json//
ip_address: "controller.ip.goes.here"
cards_with_access: ["example_card_id_1", "example_card_id_2"]
controller_port: "this/is/your_port"
network_port: 8080
major_index: 1
minor index: 1
expiration_time: 5
```
**Disclaimers:**
- All card IDs must contain 16 characters
- Depending on your OS the controller port will look differently
- The expiration time(the time in which the switch stays open) is in seconds

