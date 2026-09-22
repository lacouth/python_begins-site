def meses_ate_meta(saldo, deposito_mensal, meta):
    """Meses de deposito ate o saldo alcancar ou passar a meta."""
    # TODO: um contador de meses, ANTES do laco
    # TODO: enquanto o saldo for MENOR que a meta, deposite e conte um mes
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert meses_ate_meta(0, 100, 500) == 5
assert meses_ate_meta(200, 100, 500) == 3
assert meses_ate_meta(500, 100, 500) == 0
assert meses_ate_meta(600, 100, 500) == 0
assert meses_ate_meta(0, 150, 500) == 4
assert meses_ate_meta(50, 25, 100) == 2
print("Exercício 05: todos os testes passaram!")
