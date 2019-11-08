import RPi.GPIO as GPIO


class DigitDisplay():
    '''
    This object will be the controller for the the digit display that displays the ABV value.
    ABV value is passed in as three integers with an automatic decimal point placed at the second digit.
    Each digit is a 7 segment display
    '''

    def __init__(self):
        print("Connecting to Digit Display")
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        self.segmentClocka=11
        self.segmentLatcha=13
        self.segmentDataa=15

        self.segmentClockb=29
        self.segmentLatchb=31
        self.segmentDatab=33

        self.segmentClockc=7
        self.segmentLatchc=35
        self.segmentDatac=37

        GPIO.setup(self.segmentClocka, GPIO.OUT)
        GPIO.setup(self.segmentDataa, GPIO.OUT)
        GPIO.setup(self.segmentLatcha, GPIO.OUT)
        GPIO.output(self.segmentClocka, GPIO.LOW)
        GPIO.output(self.segmentDataa, GPIO.LOW)
        GPIO.output(self.segmentLatcha, GPIO.LOW)

        GPIO.setup(self.segmentClockb, GPIO.OUT)
        GPIO.setup(self.segmentDatab, GPIO.OUT)
        GPIO.setup(self.segmentLatchb, GPIO.OUT)
        GPIO.output(self.segmentClockb, GPIO.LOW)
        GPIO.output(self.segmentDatab, GPIO.LOW)
        GPIO.output(self.segmentLatchb, GPIO.LOW)

        GPIO.setup(self.segmentClockc, GPIO.OUT)
        GPIO.setup(self.segmentDatac, GPIO.OUT)
        GPIO.setup(self.segmentLatchc, GPIO.OUT)
        GPIO.output(self.segmentClockc, GPIO.LOW)
        GPIO.output(self.segmentDatac, GPIO.LOW)
        GPIO.output(self.segmentLatchc, GPIO.LOW)

    def show_number(self, number):
        '''
        Sets the digits to the values in number
        :param number: list of three integers
        :return:
        '''

        a = 1 << 0
        b = 1 << 6
        c = 1 << 5
        d = 1 << 4
        e = 1 << 3
        f = 1 << 1
        g = 1 << 2
        dp = 1 << 7 # decimal point

        segments = [None, None, None]

        for i in range(len(number)):
            if number[i] == 1:
                segments[i] = b | c
            elif number[i] == 2:
                segments[i] = a | b | d | e | g
            elif number[i] == 3:
                segments[i] = a | b | c | d | g
            elif number[i] == 4:
                segments[i] = b | c | f | g
            elif number[i] == 5:
                segments[i] = a | c | d | f | g
            elif number[i] == 6:
                segments[i] = a | c | d | e | f | g
            elif number[i] == 7:
                segments[i] = a | b | c
            elif number[i] == 8:
                segments[i] = a | b | c | d | e | f | g
            elif number[i] == 9:
                segments[i] = a | b | c | d | f | g
            elif number[i] == 0:
                segments[i] = a | b | c | d | e | f
            elif number[i] == ' ':
                segments[i] = 0
            elif number[i] == 'c':
                segments[i] = g | e | d
            elif number[i] == '-':
                segments[i] = g
            else:
                segments += False
            segments[i] = segments[i] | dp

        # temp = segments[1]
        # temp = temp | dp

        for s in range(8):
            GPIO.output(self.segmentClocka, GPIO.LOW)
            GPIO.output(self.segmentDataa, segments[0] & 1 << (7 - s))
            GPIO.output(self.segmentClocka, GPIO.HIGH)

            GPIO.output(self.segmentClockb, GPIO.LOW)
            GPIO.output(self.segmentDatab, segments[1] & 1 << (7 - s))
            GPIO.output(self.segmentClockb, GPIO.HIGH)

            GPIO.output(self.segmentClockc, GPIO.LOW)
            GPIO.output(self.segmentDatac, segments[2] & 1 << (7 - s))
            GPIO.output(self.segmentClockc, GPIO.HIGH)

        GPIO.output(self.segmentLatcha, GPIO.LOW)
        GPIO.output(self.segmentLatcha, GPIO.HIGH)
        GPIO.output(self.segmentLatchb, GPIO.LOW)
        GPIO.output(self.segmentLatchb, GPIO.HIGH)
        GPIO.output(self.segmentLatchc, GPIO.LOW)
        GPIO.output(self.segmentLatchc, GPIO.HIGH)

    def digit_cleanup(self):
        for _ in range(8):
            GPIO.output(self.segmentClocka,GPIO.LOW)
            GPIO.output(self.segmentDataa,0)
            GPIO.output(self.segmentClocka,GPIO.HIGH)

            GPIO.output(self.segmentClockb,GPIO.LOW)
            GPIO.output(self.segmentDatab,0)
            GPIO.output(self.segmentClockb,GPIO.HIGH)

            GPIO.output(self.segmentClockc,GPIO.LOW)
            GPIO.output(self.segmentDatac,0)
            GPIO.output(self.segmentClockc,GPIO.HIGH)

        GPIO.output(self.segmentLatcha,GPIO.LOW)
        GPIO.output(self.segmentLatcha,GPIO.HIGH)
        GPIO.output(self.segmentLatchb,GPIO.LOW)
        GPIO.output(self.segmentLatchb,GPIO.HIGH)
        GPIO.output(self.segmentLatchc,GPIO.LOW)
        GPIO.output(self.segmentLatchc,GPIO.HIGH)
