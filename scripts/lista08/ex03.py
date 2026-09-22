def sobra_franquia(franquia_gb, consumo_diario_gb, dias):
    """GB restantes depois de `dias` dias, nunca abaixo de zero."""
    # TODO: comece a sobra valendo a franquia inteira, ANTES do for
    # TODO: uma volta por dia: desconte o consumo e, se ficar negativo, zere
    # TODO: devolva round(sobra, 2)
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert sobra_franquia(20, 1.4, 5) == 13.0
assert sobra_franquia(20, 1.4, 14) == 0.4
assert sobra_franquia(10, 3, 5) == 0
assert sobra_franquia(20, 1.4, 0) == 20
assert sobra_franquia(15, 0.5, 10) == 10.0
print("Exercício 03: todos os testes passaram!")
