from wtforms import (BooleanField, Form, HiddenField, StringField, SubmitField,
                     validators)

class StringField2(StringField):
    """ A modified StringField for convienence and localisation. """

    def __init__(self, *args, form_control=True, placeholder='', **kwargs):
        vals = []
        val_length, kwargs = pick_from_dict(kwargs, 'min', 'max')

        render_kw = popget(kwargs, 'render_kw', {})
        if 'class' not in render_kw:
            render_kw['class'] = ''

        if val_length:
            if 'min' in val_length and 'max' in val_length:
                message = 'Wert muss zwischen {min} und {max} Zeichen lang sein.'.format(**val_length)
            elif 'min' in val_length:
                message = f'Wert muss länger als {val_length["min"]} sein.'
            elif 'max' in val_length:
                message = f'Wert muss kürzer als {val_length["max"]} sein.'
            vals.append(validators.Length(**val_length, message=message))
        if form_control:
            render_kw['class'] += 'form-control'
        if placeholder:
            render_kw['placeholder'] = placeholder
        super().__init__(*args, vals, **kwargs, render_kw=render_kw)


class GewerkeForm(Form):
    number = StringField2('Nummer', min=3, max=3, placeholder='000')
    title = StringField2('Bezeichnung', min=1, placeholder='Gewerk')
    action = HiddenField('action', default='add')
    submit = SubmitField('Speichern', render_kw={'class': 'btn btn-primary'})


def pick_from_dict(input_dict, *args):
    filtered_dict = {}
    for key in args:
        try:
            filtered_dict[key] = input_dict[key]
            del input_dict[key]
        except KeyError:
            pass
    return filtered_dict, input_dict

def popget(input_dict, key, default):
    try:
        value = input_dict.pop(key)
    except KeyError:
        value = default
    return value

