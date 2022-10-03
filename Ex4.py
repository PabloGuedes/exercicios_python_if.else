#variáveis
nome = ""
idade = 0
categoria = ""

#programa
nome = input("Informe o nome do nadador: ")
idade = int(input("Informe a idade do nadador: "))

if((idade >= 5) and (idade <= 7)):
    categoria = "Infantil A"
elif((idade >= 8) and (idade <= 11)):
    categoria = "Infantil B"
elif((idade >= 12) and (idade <= 13)):
    categoria = "Juvenil A"
elif((idade >= 14) and (idade <= 17)):
    categoria = "Juvenil B"
elif(idade >= 18):
    categoria = "Adulto"
else:
    print("Categoria inválida!")
     
print("")
print(f"O nome do nadador é: {nome}.")
print(f"A idade do nadador é: {idade}.")
print(f"A categoria do nadador é: {categoria}.")