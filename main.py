import serial

# empty string that will contain the card 
tag_id = ""
ser = serial.Serial('/dev/cu.usbserial-A703G1E6')       
# for loop that will receive all 16 bites from the card reader   
for i in range(16):
    read_data = ser.read()
    # decodes the bytes to strings
    char = read_data.decode("utf-8")
    # concatenates the current byte to the rest of the bytes
    tag_id += char
# closes the port
ser.close() 
print(tag_id)
