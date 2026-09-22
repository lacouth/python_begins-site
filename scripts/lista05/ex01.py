def passou_da_franquia(usado_gb, franquia_gb):
    """Devolve True quando o consumo ultrapassou a franquia do plano."""
    # TODO: compare o que foi usado com a franquia e devolva True ou False.
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert passou_da_franquia(21.5, 20) == True
assert passou_da_franquia(20, 20) == False
assert passou_da_franquia(19.9, 20) == False
assert passou_da_franquia(0, 20) == False
assert passou_da_franquia(4, 3) == True
print("Exercício 01: todos os testes passaram!")
