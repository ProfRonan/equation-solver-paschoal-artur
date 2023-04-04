#Receiving information from user
Dg = int(input("Informe o grau da equação: "))

#Operating with the information
if Dg > 2 or Dg < 1 :
    print("Grau inválido")

if Dg == 1 :
    print("A equação é do primeiro grau")
    auser = int(input("Informe um valor para o 'a' da equação: "))
    if auser == 0:
        print("Valor de a inválido")

    if auser != 0 :
        buser = int(input("Informe um valor para o 'b' da equação : "))
        operation = int((-buser)/auser)
        print(f"{operation: .2f}")

if Dg == 2 :
    print("A equação é do segundo grau")
    auser2 = int(input("Informe um valor para o 'a' da equação: "))
    if auser2 == 0:
        print("Valor de a inválido")

    if auser2 != 0 :
        buser2 = int(input("Informe um valor para o 'b' da equação : "))
        cuser2 = int(input("Informe um valor para o 'c' da equação : "))
        delta = int((buser2**2) - 4 * (auser2 * cuser2))
    if delta < 0 :
        print("A equação não possui raízes reais")

    if delta == 0 :
        print("A equação possui apenas uma raiz real")
        root_1 = int(-buser2 / 2 * auser2)
        print(f"{root_1: .2f}")

    if delta > 0 :
        print("A equação possui duas raízes reais")
        root_positive = -(buser2) + (delta **(1/2)) / 2 * auser2
        root_negative = -(buser2) - (delta **(1/2)) / 2 * auser2
        print(f"{root_negative: .2f}")
        print(f"{root_positive: .2f}")