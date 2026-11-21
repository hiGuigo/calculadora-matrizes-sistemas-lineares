# Calculadora de matrizes e sistemas lineares

Programa de terminal para operações com matrizes e classificação de sistemas lineares. Os cálculos são feitos com NumPy.

## Especificações

- Python 3.12
- NumPy

## Manual do usuário

1. Instale o Python 3.12, caso ainda não esteja instalado.
2. Abra um terminal na pasta do projeto.
3. Crie o ambiente virtual: `python3 -m venv .venv`
4. Ative o ambiente virtual:
   - Linux/macOS: `source .venv/bin/activate`
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
5. Instale a dependência: `pip install -r requirements.txt`
6. Execute o programa: `python main.py`
7. No menu, escolha `1` para as operações de matrizes ou `2` para sistemas lineares. Digite os elementos de cada linha separados por espaço.
8. Depois de cada cálculo, o programa retorna ao menu. Escolha `0` para sair.

Nas operações de matrizes estão disponíveis soma, multiplicação por escalar, multiplicação entre matrizes e transposta. Para um sistema, informe em cada linha os coeficientes das variáveis seguidos do termo independente. O programa informa se o sistema é SPD, SPI ou SI.

## Testes manuais

### Soma de matrizes

Escolha a operação `1`. Para as matrizes A e B, informe respectivamente 2 linhas e 2 colunas, com estas linhas:

```text
1 2
3 4
```

Para B, informe também 2 linhas e 2 colunas:

```text
5 6
7 8
```

Resultado esperado: `[[ 6  8] [10 12]]`.

### Multiplicação por escalar

Escolha a operação `2`, informe matriz A `2 x 2` com linhas `1 2` e `3 4` e digite o escalar `2`.

Resultado esperado: `[[2 4] [6 8]]`.

### Multiplicação entre matrizes

Escolha a operação `3`. Informe A `2 x 2` com linhas `1 2` e `3 4`; informe B `2 x 2` com linhas `5 6` e `7 8`.

Resultado esperado: `[[19 22] [43 50]]`.

### Matriz transposta

Escolha a operação `4` e informe A `2 x 3` com linhas `1 2 3` e `4 5 6`.

Resultado esperado:

```text
[[1 4]
 [2 5]
 [3 6]]
```

### Sistema SPD

No menu principal, escolha `2`. Informe `2` equações e `2` variáveis. Digite cada linha com os dois coeficientes e o termo independente:

```text
1 1 3
1 -1 1
```

Resultado esperado: classificação SPD e solução `[2 1]` (x = 2, y = 1).

### Sistema SPI

Informe `2` equações e `2` variáveis:

```text
1 1 2
2 2 4
```

Resultado esperado: classificação SPI, indicação de infinitas soluções e uma solução particular (o NumPy pode exibi-la como valores decimais aproximados).

### Sistema SI

Informe `2` equações e `2` variáveis:

```text
1 1 2
1 1 3
```

Resultado esperado: classificação SI (Sistema Impossível).
