#variável
tipoCarro = ""
capacidade = 0
valorCombustivel = 0.0
preco = 0.0

#programa
tipoCarro = input("Informe o tipo do Carro: G - Gasolina e A - Álcool' ")
capacidade = int(input("Informe a capacidade do tanque: "))

if(tipoCarro.upper() == "G"):
    tipoCarro = "Gasolina"
    print("Você escolheu um carro do tipo Gasolina")  
else:
    tipoCarro = "Álcool"
    print("Você escolheu um carro do tipo Álcool")
    
valorCombustivel = float(input("Informe o valor do litro: "))
preco = (valorCombustivel * capacidade)
print(f"O valor para encher o tanque com {tipoCarro} é: R${preco:,.2f}")