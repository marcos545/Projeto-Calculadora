from time import sleep

print(40*"*")
print("boas vibdas ao meu primeiro projeto!! ")
print(40*"*")

nome = input("digite seu nome:   ")
print("iniciando calculadora...")
sleep(3)

print(f"calculadora iniciada e ai {nome} bora começar? ")

continua = "s"
while(continua =="s"):
      num1 = float(input("digite o primeiro numero:  "))
      op = input("digite a operaçao (+, -, *, /):  ")
      num2 = float(input("digite o segundo numero: "))
      if(op == "+"):
        resultado = num1 + num2
      elif(op =="-"):
        resultado = num1 - num2
      elif(op =="*"):
        resultado = num1 * num2
      elif(op == "/"):
        resultado = num1 / num2
else:
    resultado = 0
    print(f"resultado: {resultado} ")

continua = input("deseja continuar? (s/n): ")
print("programa finalizado!!! ")

