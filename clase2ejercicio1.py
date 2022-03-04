
from library import *




def main():
    bono = 50000
    salario_minimo = 1000000
    sub_alim = 120000
    sub_transp = 80000
    nombre = input("digite su nombre ==>         ")
    salario = int(input("digite salario mensual ==>"))
    dias = int(input("digite dias laborados ==> "))
    sueldopagar = calcularsueldo(salario, dias)
    print(f"mi nombre es: {nombre} y  mi salario es : {sueldopagar}  ")
    if salario < (salario_minimo * 2 ):
        sueldopagar = sueldopagar + sub_alim + sub_transp
    else: sueldopagar = sueldopagar+ bono

if __name__ == "__main__":
    main()