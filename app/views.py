import sys
import threading
from flask import request, render_template, redirect, flash, Flask, session, url_for
from app.models import *
from app.forms import *
from app.arduino import get_ip
from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
bootstrap = Bootstrap(app)


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
    form.process()
    form.abv.data = beer.abv
    form.beername.data = beer.name
    if request.method == "POST":
        print(beer)
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
    button = request.form['action']
    if 'Demo' in button:
        # change the name of the clicked button from Demo + tap number to just the tap number
        # beer must be saved before demo
        tap_number = button.replace("Demo", "")
        selected_beer = request.form[tap_number]
        beer_vals = get_beer_by_name(selected_beer)
        print(beer_vals.name)
        # spawn and start the threads to drive the arduino displays
        # threading.Thread(target=scroll_text.demo, args=(selected_beer, )).start().join()
        # threading.Thread(target=led_display.demo, args=(selected_beer, )).start().join()

    elif 'Submit' in button:
        # save the beer to the proper tap number
        tap_number = button.replace("Submit", "")
        selected_beer = request.form[tap_number]
        tap_number = int(tap_number.replace("tap", ""))  # get the actual number to give to the database
        # print(set_tap(tap_number, selected_beer))
    # returns nothing, leaving page as it was when function was called
    return ('', 204)  # redirect('/')


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    main page that has 40 select fields to display the beer set
    for each tap as well as to set and demo beers for
    each tap
    '''
    return render_template('main.html', names=get_names())



if __name__ == '__main__':

    print("Current IP is", get_ip())
    print("Point your browser to http://", get_ip(), sep="")
    print()

    app.run(debug=True, host='0.0.0.0')

''' 
try:
    ''''''
    connect to and set the serial connection between the raspberry pi and teensy boards

    scroll_text = teensy 3.2
    led_display = teensy 3.6
    ''''''

    print('Connecting to Arduinos')
    port = '/dev/ttyUSB-SCROLLTEXT'
    scroll_text_arduino = serial.Serial(port, 9600, timeout=1)
    time.sleep(.5);
    scroll_text = Arduino(scroll_text_arduino)
    print("Scroll text board connected")

    port = '/dev/ttyUSB-MAINDISPLAY'
    led_display_arduino = serial.Serial(port, 9600, timeout=1)
    time.sleep(.5);
    led_display = Arduino(led_display_arduino)
    print("LED board connected")

    digit_display = DigitDisplay()
    print("Digit Display Connected")

except Exception as e:
    print(e)
'''
