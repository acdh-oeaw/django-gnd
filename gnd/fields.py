from django.db import models


class GndField(models.CharField):

    description = "A Field for a GND Identifier"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 250
        super().__init__(*args, **kwargs)
