# Importa o modulo OS (Integra o programa e recursos do S.O)
import os
# Importa um modulo de manipulaçao de tempo
import time

# Abrindo o arquivo txt para leiruta
with open('hosts.txt') as file:
    # Criando uma variavel para o arquivo
    dump = file.read()
    # Colocando o conteudo do arquivo em linhas separadas
    dump = dump.splitlines()

    # percorrendo o arquivo e verificando cada IP
    for ip in dump:

        # Pular uma linha entre os programas
        print("\n")

        # Imprimir o nome do IP na tela entes de executa o programa
        print(f"Verificando IP {ip}")
        # Imprimindo o (*) 60 vezes
        print("*"*60)

        # verificando e enviando request para os IP do arquivo
        os.system(f'ping -n 4 {ip}')
        # Imprimindo o (*) 60 vezes
        print("*" * 60)

        # Tempo de espera de um comando para o outro
        time.sleep(5)