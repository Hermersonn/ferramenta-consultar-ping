# Importa o modulo OS (integra os pragrama e recursos do S.O)
import os

# Imprimindo o (-) 60 vezes
print("-"*60)

# Variavel que ira receber o IP ou Host que vai ser verificado
ip_host = input("Digite o IP ou Host a ser verificado: ")

# Imprimindo o (-) 60 vezes
print("-"*60)
# Pulando uma linha entre os print
print("\n")
# Imprimindo o (#) 60 vezes
print("#"*60)

# Chamando o modulo com o comando PING
# O (-n 6) é o numero de Request que sera enviado
os.system(f'ping -n 6 {ip_host}')

#imprimindo o (#) 60 vezes
print("#"*60)