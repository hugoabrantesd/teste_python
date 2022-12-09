import json
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
import requests
from django.shortcuts import render

from apps.covid.models import Covid

# Create your views here.


def consultar_covid_uf(request, uf):
    req = requests.get(f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{uf}")
    data = json.loads(req.text)
    covid = Covid.objects.create(**data)
    model = model_to_dict(covid)
    return JsonResponse(model)


# def buscar_cep(request, cep):
#     endereco = Endereco.objects.get(cep=cep)

#     model = model_to_dict(endereco)

#     print(model)

#     return JsonResponse(model)
