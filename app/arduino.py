import socket
import time

import serial
#import serial.tools.list_ports

from app.db_handler import get_beer_by_name

arduino = None


def demo_function(selected_beer):
    beer_info = get_beer_by_name(selected_beer)[0]
    #print(beer_info)
    arduino_send_cmd("1A=101")
    time.sleep(4)
    arduino_send_cmd("1A=102")

def set_arduino(new_arduino):
    global arduino
    arduino = new_arduino


def arduino_get_resp(s):
    time.sleep(.1);
    while (s.in_waiting > 0):
        print(s.readline().decode(), end="");

def arduino_send_cmd(s):
    arduino.flush();
    s = s+'\n'
    arduino.write(s.encode());
    arduino_get_resp(arduino);
    time.sleep(.1);
    arduino.flush()

# try to detect the USB port where Arduino is connected
def arduino_get_port():
    print("Listing ports")
    port = None
    ports = serial.tools.list_ports.comports()
    for p in ports:
        print(p)
        if "Arduino" in p[1]:
            port = p[0]
            print("Arduino detected on port", port)

    return port


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip