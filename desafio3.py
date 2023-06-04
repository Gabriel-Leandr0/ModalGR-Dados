from datetime import datetime


def emprestimo(nome_colaborador, data_admissao, salario_atual, valor_emprestimo):
    tempo_casa = (datetime.now().date() - data_admissao).days / 365

    # Verifica tempo de casa > 5 anos
    if tempo_casa < 5:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return

    # Verifica valor emprestimo > 2x salario atual
    # Se emprestimo > 2x salario atual , emprestimo = 2 x salario atual
    if valor_emprestimo > (2 * salario_atual):
        valor_emprestimo = 2 * salario_atual

    # Verifica valor emprestimo é múltiplo de 2
    if 0 != valor_emprestimo % 2:
        print("Insira um valor válido!")
        return

    # Cálculo das notas de maior valor
    notas_maior_valor = {
        100: int(valor_emprestimo // 100),
        50: int((valor_emprestimo % 100) // 50),
        20: int(((valor_emprestimo % 100) % 50) // 20),
        10: int((((valor_emprestimo % 100) % 50) % 20) // 10),
        5: int(((((valor_emprestimo % 100) % 50) % 20) % 10) // 5),
        2: 0  # Inicialmente, definimos a quantidade de notas de 2 como zero
    }
    # Verifica se o resto de 5 é igual a zero
    if valor_emprestimo % 5 != 0:
        # Utiliza notas de 2 ao invés de notas de 5
        notas_maior_valor[2] = int(((((valor_emprestimo % 100) % 50) % 20) % 10) // 2)
        notas_maior_valor[5] = 0

    # Cálculo das notas de menor valor
    notas_menor_valor = {
        20: int(valor_emprestimo // 20),
        10: int((valor_emprestimo % 20) // 10),
        5: int((valor_emprestimo % 10) // 5),
        2: 0  # Inicialmente, definimos a quantidade de notas de 2 como zero
    }
    # Verifica se o resto de 5 é igual a zero
    if valor_emprestimo % 5 != 0:
        # Utiliza notas de 2 ao invés de notas de 5
        notas_menor_valor[2] = int(((valor_emprestimo % 20) % 10) // 2)
        notas_menor_valor[5] = 0

    # Cálculo das notas meio a meio maior
    valor_meio_a_meio = valor_emprestimo // 2
    notas_meio_a_meio_maior = {
        100: int(valor_meio_a_meio // 100),
        50: int((valor_meio_a_meio % 100) // 50),
        20: int(((valor_meio_a_meio % 100) % 50) // 20),
        10: int((((valor_meio_a_meio % 100) % 50) % 20) // 10),
        5: int(((((valor_meio_a_meio % 100) % 50) % 20) % 10) // 5),
        2: 0  # Inicialmente, definimos a quantidade de notas de 2 como zero
    }
    # Verifica se o resto de 5 é igual a zero
    if valor_meio_a_meio % 5 != 0:
        # Utiliza notas de 2 ao invés de notas de 5
        notas_meio_a_meio_maior[2] = int(((((valor_meio_a_meio % 100) % 50) % 20) % 10) // 2)
        notas_meio_a_meio_maior[5] = 0

    # Cálculo das notas meio a meio menor
    valor_restante_meio_a_meio = valor_meio_a_meio
    notas_meio_a_meio_menor = {
        20: int(valor_restante_meio_a_meio // 20),
        10: int((valor_restante_meio_a_meio % 20) // 10),
        5: int((valor_restante_meio_a_meio % 10) // 5),
        2: 0  # Inicialmente, definimos a quantidade de notas de 2 como zero
    }
    # Verifica se o resto de 5 é igual a zero
    if valor_restante_meio_a_meio % 5 != 0:
        # Utiliza notas de 2 ao invés de 5
        notas_meio_a_meio_menor[2] = int(((valor_restante_meio_a_meio % 20) % 10) // 2)
        notas_meio_a_meio_menor[5] = 0

    # Exibição das opções de retirada
    print(f"\nValor empréstimo: {valor_emprestimo} reais")

    print("\nNotas de maior valor:")
    for nota, quantidade in notas_maior_valor.items():
        if quantidade > 0:
            print(f"{quantidade} x {nota} reais")

    print("\nNotas de menor valor:")
    for nota, quantidade in notas_menor_valor.items():
        if quantidade > 0:
            print(f"{quantidade} x {nota} reais")

    print("\nNotas meio a meio:")
    print(f"{valor_meio_a_meio} reais em notas de maior valor:")
    for nota, quantidade in notas_meio_a_meio_maior.items():
        if quantidade > 0:
            print(f"{quantidade} x {nota} reais")

    print(f"{valor_meio_a_meio} reais em notas de menor valor:")
    for nota, quantidade in notas_meio_a_meio_menor.items():
        if quantidade > 0:
            print(f"{quantidade} x {nota} reais")


# Entrada
nome_colaborador = input("Nome do colaborador: ")
data_admissao = datetime.strptime(input("Data de admissão (formato: dd/mm/aaaa): "), "%d/%m/%Y").date()
salario_atual = float(input("Salário atual (formato: 1000.00): "))
valor_emprestimo = float(input("Valor de empréstimo: "))

emprestimo(nome_colaborador, data_admissao, salario_atual, valor_emprestimo)
