
def sumatoriaValores(n,m):
    #caso base
    if m==n:
        suma= 1*m
    else:
        suma= n*(p+1)+ sumatoriaValores(n,m-1)
    return suma
p=int(input('Ingrese un numero: '))
n=int(input('Ingrese otro numero: '))
print(sumatoriaValores(p,n))

