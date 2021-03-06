from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired

patterns = ['AliceBlue', 'Aqua', 'Blue', 'BlueViolet', 'Chartreuse', 'Crimson', 'Cyan', 'DeepPink', 'DeepSkyBlue',
                'DodgerBlue','FloralWhite', 'ForestGreen', 'Fuchsia','GhostWhite', 'Gold','Green','GreenYellow','Indigo', 'Ivory',
                'LawnGreen', 'Lime', 'LimeGreen', 'Magenta', 'Orange','OrangeRed', 'Orchid','Purple', 'Red', 'SeaGreen']


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
    abv1 = SelectField(label='ABV1', choices=[(i, i) for i in range(10)])
    abv2 = SelectField(label='ABV2', choices=[(i, i) for i in range(10)])
    abv3 = SelectField(label='ABV3', choices=[(i, i) for i in range(10)])
    submit = SubmitField('Submit')
