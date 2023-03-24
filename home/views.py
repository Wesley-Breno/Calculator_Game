from django.shortcuts import render, redirect
from .models import Pontuacoe
from func import operation_math

COOKIE_NAME = 'pontuacao'


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

        dicionario['acertou'] = 0

        # Verifica se o cookie com a pontuação já existe, se não, define a pontuação inicial como 0
        if COOKIE_NAME not in request.COOKIES:
            response = render(request, 'home/index.html', dicionario)
            response.set_cookie(COOKIE_NAME, 0, max_age=86400)
            response.set_cookie('resposta_anterior', operation[3], max_age=86400)
            return response

        # Se o cookie já existir, renderiza a página normalmente
        dicionario['pontuacao'] = int(request.COOKIES.get(COOKIE_NAME, 0))
        response = render(request, 'home/index.html', dicionario)
        response.set_cookie('resposta_anterior', operation[3], max_age=86400)
        return response

    dicionario = {}
    dicionario['pessoas'] = []
    dicionario['dados'] = Pontuacoe.objects.all()

    for dado in dicionario['dados']:
        dicionario['pessoas'].append([dado.nome, dado.pontos])

    dicionario['pessoas'].sort(key=lambda i: i[1], reverse=True)
    dicionario['pessoas'] = dicionario['pessoas'][:5]

    resposta = request.POST.get('resposta_usuario')

    try:
        if int(resposta) == int(str(request.COOKIES.get('resposta_anterior')).split('.')[0]):
            dicionario['acertou'] = 1
            pontuacao_atual = int(request.COOKIES.get(COOKIE_NAME, 0))
            nova_pontuacao = pontuacao_atual + 1
            dicionario['pontuacao'] = nova_pontuacao

            # Define o novo valor do cookie com a nova pontuação
            response = render(request, 'home/index.html', dicionario)
            response.set_cookie(COOKIE_NAME, nova_pontuacao, max_age=86400)
        else:
            pontuacao_atual = int(request.COOKIES.get(COOKIE_NAME, 0))
            nova_pontuacao = 0
            dicionario['acertou'] = 2
            dicionario['pontuacao'] = nova_pontuacao
    except:
        pontuacao_atual = int(request.COOKIES.get(COOKIE_NAME, 0))
        nova_pontuacao = 0
        dicionario['acertou'] = 2
        dicionario['pontuacao'] = nova_pontuacao

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

    response = render(request, 'home/index.html', dicionario)
    response.set_cookie('pontuacao', nova_pontuacao, max_age=86400)
    response.set_cookie('resposta_anterior', operation[3], max_age=86400)
    return response
