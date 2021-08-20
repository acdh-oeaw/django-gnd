from django import forms
from gnd.widgets import GndAcWidget


class GndForm(forms.Form):
    gnd = forms.ChoiceField(
        label='GND',
        widget=GndAcWidget(
            options={
                'placeholder': 'Search the GND',
                'multiple': False,
                'maximum-selection-length': 1,
                'minimumInputLength': 3
            }
        ),
    )
