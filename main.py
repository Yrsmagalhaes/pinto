def exibir_menu(titulo, opcoes):
    print(f"\n--- {titulo} ---")
    for chave, valor in opcoes.items():
        print(f"[{chave}] {valor}")
    return input("\nComo posso ajudar? Digite a opção: ").strip().lower()

def main():
    print("Olá! Sou o seu assistente inteligente. Estou aqui para otimizar o seu fluxo de trabalho.")
    
    menus = {
        "principal": {"1": "Equipa Técnica", "2": "Equipa Administrativa"},
        "tecnica": {
            "a": "Estado do equipamento", "b": "Diagnóstico de avarias",
            "c": "Histórico técnico", "d": "Apoio em campo"
        },
        "adm": {
            "a": "Gestão de armazém", "b": "Identificação de material",
            "c": "Compras e reposição", "d": "Custos e eficiência",
            "e": "Contratos e clientes"
        }
    }

    escolha = exibir_menu("MENU PRINCIPAL", menus["principal"])

    if escolha == "1":
        sub_escolha = exibir_menu("EQUIPA TÉCNICA", menus["tecnica"])
        if sub_escolha in menus["tecnica"]:
            print(f"\n[OK] Acedendo a: {menus['tecnica'][sub_escolha]}...")
    elif escolha == "2":
        sub_escolha = exibir_menu("EQUIPA ADMINISTRATIVA", menus["adm"])
        if sub_escolha in menus["adm"]:
            print(f"\n[OK] Acedendo a: {menus['adm'][sub_escolha]}...")
    else:
        print("\nOpção não reconhecida. Reinicie para tentar novamente.")

if __name__ == "__main__":
    main()
