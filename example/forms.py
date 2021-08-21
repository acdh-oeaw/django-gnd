from gnd.forms import GndModelForm
from . models import Person


class PersonForm(GndModelForm):

    class Meta:
        model = Person
        fields = [
            'gnd_gnd_id',
            'gnd_pref_name'
        ]