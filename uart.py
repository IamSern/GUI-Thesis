import serial


ser = serial.Serial(port='COM4', baudrate= 115200, bytesize= 8, 
                        timeout= 2, stopbits= serial.STOPBITS_ONE)

recevie = ser.read(4)
print(recevie)