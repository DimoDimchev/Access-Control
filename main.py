import serial


def close():
    if ser.is_open():
        ser.close()



def get_card_id():
    card_id_size = ser.in_waiting
    read_data = ser.read(card_id_size)

    # decodes the bytes to strings
    card_id = str(read_data, 'utf-8')
    card_id = card_id.encode("unicode_escape").decode("utf-8")

    # strips string from "?", "\n" and "\r"
    card_id = card_id.replace("?", '')
    card_id = card_id.replace("\\n", '')
    card_id = card_id.replace("\\r", '')

    return card_id


# opens port upon declaration
ser = serial.Serial('/dev/cu.usbserial-A703G1E6', baudrate=9600, timeout=0.1)

# while loop that will allow for the program to repeat itself an indefinite amount
while True:
    if ser.in_waiting == 19:
        # gets the card id
        print(get_card_id())

# closes the port if it's open
close()