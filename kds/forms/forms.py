""" All forms used in app, build using WTForms. """

from flask_admin.form.fields import Select2Field
from wtforms import Form, HiddenField, SubmitField
from .fields import InputText


class GewerkeForm(Form):
    """ Form for Gewerke. """
    id = HiddenField('Id', default=0)
    index = InputText('Nummer', min=3, max=3, placeholder='000')
    titel = InputText('Bezeichnung', min=1, placeholder='Gewerk')
    submit = SubmitField('Speichern', render_kw={'class': 'btn btn-primary'})
    readable = 'titel'

class UnternehmenForm(Form):
    """ Form for Unternehmen. """
    id = HiddenField('Id', default=0)
    name = InputText('Name', min=3)
    adr_strasse = InputText('Straße, Nummer', min=3)
    adr_plz = InputText('Postleitzahl', min=5, max=5)
    adr_stadt = InputText('Stadt', min=2)
    con_fon = InputText('Telefon')
    con_fax = InputText('Fax')
    gewerke = Select2Field('Gewerke', coerce=int, render_kw={'data-role': 'select2', 'multiple': True, 'class': 'form-control'})
    submit = SubmitField('Speichern', render_kw={'class': 'btn btn-primary'})
    readable = 'name'