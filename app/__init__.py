import time
import serial

from app.arduino import Arduino
from app.digit_display import DigitDisplay

patterns = ['bpm', 'radialpatternshift', 'juggle']

try:
    '''
    connect to and set the serial connection between the raspberry pi and teensy boards
    
    scroll_text = teensy 3.2
    led_display = teensy 3.6
    '''
    print('Connecting to Arduinos')
    port = '/dev/ttyACM0'
    scroll_text_arduino = serial.Serial(port, 9600, timeout=1)
    time.sleep(.5);
    scroll_text = Arduino(scroll_text_arduino)
    print("Scroll text board connected ACM0")

    port = '/dev/ttyACM1'
    led_display_arduino = serial.Serial(port, 9600, timeout=1)
    time.sleep(.5);
    led_display = Arduino(led_display_arduino)
    print("LED board connected, ACM1")

    digit_display = DigitDisplay()
    print("Digit Display Connected")

except Exception as e:
    print(e)

