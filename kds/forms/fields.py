""" Custom fields for WTForm fields, usually by subclassing."""

from wtforms import StringField, validators

from .utils import pick_from_dict, popget


class InputText(StringField):
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
