from django.http import JsonResponse
from django.shortcuts import render
from . import tradutor


# Create your views here.
def home(request, template_name='home.html'):
    return render(request, template_name)


def tradutor_inteiro(request, inteiro):
    try:
        valor = int(inteiro)
        resposta = tradutor.transformar_numero_extenso(inteiro)
        print(resposta)
    except (ValueError, TypeError):
        resposta = "Valor invalido"

    return JsonResponse({'extenso': resposta})