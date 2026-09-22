def preco_por_minuto(minutos):
    """Devolve o preço por minuto da faixa de consumo."""
    # TODO: escada de if/elif/else com as tres faixas, na ordem certa.
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert preco_por_minuto(0) == 0.20
assert preco_por_minuto(199) == 0.20
assert preco_por_minuto(200) == 0.18
assert preco_por_minuto(399) == 0.18
assert preco_por_minuto(400) == 0.15
assert preco_por_minuto(1000) == 0.15
print("Exercício 02: todos os testes passaram!")
