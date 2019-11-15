import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setmode(GPIO.BOARD)

segmentClocka=29
segmentLatcha=31
segmentDataa=33

segmentClockb=11
segmentLatchb=13
segmentDatab=15

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

number=0

print(number)

a=1<<0
b=1<<6
c=1<<5
d=1<<4
e=1<<3
f=1<<1
g=1<<2
dp=1<<7

x = 0
while True:
	'''
	GPIO.output(segmentClocka,GPIO.LOW)
	GPIO.output(segmentDataa,1 << (7-s))
	GPIO.output(segmentClocka,GPIO.HIGH)

	GPIO.output(segmentClockb,GPIO.LOW)
	GPIO.output(segmentDatab,1 << (7-s))
	GPIO.output(segmentClockb,GPIO.HIGH)

	GPIO.output(segmentClockc,GPIO.LOW)
	GPIO.output(segmentDatac,1 << (7-s))
	GPIO.output(segmentClockc,GPIO.HIGH)
	'''
	print("X = " + str(x))
	time.sleep(1)
	x = (x+1) % 10

	segments = [None, None, None]

	for i in range(len(segments)):
		if   x == 1: segments[i] =     b | c
		elif x == 2: segments[i] = a | b |     d | e |     g
		elif x == 3: segments[i] = a | b | c | d |         g
		elif x == 4: segments[i] =     b | c |         f | g
		elif x == 5: segments[i] = a |     c | d     | f | g
		elif x == 6: segments[i] = a |     c | d | e | f | g
		elif x == 7: segments[i] = a | b | c
		elif x == 8: segments[i] = a | b | c | d | e | f | g
		elif x == 9: segments[i] = a | b | c | d     | f | g
		elif x == 0: segments[i] = a | b | c | d | e | f
		elif x == ' ': segments[i] = 0
		elif x == 'c': segments[i] = g | e | d
		elif x == '-': segments[i] = g
		else : segments += False
	segments[1] = segments[1] | dp

	for j in range(8):
		GPIO.output(segmentClocka,GPIO.LOW)
		GPIO.output(segmentDataa,segments[0] & 1 << (7-j))
		GPIO.output(segmentClocka,GPIO.HIGH)

		GPIO.output(segmentClockb,GPIO.LOW)
		GPIO.output(segmentDatab,segments[1] & 1 << (7-j))
		GPIO.output(segmentClockb,GPIO.HIGH)

		GPIO.output(segmentClockc,GPIO.LOW)
		GPIO.output(segmentDatac,segments[2] & 1 << (7-j))
		GPIO.output(segmentClockc,GPIO.HIGH)

	GPIO.output(segmentLatcha,GPIO.LOW)
	GPIO.output(segmentLatcha,GPIO.HIGH)
	GPIO.output(segmentLatchb,GPIO.LOW)
	GPIO.output(segmentLatchb,GPIO.HIGH)
	GPIO.output(segmentLatchc,GPIO.LOW)
	GPIO.output(segmentLatchc,GPIO.HIGH)

	time.sleep(1)
	
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
	
