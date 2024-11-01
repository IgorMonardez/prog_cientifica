from core.Funcao import funcao
import math

def runge_kutta_4_ordem(expressao, w, t_inicial, t_final, divisao):
    h = (t_final - t_inicial) / divisao
    i = 1
    while t_inicial <= t_final:
        print(f"Iteração {i}")
        k1 = h * funcao(expressao, {'t': t_inicial, 'w': w, 'e': math.e})
        k2 = h * funcao(expressao, {'t': t_inicial + h / 2, 'w': w + k1 / 2, 'e': math.e})
        k3 = h * funcao(expressao, {'t': t_inicial + h / 2, 'w': w + k2 / 2, 'e': math.e})
        k4 = h * funcao(expressao, {'t': t_inicial + h, 'w': w + k3, 'e': math.e})
        w = w + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        print(f"k1: {k1}")
        print(f"k2: {k2}")
        print(f"k3: {k3}")
        print(f"k4: {k4}")
        print(f"w{i}: {w}")
        i += 1
        t_inicial += h
        print()

if __name__ == "__main__":
    print(runge_kutta_4_ordem('1 + (t-w)**2', 1, 2, 3, 2))
