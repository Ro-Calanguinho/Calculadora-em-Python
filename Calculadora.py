#Boas vindas
import time
import math
from functools import reduce
while True:
    print("Ola, bem vindo(a/e) a calculadora em python \n")

    #Tipo de operação
    print("Escolha seu tipo de operação: \n")
    
    print("Conta Simples         | 1")
    print("Algebra               | 2")
    print("Trigonometria         | 3")
    print("Convrsão de Unidade   | 4")
    print("Estátistica Básica    | 5")
    print("Funções Avançadas     | 6 ")
    print("Encerar programa      | 0 \n")

    #Declara o tipo de operação
    T_Operação = input ("Digite o número da operação: ")
    print() #Espaço
#________________________________________________________________________________________________________________________________

    #Fechar programa
    if T_Operação == "0": 
        print("Fechando programa...")
        break
#________________________________________________________________________________________________________________________________

    #Tipos de conta simples
    elif T_Operação == "1":
        print("Você escolheu conta simples")
        print("Escolha sua operação: \n")

        print("Adição (+)            | + ou 1")
        print("Subtração (-)         | - ou 2")
        print("Multiplicação (x)     | x, *, . ou 3")
        print("Divisão (/)           | /, ÷ ou 4")
        print("Potenciação (Xʸ)      | ^, P, p ou 5")
        print("Raízes (√)            | R, r ou 6")
        print("Fatorial (!)          | !, F, f ou 7")
        print("Voltar ao inicio      | 0 \n")
        
        #Declara o tipo de conta Simples
        while True:
            Op_Simples = input ("Digite a operação: ")
            print() #Espaço
            
#________________________________________________________________________________________________________________________________

            #Voltar pro menu
            if Op_Simples == "0":
                break
            
#________________________________________________________________________________________________________________________________
            
            #Soma
            elif Op_Simples in ["1", "+"]:
                print("Você escolheu adição \n")
                Quant = int(input("Quantos numeros vôce quer somar? "))
                numX = []
                for i in range(Quant):
                    num = float(input(f"Digite o {i + 1}° número: "))
                    numX.append(num)
                print() #Espaço 
                
                Result = sum(numX)
                Res = " + ".join(map(str, numX))
            
                print("Calculando", end="")
                for _ in range(3):
                    time.sleep(0.75)
                    print(".", end="", flush=True)
                print(f"\nO resultado de {Res} é:", Result)
                print() #Espaço
            
#________________________________________________________________________________________________________________________________
            
            #Subtração    
            elif Op_Simples in ["2", "-"]:
                print("Você escolheu subtração")
                Quant = int(input("Quantos numeros vôce quer subtrair? "))
                numX = []
                for i in range(Quant):
                    num = float(input(f"Digite o {i + 1}° número: "))
                    numX.append(num)
                print() #Espaço 
                
                Result = numX[0]
                for num in numX[1:]:
                    Result -= num
                Res = " - ".join(map(str, numX))
            
                print("Calculando", end="")
                for _ in range(3):
                    time.sleep(0.75)
                    print(".", end="", flush=True)
                print(f"\nO resultado de {Res} é:", Result)
                print() #Espaço
                
#________________________________________________________________________________________________________________________________

            #Multiplicação
            elif Op_Simples in ["3", "x", "*"]:
                print("Você escolheu multiplicação")
                Quant = int(input("Quantos numeros vôce quer multiplicar? "))
                numX = []
                for i in range(Quant):
                    num = float(input(f"Digite o {i + 1}° número: "))
                    numX.append(num)
                print() #Espaço 
                
                Result = math.prod(numX)
                Res = " x ".join(map(str, numX))
            
                print("Calculando", end="")
                for _ in range(3):
                    time.sleep(0.75)
                    print(".", end="", flush=True)
                print(f"\nO resultado de {Res} é:", Result)
                print() #Espaço
                
#________________________________________________________________________________________________________________________________

            #Divisão
            elif Op_Simples in ["4", "/", "÷"]:
                print("Você escolheu divisão")
                Quant = int(input("Quantos numeros vôce quer dividir? "))
                numX = []
                for i in range(Quant):
                    num = float(input(f"Digite o {i + 1}° número: "))
                    numX.append(num)
                print() #Espaço 
                
                Result = numX[0]
                for num in numX[1:]:
                    Result /= num
                Res = " / ".join(map(str, numX))
            
                print("Calculando", end="")
                for _ in range(3):
                    time.sleep(0.75)
                    print(".", end="", flush=True)
                print(f"\nO resultado de {Res} é:", Result)
                print() #Espaço
#________________________________________________________________________________________________________________________________

            #Potenciação
            elif Op_Simples in ["5", "P", "p", "^"]:
                print("Você escolheu potenciação")
                Num = int(input("Qual é a base? "))
                Pot = int(input("Qual é o expoente? "))
                
                print() #Espaço 
                
                Result = pow(Num, Pot)
            
                print("Calculando", end="")
                for _ in range(3):
                    time.sleep(0.75)
                    print(".", end="", flush=True)
                print(f"\nO resultado de", Num, "^", Pot, "é:", Result)
                print() #Espaço
                
#________________________________________________________________________________________________________________________________

            #Raízes
            elif Op_Simples in ["6", "R", "r"]:
                print("Você escolheu raízes")
                Num = int(input("Qual é a base? "))
                Raz = int(input("Qual é a raiz? "))
                
                print() #Espaço 
                
                Result = Num ** (1/Raz)
            
                print("Calculando", end="")
                for _ in range(3):
                    time.sleep(0.75)
                    print(".", end="", flush=True)
                print(f"\nO resultado de {Num} a {Raz}° é:", Result)
                print() #Espaço
                
#________________________________________________________________________________________________________________________________

            #Fatorial
            elif Op_Simples in ["7", "!", "f"]:
                print("Você escolheu fatorial")
                Num = int(input("Qual é o número? "))
                
                print() #Espaço 
                
                Result = math.factorial(Num)
            
                print("Calculando", end="")
                for _ in range(3):
                    time.sleep(0.75)
                    print(".", end="", flush=True)
                print(f"\nO resultado de {Num}! é:", Result)
                print() #Espaço
         
#________________________________________________________________________________________________________________________________

       
            else:
                print("Valor invalido, tente ver a tabela com mais atenção")
#________________________________________________________________________________________________________________________________
               
    #Tipos de contas de algebra
    elif T_Operação == "2":
        print(" \n")
        
#________________________________________________________________________________________________________________________________
               
    #Tipos de Trigonometria 
    elif T_Operação == "3":
        print(" \n")

#________________________________________________________________________________________________________________________________
               
    #Conversão de unidades
    elif T_Operação == "4":
        print("Você escolheu conversão de unidade")
        print("Escolha sua operação: \n")

        print("Temperatura           | 1")
        print("Comprimento           | 2")
        print("Massa/peso            | 3")
        print("Tempo                 | 4")
        print("Velocidade            | 5")
        print("Voltar ao inicio      | 0 \n")
        
        #Declara o tipo de conta Simples
        while True:
            Op_Simples = input ("Digite a operação: ")
            print() #Espaço
    
#________________________________________________________________________________________________________________________________

    #Contas de estatística
    elif T_Operação == "5":
        print(" \n")
    
#________________________________________________________________________________________________________________________________
 
    #Funções Avançadas
    elif T_Operação == "6":
        print(" \n")
    
#________________________________________________________________________________________________________________________________
    
    else:
        print("Valor invalido, tente ver a tabela com mais atenção")