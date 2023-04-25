from math import sqrt

w = {
    2: [1, 1],
    3: [5/9, 8/9, 5/9],
    4: [0.347854845137454, 0.652145154862546, 0.652145154862546, 0.347854845137454]
}

alfa = {
    2: [-sqrt(1/3), sqrt(1/3)],
    3: [-sqrt(3/5), 0, sqrt(3/5)],
    4: [-sqrt((3/7) + ((2*sqrt(6/5)) / 7)), -sqrt((3/7) - ((2*sqrt(6/5))/7)), sqrt((3/7) - ((2*sqrt(6/5))/7)), sqrt((3/7) + ((2*sqrt(6/5)) / 7))]
}

def gauss_legendre(fx, xi, xf, qtd_pontos):
    aux = 0
    for i in range(qtd_pontos):
        aux += fx( x(xi, xf, alfa[qtd_pontos][i])) * w[qtd_pontos][i]

    return ((xf - xi)/2 * aux)

def x(xi, xf, alfa):
    return ((xf + xi) / 2) + ((xf - xi) / 2) * alfa