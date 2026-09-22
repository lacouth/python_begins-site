def conta_digitos(n):
    """Devolve quantos algarismos tem o inteiro n (n >= 0)."""
    # TODO: trate o caso n == 0 separadamente
    # TODO: enquanto sobrar numero, jogue fora o ultimo algarismo com // 10
    #       e conte mais um
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert conta_digitos(0) == 1
assert conta_digitos(7) == 1
assert conta_digitos(42) == 2
assert conta_digitos(137) == 3
assert conta_digitos(1000) == 4
assert conta_digitos(987654321) == 9
print("Exercício 02: todos os testes passaram!")
