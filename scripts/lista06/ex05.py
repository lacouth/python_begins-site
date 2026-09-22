def qualidade_sinal(percentual):
    """Devolve "Otimo", "Bom", "Fraco" ou "Sem sinal"."""
    # TODO: escada de elif com >=, da maior faixa para a menor.
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert qualidade_sinal(100) == "Otimo"
assert qualidade_sinal(75) == "Otimo"
assert qualidade_sinal(74) == "Bom"
assert qualidade_sinal(50) == "Bom"
assert qualidade_sinal(49) == "Fraco"
assert qualidade_sinal(25) == "Fraco"
assert qualidade_sinal(24) == "Sem sinal"
assert qualidade_sinal(0) == "Sem sinal"
print("Exercício 05: todos os testes passaram!")
