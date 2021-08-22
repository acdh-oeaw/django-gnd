from django.test import TestCase, Client
from gnd.tests.tests import GND_IDS

from ..models import Person

client = Client()


# Create your tests here.
class GndTestCase(TestCase):

    def setUp(self):
        # Test definitions as before.
        pass

    def test_001_smoke(self):
        self.assertEqual(1, 1)

    def test_002_create_persons(self):
        for x in GND_IDS:
            Person.objects.create(gnd_gnd_id=x)
        qs = Person.objects.all()
        self.assertEqual(qs.count(), len(GND_IDS))

    def test_003_detail_views(self):
        for x in GND_IDS:
            Person.objects.create(gnd_gnd_id=x)
            item = Person.objects.get(gnd_gnd_id=x)
            url = item.get_absolute_url()
            response = client.get(url)
            self.assertEqual(response.status_code, 200)
            content = f"{response.content}"
            self.assertTrue(x in content)
