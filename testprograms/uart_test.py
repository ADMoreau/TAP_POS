import serial
import time

serialport = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=2)

while True:

  #levels_string = input("Enter the level string")
  #print("Sending Text : {}".format(levels_string))
  #levels_string += '\n'
  #serialport.write(levels_string.encode())
  #time.sleep(.1)
  while (serialport.in_waiting > 0):
    #print(serialport.readline().decode(), end="")
    tap = int(serialport.readline().decode('ISO-8859-1', errors='replace')[:-2])
    print(tap)
    serialport.flush()
  time.sleep(2)

