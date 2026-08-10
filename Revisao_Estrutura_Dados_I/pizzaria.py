pizzas = ["Calabresa", "Margherita", "Portuguesa", "Frango com Catupiry", "Chocolate"]
precos = [45.00, 42.00, 48.00, 50.00, 40.00]

carrinho_nomes = []
carrinho_precos = []

print("=== PIZZARIA JUAN ===")

while True:
    print("\n--- Cardápio ---")
    for i in range(len(pizzas)):
        print(f"[{i + 1}] {pizzas[i]} - R$ {precos[i]:.2f}")
    print(" Finalizar pedido")

    opcao = int(input("\nEscolha o número da pizza: "))

    if opcao == 0:
        break
    elif 1 <= opcao <= len(pizzas):
        indice = opcao - 1
        
        carrinho_nomes.append(pizzas[indice])
        carrinho_precos.append(precos[indice])
        
        print(f"-> {pizzas[indice]} adicionada ao carrinho!")
    else:
        print("Opção inválida! Tente novamente.")

print("\n=== RESUMO DO PEDIDO ===")
if len(carrinho_nomes) > 0:
    print("Pizzas escolhidas:")
    for item in carrinho_nomes:
        print(f" - {item}")
    
    total = sum(carrinho_precos)
    print(f"\nValor total: R$ {total:.2f}")
else:
    print("Nenhum item foi adicionado.")

print("Obrigado pela preferência!")

