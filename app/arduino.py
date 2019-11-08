import socket
import time
import serial
# import serial.tools.list_ports
from digit_display import *
from models import get_beer_by_name


class Arduino():
    """
    object to use to control the two arduino teensy boards
    each board is assigned to a separate arduino object
    """

    def __init__(self, board):
        self.board = board

    def display(self, selected_beer, scrolltext=False):
        beer = get_beer_by_name(selected_beer)
        # print(beer_info)
        if scrolltext:
            '''
            use the scroll text thread to display the name and set the three digit display
            '''
            self.send_cmd(beer.name)
            time.sleep(6)
            self.send_cmd(" ")
        else:
            '''
            use this thread to send the other information to the other teensy
            '''
            to_send = str(beer.val1) + str(beer.val2) + str(beer.val3) + str(beer.val4) + str(beer.val5) \
                      + str(beer.rarity) \
                      + "0001"
                      #+ str(beer.pattern) \
            self.send_cmd(to_send)
            time.sleep(6)
            self.send_cmd("end")

    def get_resp(self):
        time.sleep(.1)
        while (self.board.in_waiting > 0):
            print(self.board.readline().decode('ISO-8859-1', errors='replace'), end="")

    def send_cmd(self, s):
        self.board.flush()
        s = s + '\n'
        print(s)
        self.board.write(s.encode())
        self.get_resp()
        #time.sleep()
        #self.board.flush()

    def flush(self, scrolltext = False):
        if scrolltext == True:
            self.send_cmd(" ")
            self.board.flushInput()
        else:
            self.send_cmd("end\n")
            self.board.flushInput()


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
