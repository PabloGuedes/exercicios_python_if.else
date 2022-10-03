#variáveis
salario_minimo = 0.0
num_horas_trabalhadas = 0.0
num_dependentes = 0.0
num_horas_extras = 0.0
valor_hora = 0.0
salario_mes = 0.0
valor_dependentes = 0.0
hora_extra = 0.0
salario_bruto = 0.0
salario_liquido = 0.0

#programa
salario_minimo = float(input("Informe o valor do salário mínimo: "))
num_horas_trabalhadas = float(input("Informe o número de horas inteiras trabalhadas: "))
num_dependentes = float(input("Informe o número de dependentes do funcionário: "))
num_horas_extras = float(input("Informe a quantidade de horas extras inteiras trabalhadas: "))

valor_hora = salario_minimo * 0.20
salario_mes = num_horas_trabalhadas * valor_hora
valor_dependentes = num_dependentes * 32
hora_extra = num_horas_extras * (valor_hora * 1.5)
salario_bruto = salario_mes + hora_extra + valor_dependentes

if(salario_bruto < 200):
    salario_liquido = salario_bruto
else:
    if((salario_bruto > 200) and (salario_bruto < 500)):
        salario_liquido = salario_bruto * 0.9
    else:
        salario_liquido = salario_bruto * 0.8

if(salario_liquido < 350):
    salario_liquido = salario_liquido + 100.00
else:
    salario_liquido = salario_liquido + 50.00

print(f"O salário a receber do funcionário é igual a: R${salario_liquido:,.2f}")