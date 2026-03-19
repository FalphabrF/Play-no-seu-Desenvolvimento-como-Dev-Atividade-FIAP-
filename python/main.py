# ===============================
# FARMTECH SOLUTIONS - SISTEMA
# ===============================

# Importação das funções de cálculo (Pessoa 1)
from calculos_agricolas import calcular_area, insumo_cana, insumo_laranja

# Biblioteca para exportar dados para CSV (integração com R)
import csv

# ===============================
# VETORES (LISTAS) DE DADOS
# ===============================

# Cada lista representa uma coluna de dados
nomes_culturas = []
areas_calculadas = []
quantidade_insumo = []

# ===============================
# FUNÇÃO PARA SALVAR CSV
# ===============================

def salvar_csv():
    """
    Essa função exporta todos os dados armazenados
    para um arquivo CSV que será lido pelo R.
    """
    with open("dados_fazenda.csv", mode="w", newline="") as arquivo:
        writer = csv.writer(arquivo)

        # Cabeçalho do arquivo
        writer.writerow(["Cultura", "Area", "Insumo"])

        # Escrita dos dados linha por linha
        for i in range(len(nomes_culturas)):
            writer.writerow([
                nomes_culturas[i],
                areas_calculadas[i],
                quantidade_insumo[i]
            ])

    print("\n[SUCESSO] Dados exportados para 'dados_fazenda.csv'")

# ===============================
# MENU PRINCIPAL (LOOP)
# ===============================

while True:
    print("\n" + "="*30)
    print("      FARMTECH SOLUTIONS")
    print("="*30)
    print(" 1 - Entrada de Dados")
    print(" 2 - Saída de Dados")
    print(" 3 - Atualizar Dados")
    print(" 4 - Deletar Dado")
    print(" 5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # ===============================
    # OPÇÃO 1 - CADASTRO
    # ===============================
    if opcao == "1":
        print("\n--- CADASTRO DE PLANTIO ---")

        try:
            # Entrada de dados do usuário
            nome = input("Cultura (Cana/Laranja): ")
            b = float(input("Base (metros): "))
            h = float(input("Altura (metros): "))

            # Cálculo da área (função do Membro 1)
            area_at = calcular_area(b, h)

            # Cálculo de insumo baseado na cultura
            if nome.lower() == "cana":
                insumo_at = insumo_cana(area_at)
            elif nome.lower() == "laranja":
                insumo_at = insumo_laranja(area_at)
            else:
                print("\n[ERRO] Cultura inválida!")
                continue

            # Armazenando nos vetores
            nomes_culturas.append(nome)
            areas_calculadas.append(area_at)
            quantidade_insumo.append(insumo_at)

            print("\n[SUCESSO] Dados salvos com sucesso!")

        except ValueError:
            print("\n[ERRO] Use apenas números válidos para base e altura.")

    # ===============================
    # OPÇÃO 2 - LISTAR DADOS
    # ===============================
    elif opcao == "2":
        print("\n--- RELATÓRIO ---")

        if len(nomes_culturas) == 0:
            print("Nenhum dado cadastrado.")
        else:
            for i in range(len(nomes_culturas)):
                print(f"ID: {i} | {nomes_culturas[i]} | Área: {areas_calculadas[i]} | Insumo: {quantidade_insumo[i]}")

    # ===============================
    # OPÇÃO 3 - ATUALIZAR
    # ===============================
    elif opcao == "3":
        print("\n--- ATUALIZAR REGISTRO ---")

        if len(nomes_culturas) == 0:
            print("Nenhum dado para atualizar.")
        else:
            # Mostrar lista para o usuário escolher
            for i in range(len(nomes_culturas)):
                print(f"ID: {i} | Cultura: {nomes_culturas[i]}")

            try:
                idx = int(input("\nDigite o ID que deseja atualizar: "))

                if 0 <= idx < len(nomes_culturas):

                    print(f"Atualizando {nomes_culturas[idx]}...")

                    nova_b = float(input("Nova base: "))
                    nova_h = float(input("Nova altura: "))

                    # Recalcula área
                    nova_area = calcular_area(nova_b, nova_h)
                    areas_calculadas[idx] = nova_area

                    # Recalcula insumo baseado na cultura
                    if nomes_culturas[idx].lower() == "cana":
                        quantidade_insumo[idx] = insumo_cana(nova_area)
                    else:
                        quantidade_insumo[idx] = insumo_laranja(nova_area)

                    print("[SUCESSO] Registro atualizado!")

                else:
                    print("[ERRO] ID inválido!")

            except ValueError:
                print("[ERRO] Digite um número válido.")

    # ===============================
    # OPÇÃO 4 - DELETAR
    # ===============================
    elif opcao == "4":
        print("\n--- DELETAR REGISTRO ---")

        if len(nomes_culturas) == 0:
            print("[AVISO] Não há dados para deletar.")
        else:
            for i in range(len(nomes_culturas)):
                print(f"ID: {i} | Cultura: {nomes_culturas[i]}")

            try:
                idx = int(input("\nDigite o ID que deseja remover: "))

                if 0 <= idx < len(nomes_culturas):
                    removido = nomes_culturas.pop(idx)
                    areas_calculadas.pop(idx)
                    quantidade_insumo.pop(idx)

                    print(f"[SUCESSO] {removido} removido!")
                else:
                    print("[ERRO] ID inválido.")

            except ValueError:
                print("[ERRO] Digite apenas números.")

    # ===============================
    # OPÇÃO 5 - SAIR + EXPORTAR CSV
    # ===============================
    elif opcao == "5":
        salvar_csv()  # EXPORTA OS DADOS PARA O R

        print("\n" + "="*30)
        print("Dados da sessão encerrados.")
        print("    Até a próxima!")
        print("="*30)
        break

    # ===============================
    # OPÇÃO INVÁLIDA
    # ===============================
    else:
        print("[ERRO] Opção inválida!")