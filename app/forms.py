from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, Field, Form, RadioField, SelectField, \
    FileField, FormField
from wtforms.validators import DataRequired

from app.db_handler import get_names


patterns = ['bpm', 'radialpatternshift', 'juggle']

class SetBeer(FlaskForm):
    '''
    form used for home page to create the drop down menus to select beers
    '''
    BEER_CHOICES = get_names()
    tap1 = SelectField(label='Tap 1', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap2 = SelectField(label='Tap 2', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap3 = SelectField(label='Tap 3', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap4 = SelectField(label='Tap 4', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap5 = SelectField(label='Tap 5', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap6 = SelectField(label='Tap 6', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap7 = SelectField(label='Tap 7', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap8 = SelectField(label='Tap 8', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap9 = SelectField(label='Tap 9', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap10 = SelectField(label='Tap 10', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap11 = SelectField(label='Tap 11', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap12 = SelectField(label='Tap 12', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap13 = SelectField(label='Tap 13', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap14 = SelectField(label='Tap 14', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap15 = SelectField(label='Tap 15', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap16 = SelectField(label='Tap 16', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap17 = SelectField(label='Tap 17', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap18 = SelectField(label='Tap 18', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap19 = SelectField(label='Tap 19', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap20 = SelectField(label='Tap 20', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap21 = SelectField(label='Tap 21', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap22 = SelectField(label='Tap 22', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap23 = SelectField(label='Tap 23', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap24 = SelectField(label='Tap 24', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap25 = SelectField(label='Tap 25', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap26 = SelectField(label='Tap 26', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap27 = SelectField(label='Tap 27', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap28 = SelectField(label='Tap 28', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap29 = SelectField(label='Tap 29', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap30 = SelectField(label='Tap 30', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap31 = SelectField(label='Tap 31', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap32 = SelectField(label='Tap 32', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap33 = SelectField(label='Tap 33', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap34 = SelectField(label='Tap 34', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap35 = SelectField(label='Tap 35', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap36 = SelectField(label='Tap 36', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap37 = SelectField(label='Tap 37', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap38 = SelectField(label='Tap 38', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap39 = SelectField(label='Tap 39', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    tap40 = SelectField(label='Tap 40', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])



class SelectEdit(FlaskForm):
    '''
    used to edit previously saved beers
    '''
    BEER_CHOICES = get_names()
    beer = SelectField(label='Beer', choices=[(str(beer), str(beer)) for beer in BEER_CHOICES])
    submit = SubmitField('Submit')


class BeerForm(FlaskForm):
    '''
    form used to create new beer or to edit previously saved beer
    '''

    beername = StringField('Beer Name', validators=[DataRequired()])
    pattern = SelectField(label='Pattern', choices=[(pattern[0], str(pattern[1])) for pattern in enumerate(patterns)])
    val1 = RadioField('Value 1', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                      validators=[DataRequired()])
    val2 = RadioField('Value 2', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                      validators=[DataRequired()])
    val3 = RadioField('Value 3', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                      validators=[DataRequired()])
    val4 = RadioField('Value 4', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                      validators=[DataRequired()])
    val5 = RadioField('Value 5', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                      validators=[DataRequired()])
    rarity = RadioField('Rarity', choices=[('1', '1'), ('2', '2'), ('3', '3')],
                      validators=[DataRequired()])
    abv = StringField('ABV', validators=[DataRequired()])
    submit = SubmitField('Submit')
