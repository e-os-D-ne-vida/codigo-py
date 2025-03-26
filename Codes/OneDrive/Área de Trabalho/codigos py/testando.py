import threading
import time

def minha_tarefa():
    for i in range(5):
        print(f"Executando tarefa {i + 1}")
        time.sleep(1)

# Criando uma thread para executar a função
thread = threading.Thread(target=minha_tarefa)

# Iniciando a thread
thread.start()

# A thread principal continua executando
print("A thread principal continua rodando enquanto a tarefa é executada...")

# Espera a thread terminar
#thread.join()
print("Tarefa finalizada!")
