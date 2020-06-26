""" All forms used in app, build using WTForms. """

from flask_admin.form.fields import Select2Field
from wtforms import HiddenField, SelectMultipleField, SubmitField
from .fields import InputText
from wtforms import Form as FormOrig

from wtforms.meta import DefaultMeta

class BindNameMeta(DefaultMeta):
    def bind_field(self, form, unbound_field, options):
        if 'custom_name' in unbound_field.kwargs:
            options['name'] = unbound_field.kwargs.pop('custom_name')
        return unbound_field.bind(form=form, **options)

class Form(FormOrig):
    meta = BindNameMeta

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
    gewerke = Select2Field('Gewerke', custom_name='gewerke[]', render_kw={'data-role': 'select2', 'multiple': True, 'class': 'form-control'})
    submit = SubmitField('Speichern', render_kw={'class': 'btn btn-primary'})
