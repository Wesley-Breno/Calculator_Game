from django.shortcuts import render, redirect
from .models import Pontuacoe
from func import operation_math
from django.contrib import messages

resposta_anterior = 0


def home(request):
    if request.method != 'POST':
        dicionario = {}
        dicionario['pessoas'] = []
        dicionario['dados'] = Pontuacoe.objects.all()

        for dado in dicionario['dados']:
            dicionario['pessoas'].append([dado.nome, dado.pontos])

        dicionario['pessoas'].sort(key=lambda i: i[1], reverse=True)
        dicionario['pessoas'] = dicionario['pessoas'][:5]

        operation = operation_math()
        if operation[0] == 1:
            sinal = '+'
        elif operation[0] == 2:
            sinal = '-'
        elif operation[0] == 3:
            sinal = 'x'
        else:
            sinal = '/'

        dicionario['operation'] = [sinal, operation[1], operation[2], operation[3]]
        global resposta_anterior
        resposta_anterior = operation[3]

        dicionario['acertou'] = 0

        return render(request, 'home/index.html', dicionario)

    dicionario = {}
    dicionario['pessoas'] = []
    dicionario['dados'] = Pontuacoe.objects.all()

    for dado in dicionario['dados']:
        dicionario['pessoas'].append([dado.nome, dado.pontos])

    dicionario['pessoas'].sort(key=lambda i: i[1], reverse=True)
    dicionario['pessoas'] = dicionario['pessoas'][:5]

    resposta = request.POST.get('resposta_usuario')

    if int(resposta) == resposta_anterior:
        dicionario['acertou'] = 1
    else:
        dicionario['acertou'] = 2

    operation = operation_math()
    if operation[0] == 1:
        sinal = '+'
    elif operation[0] == 2:
        sinal = '-'
    elif operation[0] == 3:
        sinal = 'x'
    else:
        sinal = '/'

    dicionario['operation'] = [sinal, operation[1], operation[2], operation[3]]
    resposta_anterior = operation[3]

    return render(request, 'home/index.html', dicionario)
