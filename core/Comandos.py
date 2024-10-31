import sys
from metodos.Runge_Kutta import runge_kutta_4_ordem

# Dicionário para armazenar os comandos disponíveis
comandos = {}
descricao_comandos = {}


# Decorator para registrar comandos e adicion-a-los ao dicionário de comandos
def command(name, description=None):
    def decorator(func):
        comandos[name] = func
        descricao_comandos[name] = (
            description 
            if description 
            else func.__doc__ or func.__name__.split("_", 1)[-1].capitalize()
        )
        return func
    return decorator


@command("sair", description="Encerra a execução do programa.")
def command_exit():
    print("Encerrando...")
    sys.exit(0)


@command("ajuda", description="Exibe a lista de comandos disponíveis e suas descrições.")
def command_help():
    print("Comandos disponíveis:")
    for i, comando in enumerate(comandos.keys()):
        print(f"\t[{i}] {comando}: {descricao_comandos[comando]}")
        

@command("runge-kutta", description="Executa o Método de Runge-Kutta.")
def command_runge_kutta():
    print("\nInsira a expressão para y':")
    expressao = input(">> y' = ")
    
    print("\nInsira o valor para w:")
    w = float(input(">> w = "))
    
    print("\nInsira o valor inicial para t_inicial:")
    t_inicial = float(input(">> t_inicial = "))
    
    print("\nInsira o valor final para t_final:")
    t_final = float(input(">> t_final = "))
    
    print("\nInsira o número de divisões/passos:")
    divisao = int(input(">> divisao = "))
    
    print("\nResultado:\n")
    runge_kutta_4_ordem(expressao, w, t_inicial, t_final, divisao)
   