def pode_entrar(idade, altura):
    """Devolve True quando a pessoa atende às duas exigências."""
    # TODO: junte as duas condicoes com and.
    pass


# --------------------------------------------------------------------
# Testes — não altere daqui para baixo.
# Rode o programa: se aparecer a mensagem de sucesso no fim, está certo.
# --------------------------------------------------------------------
assert pode_entrar(14, 1.62) == True
assert pode_entrar(12, 1.50) == True
assert pode_entrar(14, 1.45) == False
assert pode_entrar(10, 1.70) == False
assert pode_entrar(11, 1.49) == False
assert pode_entrar(30, 1.40) == False
print("Exercício 04: todos os testes passaram!")
