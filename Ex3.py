#variáveis
amostra = 0.0

#programa
amostra = float(input("Informe a quantidade de pontos de água da amostra: "))

if(amostra <= 10):
    print("Classificação do solo: Rochoso")
elif((amostra > 10) and (amostra <= 40)):
    print("Classificação do solo: Firme")
elif((amostra > 40) and (amostra <= 80)):
    print("Classificação do solo: Pantanosa")
else:
    print("Quantidade inválida!")