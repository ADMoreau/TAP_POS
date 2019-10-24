import sys
import threading
from flask import request, render_template, redirect, flash, Flask, session
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

from app import patterns
from app.db_handler import *
from app.forms import *
from app.config import Config
from app.tables import Beers
from app.arduino import *

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
bootstrap = Bootstrap(app)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/edit', methods=['GET', 'POST'])
def edit_entry():
    name = session['name']
    beer = get_beer_by_name(name)[0]
    print(beer)
    form = BeerForm()
    form.val1.default = beer["val1"]
    form.val2.default = beer["val2"]
    form.val3.default = beer["val3"]
    form.val4.default = beer["val4"]
    form.val5.default = beer["val5"]
    form.rarity.default = beer['rarity']
    form.process()
    form.abv.data = beer['abv']
    form.beername.data = beer['name']
    if form.validate_on_submit():
        return redirect('/')
    return render_template('create-new.html', form=form)


@app.route('/select-edit', methods=['GET', 'POST'])
def select_edit():
    form = SelectEdit()
    if form.validate_on_submit():
        session['name'] = request.form.get('beer')
        return redirect('/edit')
    return render_template('edit.html', form=form)


@app.route('/create-new', methods=['GET', 'POST'])
def create_new():
    form = BeerForm(request.form)
    if form.validate_on_submit():
        flash(insert(form))
        return redirect('/')
    else:
        file_url = None
    return render_template('create-new.html', form=form)


@app.route('/set', methods=['GET', 'POST'])
def set_beers():
    form = SetBeer()
    if form.validate_on_submit():
        flash("Beer set")
        return redirect('/')
    return render_template('set.html', form=form)


@app.route('/process', methods=['POST'])
def process():
    button = request.form['action']
    if 'Demo' in button:
        tap_number = button.replace("Demo", "")
        selected_beer = request.form[tap_number]
        #demo_function(selected_beer)
        threading.Thread(target=demo_function, args=(selected_beer, )).start()
        #demo_thread.join()

    elif 'Submit' in button:
        tap_number = button.replace("Submit", "")
        selected_beer = request.form[tap_number]
        tap_number = int(tap_number.replace("tap", "")) #get the actual number to give to the database
        print(set_tap(tap_number, selected_beer))
    #returns nothing, leaving page as it was when function was called
    return ('', 204)  # redirect('/')


@app.route('/submit', methods=["POST"])
def submit():
    name = request.args.get('name')
    return


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SetBeer()
    return render_template('main.html', form=form)


if __name__ == '__main__':

    #incase the arduino is not connected
    try:
        port = '/dev/ttyACM0'
        print("Arduino port: " + port)

        # open the serial interface
        arduino = serial.Serial(port, 9600, timeout=1)
        time.sleep(.5);
        set_arduino(arduino)
        print("Port", arduino)
        print("Current IP is", get_ip())
        print("Point your browser to http://", get_ip(), sep="")
        print()

        app.run('0.0.0.0')
    except:
        print("Arduino not connected")
        app.run('0.0.0.0')


