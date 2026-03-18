# importações das funções e dados fornecidos, inicio do código.
from calculos_agricolas import calcular_area, insumo_cana, insumo_laranja

# Listas (Vetores) para armazenar os dados
nomes_culturas = []
areas_calculadas = []
quantidade_insumo = []

while True:
    print("\n" + "="*30)
    print("      FARMTECH SOLUTIONS")
    print("="*30)
    print(" 1 - Entrada de Dados")
    print(" 2 - Saída dados")
    print(" 3 - Atualizar Dados")
    print(" 4 - Deletar Dado")
    print(" 5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        # Aqui você insere a lógica de entrada que conversamos antes
        print("\n--- CADASTRO DE PLANTIO ---")
        nome = input("Cultura (Cana/Laranja): ")
        b = float(input("Base: "))
        h = float(input("Altura: "))
        
        area_at = calcular_area(b, h)
        if nome.lower() == "cana":
            insumo_at = insumo_cana(area_at)
        else:
            insumo_at = insumo_laranja(area_at)
            
        nomes_culturas.append(nome)
        areas_calculadas.append(area_at)
        quantidade_insumo.append(insumo_at)
        print("Cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- RELATÓRIO ---")
        for i in range(len(nomes_culturas)):
            print(f"ID: {i} | {nomes_culturas[i]} | Área: {areas_calculadas[i]} | Insumo: {quantidade_insumo[i]}")

    elif opcao == "3":
        print("\n--- ATUALIZAR REGISTRO ---")
        if len(nomes_culturas) == 0:
            print("Nenhum dado para atualizar.")
        else:
            # Mostra os dados para o usuário saber o que escolher 
            for i in range(len(nomes_culturas)):
                print(f"ID: {i} | Cultura: {nomes_culturas[i]}")
            
            idx = int(input("\nDigite o ID que deseja atualizar: "))

            if idx >= 0 and idx < len(nomes_culturas):
                print(f"Atualizando {nomes_culturas[idx]}...")
                nova_b = float(input("Nova base: "))
                nova_h = float(input("Nova altura: "))
                
                nova_area = calcular_area(nova_b, nova_h)
                areas_calculadas[idx] = nova_area
                
                if nomes_culturas[idx].lower() == "cana":
                    quantidade_insumo[idx] = insumo_cana(nova_area)
                else: 
                    quantidade_insumo[idx] = insumo_laranja(nova_area)
                
                print("Registro atualizado com sucesso!")
            else:
                print("ID inválido!")

    elif opcao == "4":
        print("\n--- DELETAR REGISTRO ---")
        if len(nomes_culturas) == 0:
            print("Nenhum dado para deletar.")
        else:
            # Listar antes de deletar ajuda o usuário
            for i in range(len(nomes_culturas)):
                print(f"ID: {i} | Cultura: {nomes_culturas[i]}")
                
            idx = int(input("Digite o ID que deseja remover: "))
            
            if idx >= 0 and idx < len(nomes_culturas):
                removido = nomes_culturas.pop(idx)
                areas_calculadas.pop(idx)
                quantidade_insumo.pop(idx)
                print(f"Registro de {removido} removido com sucesso!")
            else:
                print("ID inválido!")

    elif opcao == "5":
        print("Finalizando o sistema da FarmTech. Até logo!")
        break
        
    else:
        print("Opção inválida! Tente novamente.")