import newton_cotes
import gauss_legendre
import math

FUNCOES = {
    0: math.sin,
    1: math.cos,
    2: math.sqrt,
    3: math.exp
}

METODOS = {
    0: {
        0: newton_cotes.grau_1_fechada,
        1: newton_cotes.grau_2_fechada,
        2: newton_cotes.grau_3_fechada,
        3: newton_cotes.grau_4_fechada
    },
    1: {
        0: newton_cotes.grau_1_aberta,
        1: newton_cotes.grau_2_aberta,
        2: newton_cotes.grau_3_aberta,
        3: newton_cotes.grau_4_aberta
    },
    2: {
        0: gauss_legendre.gauss_legendre
    }
}


def iterar(metodo, fx, a, b, erro, n_pontos):
    erro_atual = float('inf')
    particoes = 1

    resultado = None
    resultado_atual = None
    iteracoes = 0

    while erro_atual > erro:
        resultado = resultado_atual
        resultado_atual = 0

        h = (b - a) / particoes
        for i in range(particoes):
            resultado_atual += metodo(fx, a + h*i, a + h*(i + 1), n_pontos)
            
        iteracoes += 1

        if resultado != None:
            erro_atual = abs(resultado - resultado_atual)

        particoes *= 2

    return resultado_atual, iteracoes


def particionar(metodo, fx, a, b, n_particoes, n_pontos):
    resultado_atual = 0
    iteracoes = 0

    h = (b - a) / n_particoes
    for i in range(n_particoes):
        resultado_atual += metodo(fx, a + h*i, a + h*(i + 1), n_pontos)
        iteracoes += 1

    return resultado_atual, iteracoes


def receber_entrada_is(limite_inf, limite_sup, mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            if entrada >= limite_inf and entrada <= limite_sup:
                return entrada
        except:
            pass

def receber_entrada_i(limite_inf, mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            if entrada > limite_inf:
                return entrada
        except:
            pass

def receber_valores():
    while True:
        try:
            a = float(input('Escolha o valor do x inicial: '))
            b = float(input('Escolha o valor do x final: '))
            if a < b:
                return a, b;
            else:
                print('O valor de a precisa ser menor que o de b')
        except:
            pass

#--------------inicio do programa--------------

print('Escolha a função que você quer aproximar: ')
print('0: Seno')
print('1: Cosseno')
print('2: Raiz Quadrada')
print('3: Exponenciação')
func = receber_entrada_is(0, 3, 'Escolha uma opção: ')

print("")

a, b = receber_valores()

print("")

print('Escolha o metodo: ')
print('0: newton cotes fechada')
print('1: newton cotes aberta')
print('2: gauss legendre')
metodo = receber_entrada_is(0, 2, 'Escolha uma opção: ')

print("")

if(metodo != 2):
    print('Escolha o grau: ')
    print('0: grau 1')
    print('1: grau 2')
    print('2: grau 3')
    print('3: grau 4')
    grau = receber_entrada_is(0, 3, 'Escolha uma opção: ')
    n_pontos = 0

else:
    grau = 0
    print()
    n_pontos = receber_entrada_i(1, 'Digite o número de pontos: ')

print("")

print('Escolha o ponto de parada: ')
print('0: Partição')
print('1: Erro')
parada = receber_entrada_is(0, 1, 'Escolha uma opção: ')

print("")

if (parada == 1):
    print("Digite o valor do erro:")
    erro = receber_entrada_i(0.0000001)

    resultado_atual, iteracoes = iterar(METODOS[metodo][grau], FUNCOES[func], a, b, erro, n_pontos)
    print("Resultado: ", resultado_atual)
    print("Numero de Iteracoes: ", iteracoes)
else:
    particoes = receber_entrada_i(0, "Digite o número de partições: ")

    resultado_atual, iteracoes = particionar(METODOS[metodo][grau], FUNCOES[func], a, b, particoes, n_pontos)
    print("Resultado: ", resultado_atual)
    print("Numero de Iteracoes: ", iteracoes)