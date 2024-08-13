import random       #import de bibliotecas 
import psutil       #import de bibliotecas
import time         #import de bibliotecas
import pandas as pd #import de bibliotecas

def obter_uso_sistema(): #função para analisar o uso do sistema
    processo = psutil.Process() 
    uso_ram = processo.memory_info().rss / (1024 * 1024)#uso de ram
    uso_cpu = psutil.cpu_percent(interval=1) #uso de RAM
    return uso_ram, uso_cpu #retorna o uso da RAM e do CPU

def carregar_arquivo(nome_arquivo, delimitador=','): #carrega o arquivo para analise
    tempo_inicio = time.time() #inicia o cronometro 
    
    ram_inicial, cpu_inicial = obter_uso_sistema() #analisa o uso de processamento no inicio
    
    df = pd.read_csv(nome_arquivo, delimiter=delimitador, header=None) # Leitura do arquivo .txt

    ram_final, cpu_final = obter_uso_sistema() #o fim do uso de RAM e CPU
    tempo_fim = time.time() #tempo de uso
     
    indice_aleatorio = random.randint(0, len(df) - 1) # Seleciona um índice aleatório e o número correspondente
    numero_aleatorio = df.iloc[indice_aleatorio, 0]   # Seleciona um índice aleatório e o número correspondente

    ram_consumida = ram_final - ram_inicial    #consumo de RAM
    cpu_consumida = cpu_final - cpu_inicial    #consumo de CPU
    tempo_decorrido = tempo_fim - tempo_inicio #tempo utilizado para a rotina do código

    return numero_aleatorio, indice_aleatorio, ram_consumida, cpu_consumida, tempo_decorrido #retorna o tempo e o uso de RAM e CPu

nome_arquivo = 'caminho para o seu arquivo.txt/.csv/.xlsx ...' #caminho para o meu arquivo (lembre-se de alterar a barra de "\" para "/")
numero_aleatorio, numero_linha, ram_usada, cpu_usada, tempo_decorrido = carregar_arquivo(nome_arquivo) 
print("print par a pasta de 1bilhão de valores")
print(f"Número aleatório: {numero_aleatorio} (Linha: {numero_linha + 1})")
print(f"RAM usada: {ram_usada:.2f} MB")
print(f"CPU usada: {cpu_usada:.2f}%")
print(f"Tempo para carregar o arquivo: {tempo_decorrido:.2f} segundos")
