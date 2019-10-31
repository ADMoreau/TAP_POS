import socket
import time
import serial
#import serial.tools.list_ports
from app import digit_display
from app.db_handler import get_beer_by_name


class Arduino():
    '''
    object to use to control the two arduino teensy boards
    each board is assigned to a separate arduino object
    '''

    def __init__(self, board):
        self.board = board

    def display(self, selected_beer, scrolltext = False):
        beer_info = get_beer_by_name(selected_beer)[0]
        #print(beer_info)
        if scrolltext:
            '''
            use the scroll text thread to display the name and set the three digit display
            '''
            self.send_cmd(beer_info['name'])
            digit_display.show_number(beer_info['abv'])
        else:
            '''
            use this thread to send the other information to the other teensy
            '''
            to_send = beer_info['val1'] + beer_info['val2'] + beer_info['val3'] + beer_info['val4'] + beer_info['val5']\
                      + beer_info['pattern'] \
                      + beer_info['rarity']
            self.send_cmd(to_send)

        '''
        self.arduino_send_cmd("1A=101")
        time.sleep(4)
        self.arduino_send_cmd("1A=102")
        '''

    def get_resp(self, s):
        time.sleep(.1)
        while (self.board.in_waiting > 0):
            print(s.readline().decode(), end="")

    def send_cmd(self, s):
        self.board.flush()
        s = s+'\n'
        self.board.write(s.encode())
        self.arduino_get_resp()
        time.sleep(.1)
        self.board.flush()

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
