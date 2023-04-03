#Receiving information from user
Dg = int(input("Informe um grau de equação: \n"))

#Operating with the information
if Dg > 2 or Dg < 1 :
    print("Grau inválido")
if Dg == 1 :
    print("A equação é do primeiro grau")
    auser = int(input("Informe um valor para o 'a' da equação: \n"))
    if auser == 0:
        print("Valor de 'a' inválido")
    if auser != 0 :
        buser = int(input("Informe um valor para o 'b' da equação : \n"))
        operation = x = -buser/auser
        operation = int(operation)
        print(f"A raíz da sua equação é {operation}")
        exit()
if Dg == 2 :
    print("A equação é do segundo grau")
    auser = int(input("Informe um valor para o 'a' da equação: \n"))
    if auser == 0:
        print("Valor de a inválido")
if auser != 0 :
    buser = int(input("Informe um valor para o 'b' da equação : \n"))
    cuser = int(input("Informe um valor para o 'c' da equação : \n"))
    delta = int((buser**2) - 4 * auser * cuser)
    if delta < 0 :
        print("A equação não possui raízes reais")
    if delta == 0 :
        print("A equação possui uma raíz real")
    if delta > 0 :
        print("A equação possui duas raízes reais")