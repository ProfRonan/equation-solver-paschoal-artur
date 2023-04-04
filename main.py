#Receiving information from user
Dg = int(input("Informe um grau de equação: \n"))

#Operating with the information
if Dg > 2 or Dg < 1 :
    print("Grau inválido")
    exit()
if Dg == 1 :
    print("A equação é do primeiro grau")
    auser = float(input("Informe um valor para o 'a' da equação: \n"))
    if auser == 0:
        print("Valor de a inválido")
        exit()
    if auser != 0 :
        buser = float(input("Informe um valor para o 'b' da equação : \n"))
        operation = float((-buser)/auser)
        print(f"A raíz da sua equação é {operation: .2f}")
        exit()
if Dg == 2 :
    print("A equação é do segundo grau")
    auser2 = float(input("Informe um valor para o 'a' da equação: \n"))
    if auser2 == 0:
        print("Valor de a inválido")
        exit()
    if auser2 != 0 :
        buser2 = float(input("Informe um valor para o 'b' da equação : \n"))
        cuser2 = float(input("Informe um valor para o 'c' da equação : \n"))
        delta2 = float((buser2**2) - 4 * (auser2 * cuser2))
    if delta2 < 0 :
        print("A equação não possui raízes reais")
        exit()
    if delta2 == 0 :
        print("A equação possui apenas uma raiz real")
        exit()
    if delta2 > 0 :
        print("A equação possui duas raízes reais")