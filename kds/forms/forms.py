""" All forms used in app, build using WTForms. """

from flask_admin.form.fields import Select2Field
from wtforms import Form, HiddenField, SubmitField
from .fields import InputText


class GewerkeForm(Form):
    """ Form for Gewerke. """
    index = InputText('Nummer', min=3, max=3, placeholder='000')
    titel = InputText('Bezeichnung', min=1, placeholder='Gewerk')

    action = HiddenField('action', default='add')
    submit = SubmitField('Speichern', render_kw={'class': 'btn btn-primary'})

class UnternehmenForm(Form):
    """ Form for Unternehmen. """
    name = InputText('Name', min=3)
    adr_strasse = InputText('Straße, Nummer', min=3)
    adr_plz = InputText('Postleitzahl', min=5, max=5)
    adr_stadt = InputText('Stadt', min=2)
    con_fon = InputText('Telefon')
    con_fax = InputText('Fax')
    gewerke = Select2Field('Gewerke', coerce=int, render_kw={'data-role': 'select2', 'multiple': True, 'class': 'form-control'})
    submit = SubmitField('Speichern', render_kw={'class': 'btn btn-primary'})
