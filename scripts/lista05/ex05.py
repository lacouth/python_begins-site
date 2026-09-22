def taxa_excedente(minutos_falados, minutos_franquia):
    """Devolve quanto o cliente paga pelos minutos além da franquia."""
    # TODO: so ha excedente quando os minutos falados passam da franquia.
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert taxa_excedente(137, 100) == 14.8
assert taxa_excedente(90, 100) == 0
assert taxa_excedente(100, 100) == 0
assert taxa_excedente(101, 100) == 0.4
assert taxa_excedente(500, 200) == 120.0
print("Exercício 05: todos os testes passaram!")
