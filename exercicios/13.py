PesoPescado = float(input('Informe o peso dos peixes: '))
if PesoPescado > 50:
    Multa = 4 * PesoPescado;
    print(f'Você ultrapassou o peso limite permitido e deve pagar {Multa} de multa.')
elif PesoPescado < 50:
    print(f"O peso pescado está dentro do limite permitido.")
