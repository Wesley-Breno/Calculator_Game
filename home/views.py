from django.shortcuts import render, redirect
from .models import Pontuacoe
from func import operation_math

COOKIE_NAME = 'pontuacao'
resposta_anterior_sem_cookie = 0
cont = 0


def home(request):
    if request.method != 'POST':
        dicionario = {}

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

        global resposta_anterior_sem_cookie
        resposta_anterior_sem_cookie = operation[3]

        dicionario['acertou'] = 0

        # Verifica se o cookie com a pontuação não existe
        if COOKIE_NAME not in request.COOKIES:
            dicionario['primeira_vez_no_site'] = True
            return render(request, 'home/index.html', dicionario)

        # Se o cookie já existir, renderiza a página normalmente
        dicionario['primeira_vez_no_site'] = False
        dicionario['pontuacao'] = int(request.COOKIES.get(COOKIE_NAME, 0))
        response = render(request, 'home/index.html', dicionario)
        response.set_cookie('resposta_anterior', operation[3], max_age=86400, secure=True, httponly=True)
        return response

    dicionario = {}

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

    resposta = request.POST.get('resposta_usuario')
    concorda_com_cookies = request.POST.get('concorda_com_cookies')

    if concorda_com_cookies == 'True' or COOKIE_NAME in request.COOKIES:
        if COOKIE_NAME not in request.COOKIES:
            response = render(request, 'home/index.html', dicionario)
            response.set_cookie(COOKIE_NAME, 0, max_age=86400, secure=True, httponly=True)
            response.set_cookie('resposta_anterior', operation[3], max_age=86400, secure=True, httponly=True)
            return response

        else:
            try:
                if int(resposta) == int(str(request.COOKIES.get('resposta_anterior')).split('.')[0]):
                    dicionario['acertou'] = 1
                    pontuacao_atual = int(request.COOKIES.get(COOKIE_NAME, 0))
                    nova_pontuacao = pontuacao_atual + 1
                    dicionario['pontuacao'] = nova_pontuacao

                    # Define o novo valor do cookie com a nova pontuação
                    response = render(request, 'home/index.html', dicionario)
                    response.set_cookie(COOKIE_NAME, nova_pontuacao, max_age=86400, secure=True, httponly=True)
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
            response.set_cookie('pontuacao', nova_pontuacao, max_age=86400, secure=True, httponly=True)
            response.set_cookie('resposta_anterior', operation[3], max_age=86400, secure=True, httponly=True)
            return response

    else:
        resposta = request.POST.get('resposta_usuario')

        if resposta is None:
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
            resposta_anterior_sem_cookie = operation[3]

            return render(request, 'home/index.html', dicionario)

        if int(resposta) == resposta_anterior_sem_cookie:
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
        resposta_anterior_sem_cookie = operation[3]

        return render(request, 'home/index.html', dicionario)
