""" All forms used in app, build using WTForms. """

from wtforms import Form, HiddenField, SubmitField
from .fields import InputText

class GewerkeForm(Form):
    """ Form for Gewerke. """
    number = InputText('Nummer', min=3, max=3, placeholder='000')
    title = InputText('Bezeichnung', min=1, placeholder='Gewerk')
    action = HiddenField('action', default='add')
    submit = SubmitField('Speichern', render_kw={'class': 'btn btn-primary'})
