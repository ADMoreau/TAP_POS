import serial
import time
import RPi.GPIO as GPIO
import threading

scrolltext = '/dev/ttyUSB-SCROLLTEXT'
scrolltext = serial.Serial(scrolltext, 9600, timeout=2)
time.sleep(.5)
print("Scrolltext connection established")

levels = '/dev/ttyUSB-MAINDISPLAY'
levels = serial.Serial(levels, 9600, timeout=2)
time.sleep(.5)
print("Levels connection established")

taps = '/dev/ttyS0'
taps = serial.Serial(taps, 9600, timeout=2)
time.sleep(.5)
print("Taps connection established")

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

segmentClocka=11
segmentLatcha=13
segmentDataa=15

segmentClockb=29
segmentLatchb=31
segmentDatab=33

segmentClockc=7
segmentLatchc=35
segmentDatac=37

GPIO.setup(segmentClocka,GPIO.OUT)
GPIO.setup(segmentDataa,GPIO.OUT)
GPIO.setup(segmentLatcha,GPIO.OUT)
GPIO.output(segmentClocka,GPIO.LOW)
GPIO.output(segmentDataa,GPIO.LOW)
GPIO.output(segmentLatcha,GPIO.LOW)

GPIO.setup(segmentClockb,GPIO.OUT)
GPIO.setup(segmentDatab,GPIO.OUT)
GPIO.setup(segmentLatchb,GPIO.OUT)
GPIO.output(segmentClockb,GPIO.LOW)
GPIO.output(segmentDatab,GPIO.LOW)
GPIO.output(segmentLatchb,GPIO.LOW)

GPIO.setup(segmentClockc,GPIO.OUT)
GPIO.setup(segmentDatac,GPIO.OUT)
GPIO.setup(segmentLatchc,GPIO.OUT)
GPIO.output(segmentClockc,GPIO.LOW)
GPIO.output(segmentDatac,GPIO.LOW)
GPIO.output(segmentLatchc,GPIO.LOW)
print("ABV display connected")

def showNumber(number):
  print("ABV = {}".format(number))

  a=1<<0
  b=1<<6
  c=1<<5
  d=1<<4
  e=1<<3
  f=1<<1
  g=1<<2
  dp=1<<7

  segments = [None, None, None]

  for i in range(len(number)):
    if   number[i] == 1: segments[i] =     b | c
    elif number[i] == 2: segments[i] = a | b |     d | e |     g
    elif number[i] == 3: segments[i] = a | b | c | d |         g
    elif number[i] == 4: segments[i] =     b | c |         f | g
    elif number[i] == 5: segments[i] = a |     c | d     | f | g
    elif number[i] == 6: segments[i] = a |     c | d | e | f | g
    elif number[i] == 7: segments[i] = a | b | c
    elif number[i] == 8: segments[i] = a | b | c | d | e | f | g
    elif number[i] == 9: segments[i] = a | b | c | d     | f | g
    elif number[i] == 0: segments[i] = a | b | c | d | e | f
    elif number[i] == ' ': segments[i] = 0
    elif number[i] == 'c': segments[i] = g | e | d
    elif number[i] == '-': segments[i] = g
    else : segments += False

  for s in range(8):
    GPIO.output(segmentClocka,GPIO.LOW)
    GPIO.output(segmentDataa,segments[0] & 1 << (7-s))
    GPIO.output(segmentClocka,GPIO.HIGH)

    GPIO.output(segmentClockb,GPIO.LOW)
    GPIO.output(segmentDatab,segments[1] & 1 << (7-s))
    GPIO.output(segmentClockb,GPIO.HIGH)

    GPIO.output(segmentClockc,GPIO.LOW)
    GPIO.output(segmentDatac,segments[2] & 1 << (7-s))
    GPIO.output(segmentClockc,GPIO.HIGH)

  GPIO.output(segmentLatcha,GPIO.LOW)
  GPIO.output(segmentLatcha,GPIO.HIGH)
  GPIO.output(segmentLatchb,GPIO.LOW)
  GPIO.output(segmentLatchb,GPIO.HIGH)
  GPIO.output(segmentLatchc,GPIO.LOW)
  GPIO.output(segmentLatchc,GPIO.HIGH)

def digit_cleanup():
  for _ in range(8):
    GPIO.output(segmentClocka,GPIO.LOW)
    GPIO.output(segmentDataa,0)
    GPIO.output(segmentClocka,GPIO.HIGH)

    GPIO.output(segmentClockb,GPIO.LOW)
    GPIO.output(segmentDatab,0)
    GPIO.output(segmentClockb,GPIO.HIGH)

    GPIO.output(segmentClockc,GPIO.LOW)
    GPIO.output(segmentDatac,0)
    GPIO.output(segmentClockc,GPIO.HIGH)

  GPIO.output(segmentLatcha,GPIO.LOW)
  GPIO.output(segmentLatcha,GPIO.HIGH)
  GPIO.output(segmentLatchb,GPIO.LOW)
  GPIO.output(segmentLatchb,GPIO.HIGH)
  GPIO.output(segmentLatchc,GPIO.LOW)
  GPIO.output(segmentLatchc,GPIO.HIGH)

def scroll(text):
  text += '\n'
  scrolltext.write(text.encode())
  time.sleep(.1)
  while (scrolltext.in_waiting > 0):
    print(scrolltext.readline().decode('ISO-8859-1', errors='replace'), end="")
  scrolltext.flush()

def display(i): 
  taps.flush()
  abv  = "888"
  abv_number = [int(i) for i in abv]
  showNumber(abv_number)
  if i == "0":
    levels.flush()
    levels_string = "1234530001"
    levels_string += '\n'
    levels.write(levels_string.encode())
    print(levels_string)
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Beer 0")
  elif i == "1":
    levels.flush()
    levels.write("2234530001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Beer 1")
  elif i == "2":
    levels.flush()
    levels.write("1235530001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Beer 2")
  elif i == "3":
    levels.flush()
    levels.write("5555530001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Beer 3")
  elif i == "4":
    levels.flush()
    levels.write("1211530001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Beer 4")
  elif i == "5":
    levels.flush()
    levels.write("5432130001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Beer 5")
  elif i == "6":
    levels.flush()
    levels.write("5434530001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Beer 6")
  elif i == "7":
    levels.flush()
    levels.write("3534530001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Beer 7")
  elif i == "31":
    levels.flush()
    levels.write("3534530001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("1836")
  elif i == 39:
    levels.flush()
    levels.write("3534530001\n".encode())
    while (levels.in_waiting > 0):
      print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
    levels.flush()
    scroll("Sam's Daily")
  time.sleep(6)
  levels.write("end\n".encode())
  #taps.write("end\n".encode())
  scroll(" ")
  #time.sleep(.1)
  while (levels.in_waiting > 0):
    print(levels.readline().decode('ISO-8859-1', errors='replace'), end="")
  levels.flush()
  #taps.flush()
  digit_cleanup()
  #i = None
  #break
  return

digit_cleanup()
scrolltext.flush()
while True:
  #taps.flushInput()
  #taps.flushOutput()
  if (taps.in_waiting > 0):
    i = taps.readline().decode('ISO-8859-1', errors='replace')
    print(int(i[:-2]))
    #time.sleep(1)
    display(int(i[:-2]))
    taps.flushInput()
    #taps.flushOutput()
    #if time.time() < timeout + 5 or i == None:
    #  i = taps.readline().decode()
    #  taps.flush()
    # try:
    #    print(i[0])
    #  except Exception as e:
    #    print(e)
    #else:
    #  timeout = time.time()
    #  assert(i != None)
    #t = threading.Thread(target=display, args=(i,))
    #t.start()
    #while (taps.in_waiting > 0):
    #    i = taps.readline().decode()
    #  #taps.flush()
    #elif timeout == 0 or time.time() >= timeout + 5:
