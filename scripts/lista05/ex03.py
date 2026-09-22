def valor_multa(velocidade):
    """Devolve o valor da multa em reais: R$ 5 por km/h acima de 80."""
    # TODO: se passou de 80, cobre 5 reais por km/h excedente; senão, 0.
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert valor_multa(90) == 50
assert valor_multa(81) == 5
assert valor_multa(80) == 0
assert valor_multa(60) == 0
assert valor_multa(120) == 200
print("Exercício 03: todos os testes passaram!")
