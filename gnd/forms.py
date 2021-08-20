from django import forms
from gnd.widgets import GndAcWidget


class GndFormField(forms.CharField):
    widget = GndAcWidget(
        options={
            'placeholder': 'Search the GND',
            'multiple': False,
            'maximum-selection-length': 21,
            'minimumInputLength': 3
        }
    )


class GndForm(forms.Form):
    gnd = GndFormField(
        label='GND',
        widget=GndAcWidget(
            options={'placeholder': 'Search the GND'}
        ),
    )
