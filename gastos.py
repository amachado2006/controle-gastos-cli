"""
Controle de Gastos Pessoais - CLI
Aplicação para registrar e acompanhar gastos do dia a dia.
"""

import json
import os

ARQUIVO_DADOS = "dados/gastos.json"


def carregar_gastos():
    """Carrega os gastos salvos do arquivo JSON."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_gastos(gastos):
    """Salva os gastos no arquivo JSON."""
    os.makedirs(os.path.dirname(ARQUIVO_DADOS), exist_ok=True)
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)


def adicionar_gasto(descricao, valor, categoria):
    """Adiciona um novo gasto à lista."""
    if not descricao or not descricao.strip():
        raise ValueError("A descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    gastos = carregar_gastos()
    novo = {
        "id": len(gastos) + 1,
        "descricao": descricao.strip(),
        "valor": round(valor, 2),
        "categoria": categoria.strip() if categoria else "Outros",
    }
    gastos.append(novo)
    salvar_gastos(gastos)
    return novo


def listar_gastos():
    """Retorna todos os gastos registrados."""
    return carregar_gastos()


def calcular_total():
    """Calcula o total de todos os gastos."""
    gastos = carregar_gastos()
    return round(sum(g["valor"] for g in gastos), 2)


def remover_gasto(gasto_id):
    """Remove um gasto pelo ID. Retorna True se removido, False se não encontrado."""
    gastos = carregar_gastos()
    novos_gastos = [g for g in gastos if g["id"] != gasto_id]
    if len(novos_gastos) == len(gastos):
        return False
    salvar_gastos(novos_gastos)
    return True


def exibir_menu():
    print("\n===== CONTROLE DE GASTOS PESSOAIS =====")
    print("1. Adicionar gasto")
    print("2. Listar gastos")
    print("3. Ver total gasto")
    print("4. Remover gasto")
    print("0. Sair")
    print("========================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            descricao = input("Descrição do gasto: ")
            try:
                valor = float(input("Valor (R$): "))
                categoria = input("Categoria (ex: Alimentação, Transporte): ")
                gasto = adicionar_gasto(descricao, valor, categoria)
                print(f"\n✅ Gasto adicionado: {gasto['descricao']} - R$ {gasto['valor']:.2f}")
            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "2":
            gastos = listar_gastos()
            if not gastos:
                print("\nNenhum gasto registrado ainda.")
            else:
                print("\n--- SEUS GASTOS ---")
                for g in gastos:
                    print(f"[{g['id']}] {g['descricao']} | R$ {g['valor']:.2f} | {g['categoria']}")

        elif opcao == "3":
            total = calcular_total()
            print(f"\n💰 Total gasto: R$ {total:.2f}")

        elif opcao == "4":
            try:
                gasto_id = int(input("ID do gasto a remover: "))
                if remover_gasto(gasto_id):
                    print("✅ Gasto removido com sucesso.")
                else:
                    print("❌ Gasto não encontrado.")
            except ValueError:
                print("❌ ID inválido.")

        elif opcao == "0":
            print("\nAté logo! 👋")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
