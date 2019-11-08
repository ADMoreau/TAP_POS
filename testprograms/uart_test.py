import serial
import time

serialport = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3.0)

while True:
  '''
  serialport.write("Good Idea".encode())
  rcv = serialport.read(100)
  serialport.write("Recieved: " + repr(rcv.decode()))
  '''

  #levels_string = input("Enter the level string")
  #print("Sending Text : {}".format(levels_string))
  #levels_string += '\n'
  serialport.flush()
  #serialport.write(levels_string.encode())
  #time.sleep(.1)
  while (serialport.in_waiting > 0):
    print(serialport.readline().decode(), end="")
  time.sleep(.1)

