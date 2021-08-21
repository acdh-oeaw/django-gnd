from datetime import datetime
from django.db import models
from pylobid.pylobid import PyLobidPerson
from . fields import GndField


class GndBaseModel(models.Model):
    gnd_gnd_id = GndField(
        blank=True, null=True, unique=True
    )
    gnd_pref_name = models.CharField(
        blank=True, null=True, max_length=250
    )
    gnd_payload = models.JSONField(blank=True, null=True)
    gnd_created = models.DateTimeField(
        blank=True, null=True, auto_now=False, auto_now_add=False
    )

    def __str__(self):
        return f"{self.gnd_gnd_id}"

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.gnd_gnd_id and not self.gnd_created:
            # ToDo: Use PyLobidClient() instead of PyLobidPerson()
            py_ent = PyLobidPerson(gnd_id=self.gnd_gnd_id)
            self.gnd_pref_name = py_ent.pref_name
            self.gnd_payload = py_ent.ent_dict
            self.gnd_created = datetime.now()
        super().save(*args, **kwargs)
