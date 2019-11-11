import sys
import threading
from flask import render_template, redirect, flash, session

#from app.digit_display import DigitDisplay
from models import *
from forms import *
from arduino import *
from config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
import serial
import time


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
bootstrap = Bootstrap(app)

scroll_text = None
led_display = None
digit_display = None
lock = threading.Lock()


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    '''
    once beer has been selected to edit at the /select-edit page prefill the BeerForm data with the data for the beer
    that was selected to edit by said beer's name.

    beer name stored as session variable that is saved in the select-edit function
    :return:
    '''
    name = session['name']
    beer = get_beer_by_name(name)
    form = BeerForm()
    form.val1.default = beer.val1
    form.val2.default = beer.val2
    form.val3.default = beer.val3
    form.val4.default = beer.val4
    form.val5.default = beer.val5
    form.rarity.default = beer.rarity
    form.abv1.default = int(beer.abv[0])
    form.abv2.default = int(beer.abv[1])
    form.abv3.default = int(beer.abv[2])
    form.pattern.default = beer.pattern
    form.process()
    form.beername.data = beer.name
    if request.method == "POST":
        delete_beer(beer)
        insert(form)
        return redirect('/')
    return render_template('edit.html', form=form)


@app.route('/select-edit', methods=['GET', 'POST'])
def select_edit():
    '''
    go to the page where you select the beer that you want to edit

    select fields are not preselected with the saved values
    '''
    if request.method == "POST":
        session['name'] = request.form['beer_select']
        return redirect('/edit')
    return render_template('select-edit.html', names=get_names())


@app.route('/select-delete', methods=['GET', 'POST'])
def select_delete():
    '''
    go to the page where you select the beer that you want to edit

    select fields are not preselected with the saved values
    '''
    if request.method == "POST":
        beername = request.form['beer_select']
        beer = get_beer_by_name(beername)
        delete_beer(beer)
        return redirect('/')
    return render_template('select-edit.html', names=get_names())


@app.route('/create-new', methods=['GET', 'POST'])
def create_new():
    '''
    go to the page where you create a new beer to save in the database
    '''
    form = BeerForm()
    # if form.validate_on_submit():
    if request.method == "POST":
        print("Validated")
        flash(insert(form))
        return redirect('/')
    return render_template('create-new.html', form=form)


@app.route('/process', methods=['POST'])
def process():
    '''
    process the buttons used to set and demonstrate the beer information in the database

    :return: nothing, do not switch or update the web page in any way
    '''
    def demo(selected_beer):
        if lock.locked() == False:
            try:
                lock.acquire()
                scroll_text.display(selected_beer, True)
                led_display.display(selected_beer)
                time.sleep(10)
                scroll_text.flush(True)
                led_display.flush()
            finally:
                lock.release()
        else:
            return
        
    button = request.form['action']
    if 'Demo' in button:
        # change the name of the clicked button from Demo + tap number to just the tap number
        # beer must be saved before demo
        tap_number = button.replace("Demo", "")
        selected_beer = request.form[tap_number]
        beer = get_beer_by_name(selected_beer)
        #print(beer_vals.name)
        # spawn and start the threads to drive the arduino displays
        demo(beer)
        '''
        scrollstart = threading.Thread(target=scroll_text.display, args=(selected_beer, True)).start()
        displaystart = threading.Thread(target=led_display.display, args=(selected_beer, )).start()
        scrollstart.join()
        displaystart.join()
        time.sleep(6)
        scrollend = threading.Thread(target=scroll_text.flush, args=(selected_beer, True)).start()
        displayend = threading.Thread(target=led_display.flush, args=(selected_beer, )).start()
        scrollend.join()
        displayend.join()
        '''

    elif 'Submit' in button:
        # save the beer to the proper tap number
        tap_number = button.replace("Submit", "")
        selected_beer = request.form[tap_number]
        tap_number = int(tap_number.replace("tap", "")) - 1  # get the actual number to give to the database
        update_tap(selected_beer, tap_number)
        print(str(tap_number) + " update")
        # print(set_tap(tap_number, selected_beer))
    # returns nothing, leaving page as it was when function was called
    
    return ('', 204)


@app.route('/view')
def view():
    beer_df = get_records()
    beer_df.set_index(['name'], inplace=True)
    beer_df.index.name = None
    #print(beer_df)
    return beer_df.to_html(header=True)


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    main page that has 40 select fields to display the beer set
    for each tap as well as to set and demo beers for
    each tap
    '''
    return render_template('main.html', names=get_names())


def watch_for_tap(taps, scroll, levels): #, digits):
    '''
    thread to monitor and run the displays
    '''
    print("taps initialized")
    #digits.digit_cleanup()
    while True:
        if (taps.in_waiting > 0 and lock.locked() == False):
            try:
                lock.acquire()
                tap = int(taps.readline().decode('ISO-8859-1', errors='replace')[:-2])
                print(tap)
                beer = get_beer_by_tap(tap)
                if beer is not None:
                    print(beer.name)
                    levels.display(beer, scrolltext=False)
                    scroll.display(beer, scrolltext=True)
                    time.sleep(10)
                    levels.flush(scrolltext=False)
                    #digits.digit_cleanup()
                else:
                    print("No Beer")
                    scroll.send_cmd("NO BEER ON TAP {}".format(tap + 1))
                    time.sleep(10)
                scroll.flush(scrolltext=True)
            finally:
                taps.flush()
                taps.in_waiting == 0
                lock.release()
        
        elif (taps.in_waiting > 0 and lock.locked() == True):
                taps.flush()
                taps.in_waiting == 0


if __name__ == '__main__':

    try:
        '''
        connect to and set the serial connection between the raspberry pi and teensy boards

        scroll_text = teensy 3.2
        led_display = teensy 3.6
        '''

        print('Connecting to Arduinos')
        port = '/dev/ttyUSB-SCROLLTEXT'
        scroll_text_arduino = serial.Serial(port, 9600, timeout=3)
        time.sleep(.5);
        scroll_text = Arduino(scroll_text_arduino)
        print("Scroll text board connected")

        port = '/dev/ttyUSB-MAINDISPLAY'
        led_display_arduino = serial.Serial(port, 9600, timeout=3)
        time.sleep(.5);
        led_display = Arduino(led_display_arduino)
        print("LED board connected")

        taps = '/dev/ttyS0'
        taps = serial.Serial(taps, 9600, timeout=3)
        time.sleep(.5)
        print("Taps I2C receiver connected")

        #digit_display = DigitDisplay()
        #print("Digit Display Connected")
        
        watch_thread = threading.Thread(target=watch_for_tap, args=(taps,
                                                                    scroll_text,
                                                                    led_display))
                                                                    #digit_display))
        watch_thread.start()
        

    except Exception as e:
        print(e)

    print("Current IP is", get_ip())
    print("Point your browser to http://", get_ip(), sep="")
    print()

    app.run(debug=True, host='0.0.0.0')
