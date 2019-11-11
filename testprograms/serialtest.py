import time
import serial


#port = '/dev/ttyUSB-MAINDISPLAY'
port = '/dev/ttyUSB-SCROLLTEXT'
levelsDisplay = serial.Serial(port, 9600, timeout=1)
time.sleep(.5)


while True:
  levels_string = input("Enter the level string")
  print("Sending Text : {}".format(levels_string))
  levels_string += '\n'
  levelsDisplay.flush()
  levelsDisplay.write(levels_string.encode())
  time.sleep(.1)
  while (levelsDisplay.in_waiting > 0):
    print(levelsDisplay.readline().decode(encoding = "ISO-8859-1", errors='replace')) #, end="")
  time.sleep(.1)
  levelsDisplay.flush()

