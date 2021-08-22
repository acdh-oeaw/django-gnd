from django.test import TestCase
from .data import MOEST

from gnd.utils import fetch_gender


GND_IDS = [
    'https://d-nb.info/gnd/134397614',
    'https://d-nb.info/gnd/124584233'
]


# Create your tests here.
class GndTestCase(TestCase):

    def setUp(self):
        # Test definitions as before.
        pass

    def test_001_smoke(self):
        self.assertEqual(1, 1)

    def test_002_gender(self):
        gender = fetch_gender(MOEST)
        self.assertEqual(gender, 'https://d-nb.info/standards/vocab/gnd/gender#male')
