def maior_divisor(n):
    """Maior divisor de n que seja menor que n (n >= 2)."""
    # TODO: comece o candidato em 1, ANTES do for
    # TODO: percorra de 1 ate n - 1 e, se dividir n sem resto, guarde o
    #       candidato novo
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert maior_divisor(2) == 1
assert maior_divisor(7) == 1
assert maior_divisor(10) == 5
assert maior_divisor(12) == 6
assert maior_divisor(100) == 50
assert maior_divisor(97) == 1
print("Exercício 05: todos os testes passaram!")
