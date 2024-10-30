import sys
from core.Comandos import comandos, descricao_comandos


def main():
    lista_comandos = list(comandos.items())
    print("============== Calculadora de métodos numéricos ==============\n")
    print("Digite o número ou o nome do comando para executá-lo.\n")

    for i, (comando, funcao) in enumerate(lista_comandos):
        print(f"[{i}] {comando}: {descricao_comandos[comando]}")
        
    while True:
        try:
            user_input = input("\n>> ").strip()
            if not user_input:
                continue

            partes = user_input.split()
            comando = partes[0]
            args = partes[1:]
            
            if comando.isdigit():
                try:
                    funcao = lista_comandos[int(comando)][1]
                    funcao(*args)
                    print("\nExecutado com sucessso. Digite outro comando para continuar.")
                except IndexError:
                    print(f"Comando desconhecido: {comando}. Digite 'ajuda' para obter uma lista de comandos disponíveis.")
                    continue
            elif comando in comandos:
                funcao = comandos[comando]
                funcao(*args)
            else:
                print(f"Comando desconhecido: {comando}. Digite 'ajuda' para obter uma lista de comandos disponíveis.")
        
        except KeyboardInterrupt:
            print("\nInterrupção detectada. Encerrando...")
            sys.exit(0)
        
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()