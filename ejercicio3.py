def conversionDeNumero(n, base):
    while decimal > 0:
        residuo = n % base
        suma += residuo   
        decimal = int(decimal / 16)
    return suma
n=int(input("ingrese un número: "))
base= int(input("A qué base quiere ingresar"))
print(conversionDeNumero(n,base))