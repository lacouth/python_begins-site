def conta_energia(kwh):
    """Devolve o valor da conta de luz, arredondado para duas casas."""
    # TODO: escolha a tarifa (0.45 ate 150 kWh, 0.72 acima) e devolva o total.
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert conta_energia(150) == 67.5
assert conta_energia(151) == 108.72
assert conta_energia(100) == 45.0
assert conta_energia(0) == 0
assert conta_energia(320) == 230.4
print("Exercício 04: todos os testes passaram!")
