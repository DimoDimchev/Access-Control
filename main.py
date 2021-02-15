import serial

ser = serial.Serial('/dev/cu.usbserial-A703G1E6', baudrate=9600, timeout=0.03)    


# while loop that will allow for the program to repeat itself an indefinite amount
while True:

    # empty string that will contain the card 
    tag_id = ""   
    card_id_size = ser.in_waiting()

    read_data = ser.read(card_id_size)
    # decodes the bytes to strings
    char = read_data.decode("utf-8")

    # concatenates the current byte to the rest of the bytes
    tag_id += char

# closes the port
ser.close() 

print(tag_id)
