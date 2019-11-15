import serial
import time

taps = '/dev/ttyS0'
taps = serial.Serial(port = '/dev/serial0',
        baudrate = 115200,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout= 1)

time.sleep(.5)
print("Taps connection established")

while True:
  if (taps.in_waiting > 0):
    i = taps.readline().decode('ISO-8859-1', errors='replace').rstrip('\n')
    #i = taps.read(2).decode('ISO-8859-1', errors='replace').rstrip('\n')
    print(int(i))
    taps.flush()
    #print(int(i[:-2]))
