def espera_total(tentativas):
    """Segundos somados de espera, dobrando a cada tentativa (1, 2, 4, 8...)."""
    # TODO: total em 0 e espera em 1, ANTES do for
    # TODO: uma volta por tentativa: some a espera ao total e dobre a espera
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert espera_total(0) == 0
assert espera_total(1) == 1
assert espera_total(2) == 3
assert espera_total(3) == 7
assert espera_total(5) == 31
assert espera_total(10) == 1023
print("Exercício 04: todos os testes passaram!")
