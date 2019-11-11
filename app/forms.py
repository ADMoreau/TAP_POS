from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired

patterns = ['AliceBlue', 'Amethyst', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque',
                'BlanchedAlmond', 'Blue', 'BlueViolet', 'Brown', 'BurlyWood', 'CadetBlue', 'Chartreuse', 'Chocolate',
                'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenrod', 'DarkGray',
                'DarkGreen', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon',
                'DarkSeaGreen', 'DarkSlateBlue', 'DarkSlateGray', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue',
                'DimGray', 'DodgerBlue', 'FireBrick', 'FloralWhite', 'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold',
                'Goldenrod', 'Gray', 'Green', 'GreenYellow', 'Honeydew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory', 'Khaki', 'Lavender',
                'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan', 'LightGoldenrodYellow',
                'LightGreen', 'LightGrey', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray', 'LightSteelBlue',
                'LightYellow', 'Lime', 'LimeGreen', 'Linen', 'Magenta', 'Maroon', 'MediumAquamarine', 'MediumBlue', 'MediumOrchid',
                'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed',
                'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy', 'OldLace', 'Olive', 'OliveDrab', 'Orange',
                'OrangeRed', 'Orchid', 'PaleGoldenrod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed', 'PapayaWhip', 'PeachPuff',
                'Peru, Pink', 'Plaid', 'Plum', 'PowderBlue', 'Purple', 'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Salmon',
                'SandyBrown', 'SeaGreen', 'Seashell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'Snow', 'SpringGreen',
                'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'WhiteSmoke', 'Yellow', 'YellowGreen']


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
