from django import forms
from gnd.widgets import GndAcWidget


class GndForm(forms.Form):
    gnd = forms.ChoiceField(
        label='GND',
        widget=GndAcWidget(
            options={
                'placeholder': 'Start Typing',
                'multiple': False,
                'maximum-selection-length': 1
            }
        ),
    )
