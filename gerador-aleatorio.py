import random #import de bibliotecas
import time   #import de bibliotecas
import psutil #import de bibliotecas

def obter_uso_cpu(): #calculadora de uso de CPU
    return psutil.cpu_percent(interval=1) 

def obter_uso_ram(): #Calculadora de uso de RAM
    return psutil.virtual_memory().used

uso_cpu_inicial = obter_uso_cpu() #contabiliza o uso da CPU antes de iniciar
uso_ram_inicial = obter_uso_ram() #contabiliza o uso da CPU antes de iniciar
tempo_inicio = time.time()        #cronometro

nome_arquivo = "1b.txt" #nome do arquivo a ser gerado

tamanho_bloco = 1000000 #criação de blocos (o arquivo vai criar um milhão de numeros por vez) pois o computador pode não suportar criar tudo ao mesmo tempo
total_numeros = 1000000000 #tamanho total para o arquivo

with open(nome_arquivo, "w") as arquivo: #escreve dentro do arquivo
    for _ in range(total_numeros // tamanho_bloco): #aqui cria o arquivo segundo os tamanhos definidos a cima
        numeros_aleatorios = [random.randint(0, 1000000000) for _ in range(tamanho_bloco)] #aleatorizando os valores
        arquivo.write(','.join(map(str, numeros_aleatorios)) + '\n') 

tempo_fim = time.time() #final do tempo de criação do arquivo

uso_cpu_final = obter_uso_cpu() #uso da CPU
uso_ram_final = obter_uso_ram() #uso da RAM

tempo_decorrido = tempo_fim - tempo_inicio  #tempo utilizado
cpu_usada = uso_cpu_final - uso_cpu_inicial #CPU utilzada
ram_usada = (uso_ram_final - uso_ram_inicial) / (1024 * 1024) #RAM utlizada

print(f"Números aleatórios foram salvos em '{nome_arquivo}'")
print(f"Tempo decorrido: {tempo_decorrido:.6f} segundos")
print(f"Uso de CPU: {cpu_usada:.2f}%")
print(f"Uso de RAM: {ram_usada:.6f} MB")
