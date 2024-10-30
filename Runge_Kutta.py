from Função import funcao


def runge_kutta(expressao, w, t_inicial, t_final, divisao):
    h = (t_final - t_inicial) / divisao
    i = 1
    while t_inicial <= t_final:
        k1 = h * funcao(expressao, {'t': t_inicial, 'w': w})
        k2 = h * funcao(expressao, {'t': t_inicial + h / 2, 'w': w + k1 / 2})
        k3 = h * funcao(expressao, {'t': t_inicial + h / 2, 'w': w + k2 / 2})
        k4 = h * funcao(expressao, {'t': t_inicial + h, 'w': w + k3})
        w = w + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        print(f"k1: {k1}")
        print(f"k2: {k2}")
        print(f"k3: {k3}")
        print(f"k4: {k4}")
        print(f"w{i}: {w}")
        i += 1
        t_inicial += h


print(runge_kutta('1 + (t-w)**2', 1, 2, 3, 2))
