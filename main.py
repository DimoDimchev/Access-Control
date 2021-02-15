import serial

def check_if_closed():
    if ser.is_open():
        ser.close()
    else:
        ser.open()

def get_card_id():
    card_id_size = ser.in_waiting
    read_data = ser.read(size=card_id_size)

    # decodes the bytes to strings
    card_id = str(read_data, 'utf-8')
    
    # strips string from "?", "\n" and "\r"
    for char in card_id:
        if char in "?\n\r":
            card_id = card_id.replace(char,'')

    return card_id


# opens port upon declaration
ser = serial.Serial('/dev/cu.usbserial-A703G1E6', baudrate=9600, timeout=0.03)

# while loop that will allow for the program to repeat itself an indefinite amount
while True:  
    if ser.in_waiting:
        # gets the card id
        print(get_card_id())

# closes the port if it's open
check_if_closed()