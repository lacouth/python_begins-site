def soma_digitos(n):
    """Devolve a soma dos algarismos do inteiro n (n >= 0)."""
    # TODO: acumulador em 0, ANTES do laco
    # TODO: enquanto n > 0: pegue o ultimo algarismo com % 10, some,
    #       e descarte-o com // 10
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert soma_digitos(0) == 0
assert soma_digitos(7) == 7
assert soma_digitos(137) == 11
assert soma_digitos(4321) == 10
assert soma_digitos(1000) == 1
assert soma_digitos(999999) == 54
print("Exercício 04: todos os testes passaram!")
