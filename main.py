#Receiving information from user
Dg = int(input("Informe o grau da equação: \n"))

#Operating with the information
if Dg > 2 or Dg < 1 :
    print("Grau inválido\n")

if Dg == 1 :
    print("A equação é do primeiro grau\n")
    auser = int(input("Informe um valor para o 'a' da equação: \n"))
    if auser == 0:
        print("Valor de a inválido\n")

    if auser != 0 :
        buser = int(input("Informe um valor para o 'b' da equação : \n"))
        operation = int((-buser)/auser)
        print(f"{operation: .2f}")

if Dg == 2 :
    print("A equação é do segundo grau\n")
    auser2 = int(input("Informe um valor para o 'a' da equação: \n"))
    if auser2 == 0:
        print("Valor de a inválido\n")

    if auser2 != 0 :
        buser2 = int(input("Informe um valor para o 'b' da equação : \n"))
        cuser2 = int(input("Informe um valor para o 'c' da equação : \n"))
        delta_eq = int((buser2**2) - 4 * (auser2 * cuser2))
        if delta_eq < 0 :
            print("A equação não possui raízes reais\n")

        if delta_eq == 0 :
            print("A equação possui apenas uma raiz real\n")
            root_1 = int(-buser2 / 2 * auser2)
            print(f"{root_1: .2f}\n")

        if delta_eq > 0 :
            print("A equação possui duas raízes reais\n")
            root_positive = int(-(buser2) + (delta_eq **(1/2)) / 2 * auser2)
            root_negative = int(-(buser2) - (delta_eq **(1/2)) / 2 * auser2)
            print(f"{root_negative: .2f}\n")
            print(f"{root_positive: .2f}\n")