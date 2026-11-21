import numpy as np

np.set_printoptions(
    formatter={
        "float_kind": lambda valor: str(int(valor)) if valor.is_integer() else str(valor)
    }
)

def ler_matriz(nome):
    linhas = int(input(f"Quantidade de linhas da matriz {nome}: "))
    colunas = int(input(f"Quantidade de colunas da matriz {nome}: "))

    if linhas <= 0 or colunas <= 0:
        raise ValueError("A matriz precisa ter pelo menos uma linha e uma coluna.")

    valores = []
    for i in range(linhas):
        linha = input(
            f"Digite os {colunas} elementos da linha {i + 1}, separados por espaço: "
        ).split()
        if len(linha) != colunas:
            raise ValueError(f"A linha precisa conter exatamente {colunas} elementos.")
        valores.append([float(valor) for valor in linha])

    return np.array(valores, dtype=float)

def calcular_matrizes():
    print("\n## CÁLCULO DE MATRIZES ##")
    print("1. Soma de matrizes")
    print("2. Multiplicação por escalar")
    print("3. Multiplicação entre matrizes")
    print("4. Transposta")
    operacao = input("Escolha uma operação: ")

    if operacao == "1":
        matriz_a = ler_matriz("A")
        matriz_b = ler_matriz("B")
        if matriz_a.shape != matriz_b.shape:
            print("Não é possível somar matrizes de dimensões diferentes.")
            return
        resultado = matriz_a + matriz_b
        print("Resultado da soma:")
    elif operacao == "2":
        matriz = ler_matriz("A")
        escalar = float(input("Digite o escalar: "))
        resultado = matriz * escalar
        print("Resultado da multiplicação por escalar:")
    elif operacao == "3":
        matriz_a = ler_matriz("A")
        matriz_b = ler_matriz("B")
        if matriz_a.shape[1] != matriz_b.shape[0]:
            print("É impossível multiplicar essas matrizes.")
            return
        resultado = matriz_a @ matriz_b
        print("Resultado da multiplicação entre matrizes:")
    elif operacao == "4":
        matriz = ler_matriz("A")
        resultado = matriz.T
        print("Matriz transposta:")
    else:
        print("Opção inválida.")
        return

    print(resultado)

def calcular_sistema_linear():
    print("\n## SISTEMAS LINEARES ##")
    equacoes = int(input("Quantidade de equações: "))
    variaveis = int(input("Quantidade de variáveis: "))
    if equacoes <= 0 or variaveis <= 0:
        raise ValueError("Informe pelo menos uma equação e uma variável.")

    coeficientes = []
    resultados = []
    for i in range(equacoes):
        linha = input(
            f"Equação {i + 1}: digite {variaveis} coeficientes e o resultado, separados por espaço: "
        ).split()
        if len(linha) != variaveis + 1:
            raise ValueError(
                f"Digite exatamente {variaveis} coeficientes e o resultado."
            )
        coeficientes.append([float(valor) for valor in linha[:-1]])
        resultados.append(float(linha[-1]))

    matriz_a = np.array(coeficientes, dtype=float)
    vetor_b = np.array(resultados, dtype=float)
    posto_a = np.linalg.matrix_rank(matriz_a)
    matriz_ampliada = np.column_stack((matriz_a, vetor_b))
    posto_ampliada = np.linalg.matrix_rank(matriz_ampliada)

    if posto_a != posto_ampliada:
        print("Classificação: SI (Sistema Impossível).")
    elif posto_a == variaveis:
        solucao = np.linalg.lstsq(matriz_a, vetor_b, rcond=None)[0]
        print("Classificação: SPD (Sistema Possível Determinado).")
        print("Solução:", solucao)
    else:
        solucao = np.linalg.lstsq(matriz_a, vetor_b, rcond=None)[0]
        print("Classificação: SPI (Sistema Possível Indeterminado).")
        print("Uma solução particular:", solucao)
        print("O sistema possui infinitas soluções (há variáveis livres).")

def main():
    while True:
        print("\n## OPERAÇÕES ##")
        print("1. Cálculo de Matrizes")
        print("2. Sistemas Lineares")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                calcular_matrizes()
            elif opcao == "2":
                calcular_sistema_linear()
            elif opcao == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Entrada inválida: {erro}")

if __name__ == "__main__":
    main()
