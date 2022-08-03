# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#       Para homens: (72.7*h) - 58
#       Para mulheres: (62.1*h) - 44.7 

print("Calculo de peso ideal!")

h = float(input("Informe a sua altura: "))
AlturaGenero = str(input("Informe o seu sexo: "))

if AlturaGenero == 'masculino':
    PesoIdeal = (72.7*h) - 58;
    print(f'Seu peso ideal deve ser {PesoIdeal:.2f}')
elif AlturaGenero == "feminino":
    PesoIdeal = (62.1*h) - 44.7;
    print(f'Seu peso ideal deve ser {PesoIdeal:.2f}')
