from sympy import symbols, sympify


def funcao(formula, valores):
    try:
        # Converte a fórmula para uma expressão sympy
        expr = sympify(formula)

        # Avalia a expressão com os valores das variáveis
        resultado = expr.evalf(subs=valores)
        return resultado
    except Exception as e:
        print(f"Ocorreu um erro ao avaliar a fórmula: {e}")
