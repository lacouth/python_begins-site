def conta_multiplos(inicio, fim, divisor):
    """Quantos numeros de inicio ate fim (inclusive) sao multiplos de divisor."""
    # TODO: contador em 0, ANTES do for
    # TODO: percorra de inicio ate fim INCLUSIVE e teste o resto da divisao
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert conta_multiplos(1, 10, 3) == 3
assert conta_multiplos(1, 100, 10) == 10
assert conta_multiplos(1, 10, 11) == 0
assert conta_multiplos(5, 5, 5) == 1
assert conta_multiplos(1, 20, 2) == 10
assert conta_multiplos(10, 1, 2) == 0
print("Exercício 02: todos os testes passaram!")
