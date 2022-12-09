import json
from django.forms import model_to_dict
from django.test import TestCase
import factory
import requests

from apps.covid.models import Covid


# Create your tests here.
class CovidFactory(factory.Factory):
    class Meta:
        model = Covid


class CovidTestCase(TestCase):
    def setUp(self):
        self.estado = "pb"

    def test_consultar_estado_errado(self):
        req = requests.get(f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{self.estado}")

        data = json.loads(req.text)

        covid = CovidFactory()
        covid.uid = data["uid"]
        covid.uf = data["uf"]
        covid.state = data["state"]
        covid.cases = data["cases"]
        covid.deaths = data["deaths"]
        covid.suspects = data["suspects"]
        covid.refuses = data["refuses"]
        covid.datetime = data["datetime"]
        covid.save()
        
        #model = model_to_dict(covid, exclude=["id"])

        #self.assertEquals(data, model)
        # self.assertNotEquals(model["logradouro"], "")
        
        self.assertEquals(data["uf"], "PB")
        self.assertGreaterEqual(covid.suspects, 80)
        self.assertIn("2022", covid.datetime)