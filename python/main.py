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
        print("\n--- CADASTRO DE PLANTIO ---")
        try:
            nome = input("Cultura (Cana/Laranja): ")
            b = float(input("Base (metros): "))
            h = float(input("Altura (metros): "))
            
            # Aqui chamamos as funções do seu colega (Membro 1)
            area_at = calcular_area(b, h)
            
            if nome.lower() == "cana":
                insumo_at = insumo_cana(area_at)
            else:
                insumo_at = insumo_laranja(area_at)
            
            # Guardando tudo nos seus vetores (Listas)
            nomes_culturas.append(nome)
            areas_calculadas.append(area_at)
            quantidade_insumo.append(insumo_at)
            
            print("\n[SUCESSO] Dados salvos com sucesso!")

        except ValueError:
            # Se o usuário digitar 'dez' em vez de '10', ele cai aqui:
            print("\n[ERRO] Por favor, use apenas números para Base e Altura.")
            print("Retornando ao menu principal...")

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
        
        # Primeiro, verificamos se existe algo cadastrado (len > 0)
        if len(nomes_culturas) > 0:
            # Mostramos a lista para o usuário ver o ID que quer apagar
            for i in range(len(nomes_culturas)):
                print(f"ID: {i} | Cultura: {nomes_culturas[i]}")
            
            try:
                idx = int(input("\nDigite o ID que deseja remover: "))
                
                # Verificamos se o número que ele digitou existe na lista
                if 0 <= idx < len(nomes_culturas):
                    # O comando .pop(idx) remove o item daquela posição
                    removido = nomes_culturas.pop(idx)
                    areas_calculadas.pop(idx)
                    quantidade_insumo.pop(idx)
                    
                    print(f"\n[SUCESSO] Registro de {removido} removido!")
                else:
                    print("\n[ERRO] Esse ID não existe.")
            
            except ValueError:
                print("\n[ERRO] Digite apenas o número do ID.")
        
        else:
            # Se a lista estiver vazia (len == 0), ele cai aqui:
            print("\n[AVISO] Não há nenhum dado cadastrado para deletar.")
        
    elif opcao == "5":
         print("\n" + "="*30)
         print("Dados da sessão encerrados.")
         print("    Até a próxima!")
         print("="*30)
         break #Encerra o programa.
             