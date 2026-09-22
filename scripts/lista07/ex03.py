def dias_ate_acabar(franquia_gb, consumo_diario_gb):
    """Dias completos que a franquia aguenta com esse consumo diario."""
    # TODO: acumulador do que ja foi usado e contador de dias, ANTES do laco
    # TODO: continue enquanto couber MAIS UM dia dentro da franquia
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert dias_ate_acabar(20, 1.4) == 14
assert dias_ate_acabar(10, 2) == 5
assert dias_ate_acabar(10, 3) == 3
assert dias_ate_acabar(5, 10) == 0
assert dias_ate_acabar(50, 0.5) == 100
print("Exercício 03: todos os testes passaram!")
