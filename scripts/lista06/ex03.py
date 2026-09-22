def categoria(idade):
    """Devolve a categoria do participante, ou "Idade invalida"."""
    # TODO: rejeite idade <= 0 primeiro, depois classifique nas tres faixas.
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert categoria(10) == "Infantil"
assert categoria(12) == "Infantil"
assert categoria(13) == "Juvenil"
assert categoria(17) == "Juvenil"
assert categoria(18) == "Adulto"
assert categoria(70) == "Adulto"
assert categoria(0) == "Idade invalida"
assert categoria(-5) == "Idade invalida"
print("Exercício 03: todos os testes passaram!")
