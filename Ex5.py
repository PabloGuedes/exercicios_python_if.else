#variáveis
salario = 0.0
novo_salario = 0.0
bonificacao = 0.0
auxilio_escola = 0.0

#programa
salario = float(input("Informe o salário: "))

if(salario <= 500):
    bonificacao = salario * 0.5
elif((salario > 500) and (salario <= 1200)):
    bonificacao = salario * 0.12
elif(salario > 1200):
    bonificacao = salario

if(salario <= 600):
    auxilio_escola = 150
elif(salario > 600):
    auxilio_escola = 100

novo_salario = salario + bonificacao + auxilio_escola

print(f"O novo salário desse funcionário é: R${novo_salario}")