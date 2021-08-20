from django import forms

from . models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = [
            "gnd_pref_name",
            "gnd_payload"
        ]
