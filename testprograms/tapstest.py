import serial
import time

taps = '/dev/ttyS0'
taps = serial.Serial(taps, 9600, timeout=2)
time.sleep(.5)
print("Taps connection established")

while True:
  if (taps.in_waiting > 0):
    i = taps.readline().decode('ISO-8859-1', errors='replace')
    print(int(i))
    #print(int(i[:-2]))
