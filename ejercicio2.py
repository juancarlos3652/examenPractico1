
n=int(input("ingrese un número: "))
def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    suma=0
    while decimal > 0:
        residuo = decimal % 16
        suma +=residuo 
        hexadecimal = residuo + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal
print(decimal_a_hexadecimal(n))
