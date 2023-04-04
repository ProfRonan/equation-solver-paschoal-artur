import math
#Receiving information from user
Dg = int(input("Informe o grau da equação: \n"))

#Operating with the information
if Dg > 2 or Dg < 1 :
    print("Grau inválido\n")

if Dg == 1 :
    print("A equação é do primeiro grau\n")
    a_user = int(input("Informe um valor para o 'a' da equação: \n"))
    if a_user == 0:
        print("Valor de a inválido\n")

    if a_user != 0 :
        b_user = int(input("Informe um valor para o 'b' da equação : \n"))
        operation = int((-b_user)/a_user)
        print(f"{operation: .2f}")

if Dg == 2 :
    print("A equação é do segundo grau\n")
    a_user2 = int(input("Informe um valor para o 'a' da equação: \n"))
    if a_user2 == 0:
        print("Valor de a inválido\n")

    if a_user2 != 0 :
        b_user2 = int(input("Informe um valor para o 'b' da equação : \n"))
        c_user2 = int(input("Informe um valor para o 'c' da equação : \n"))
        delta_eq = int((b_user2**2) - (4 * a_user2 * c_user2))
        if delta_eq < 0 :
            print("A equação não possui raízes reais")

        if delta_eq == 0 :
            print("A equação possui apenas uma raiz real")
            root_1 = int(-b_user2 / 2 * a_user2)
            print(f"{root_1: .2f}\n")

        if delta_eq > 0 :
            print("A equação possui duas raízes reais")
            root_positive = int((-b_user2 + math.sqrt(delta_eq)) / 2 * a_user2)
            root_negative = int((-b_user2 - math.sqrt(delta_eq)) / 2 * a_user2)
            print(f"{root_negative: .2f}")
            print(f"{root_positive: .2f}\n")