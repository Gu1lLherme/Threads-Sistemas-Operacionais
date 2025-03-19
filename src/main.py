import threading
import time
import random

lock = threading.Lock()  # Mutex para sincronização
pedidos_processados = 0  # Recurso compartilhado

# Funções para processamento sequencial
def validar_dados(pedido_id):
    time.sleep(random.uniform(0.5, 1.5)) #simula um tempo de execução variável de cada processo da empresa 
    print(f"Pedido {pedido_id}: Dados validados")

def conferir_estoque(pedido_id):
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Pedido {pedido_id}: Estoque conferido")

def calcular_frete(pedido_id):
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Pedido {pedido_id}: Frete calculado")

def emitir_nota_fiscal(pedido_id):
    time.sleep(random.uniform(0.5, 1.5))
    print(f"Pedido {pedido_id}: Nota fiscal emitida")

# Execução sequencial
def processar_pedido(pedido_id):
    global pedidos_processados
    validar_dados(pedido_id)
    conferir_estoque(pedido_id)
    calcular_frete(pedido_id)
    emitir_nota_fiscal(pedido_id)
    
    with lock:  # Garante exclusão mútua na atualização do contador
        pedidos_processados += 1
        print(f"Pedido {pedido_id} finalizado! Total processado: {pedidos_processados}\n")

# Execução Threads - sincronização MUTEX
def processar_pedidos_com_threads(pedidos):
    threads = []
    for pedido_id in pedidos:
        t = threading.Thread(target=processar_pedido, args=(pedido_id,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

# Algortimo Principal
def main():
    pedidos = [1, 2, 3, 4, 5]
    
    print("Execução Sequencial:")
    inicio = time.time()
    for pedido in pedidos:
        processar_pedido(pedido)
    fim = time.time()
    print(f"Tempo total (Sequencial): {fim - inicio:.2f} segundos\n")
    
    global pedidos_processados
    pedidos_processados = 0  # Reset para execução com threads
    print("=" * 20)
    
    print("Execução com Threads:")
    inicio = time.time()
    processar_pedidos_com_threads(pedidos)
    fim = time.time()
    print(f"Tempo total (Threads): {fim - inicio:.2f} segundos\n")

if __name__ == "__main__":
    main()