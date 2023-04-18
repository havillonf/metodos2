import funcoes
import math

FUNCOES = {
    0: math.sin,
    1: math.cos,
    2: math.sqrt,
    3: math.cbrt,
    4: math.exp
}

METODOS = {
    0: {
        0: funcoes.grau_1_fechada,
        1: funcoes.grau_2_fechada,
        2: funcoes.grau_3_fechada,
        3: funcoes.grau_4_fechada
    },
    1: {
        0: funcoes.grau_1_aberta,
        1: funcoes.grau_2_aberta,
        2: funcoes.grau_3_aberta,
        3: funcoes.grau_4_aberta
    }
}


def iterar(metodo, fx, a, b, erro):
    erro_atual = float('inf')
    particoes = 1

    resultado = None
    resultado_atual = None

    while erro_atual > erro:
        resultado = resultado_atual
        resultado_atual, iteracoes = 0, 0

        h = (b - a) / particoes
        for i in range(particoes):
            resultado_atual += metodo(fx, a + h*i, a + h*(i + 1))
            iteracoes += 1

        if resultado != None:
            erro_atual = abs(resultado - resultado_atual)

        particoes *= 2

    return resultado_atual, iteracoes


def particionar(metodo, fx, a, b, n_particoes):
    resultado_atual = 0
    iteracoes = 0

    h = (b - a) / n_particoes
    for i in range(n_particoes):
        resultado_atual += metodo(fx, a + h*i, a + h*(i + 1))
        iteracoes += 1

    return resultado_atual, iteracoes


def receber_entrada_is(limite_inf, limite_sup):
    while True:
        try:
            entrada = int(input('Escolha uma opção: '))
            if entrada >= limite_inf and entrada <= limite_sup:
                return entrada
        except:
            pass

def receber_entrada_i(limite_inf):
    while True:
        try:
            entrada = int(input('Escolha uma opção: '))
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
print('3: Raiz Cúbica')
print('4: Exponenciação')
func = receber_entrada_is(0, 3)

print("")

a, b = receber_valores()

print("")

print('Escolha a filosofia: ')
print('0: fechada')
print('1: aberta')
filosofia = receber_entrada_is(0, 1)

print("")

print('Escolha o grau: ')
print('0: grau 1')
print('1: grau 2')
print('2: grau 3')
print('3: grau 4')
grau = receber_entrada_is(0, 3)

print("")

print('Escolha o ponto de parada: ')
print('0: Partição')
print('1: Erro')
parada = receber_entrada_is(0, 1)

print("")

if (parada == 1):
    print("Digite o valor do erro:")
    erro = receber_entrada_i(0.00000001)

    resultado_atual, iteracoes = iterar(METODOS[filosofia][grau], FUNCOES[func], a, b, erro)
    print("Resultado: ", resultado_atual)
    print("Numero de Iteracoes: ", iteracoes)
else:
    print("Digite o número de partições")
    particoes = receber_entrada_i(0)

    resultado_atual, iteracoes = particionar(METODOS[filosofia][grau], FUNCOES[func], a, b, particoes)
    print("Resultado: ", resultado_atual)
    print("Numero de Iteracoes: ", iteracoes)
