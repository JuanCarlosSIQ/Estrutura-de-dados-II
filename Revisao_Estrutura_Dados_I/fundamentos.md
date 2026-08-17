# ==============================================================================
# TÓPICO 1: Dados na Memória
# Demonstração de referências de variáveis e busca do ID único na memória RAM
# ==============================================================================

# Criação de um objeto do tipo inteiro (20) e atribuição à variável 'idade'
idade = 20

# Exibe o valor contido e o endereço único de memória atribuído pelo Python
print(f"Valor inicial da variável 'idade': {idade}")
print(f"Endereço/ID na memória RAM (id(idade)): {id(idade)}")

# Ao reatribuir um novo valor, Python cria um novo objeto na memória
idade = 21
print(f"\nNovo valor atribuído a 'idade': {idade}")
print(f"Novo endereço/ID na memória RAM: {id(idade)}")
