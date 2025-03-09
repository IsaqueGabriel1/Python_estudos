
opc = "soma, digite 1 \nsubtrair, digite 2 \nmultiplicar, digite 3 \ndividir, digite 4"
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
calc = input('\n{}\nO que você deseja calcular? \nopções:\n{}\nresp:'.format('--------------------------------',opc))

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2


if calc == "1":
    print(soma(num1, num2))
else:
    if calc == "2":
        print(sub(num1, num2))
    else:
        if calc == "3":
            print(mult(num1, num2))
        else:
            if calc == "4":
                print(div(num1, num2))
            else:
                print("Opção invalida!!!")
            




#print("Soma é = {}".format(soma(num1,num2)))
#print("Sub é = {}".format(sub(num1,num2)))
#print("mult = {}".format(mult(num1,num2)))
#print("div = {}".format(div(num1,num2)))
