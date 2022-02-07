from django.test import TestCase
from gnd.tests.tests import GND_IDS

from ..models import Person


# Create your tests here.
class GndTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        for x in GND_IDS:
            Person.objects.create(gnd_gnd_id=x)

    def test_001_smoke(self):
        self.assertEqual(1, 1)

    def test_002_detail_views(self):
        for x in GND_IDS:
            item = Person.objects.get(gnd_gnd_id=x)
            url = item.get_absolute_url()
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            content = f"{response.content}"
            self.assertTrue(x in content)
