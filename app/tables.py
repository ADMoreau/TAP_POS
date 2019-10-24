from flask_table import Table, Col, LinkCol

class Beers(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    abv = Col('ABV')
    abv_color = Col('ABV Color')
    rarity = Col('Rarity')
    rarity_color = Col('Rarity Color')
    in_use = Col('In Use')
    edit = LinkCol('Edit', 'edit_entry', url_kwargs=dict(id='id'))
