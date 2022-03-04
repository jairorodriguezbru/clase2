# manejo de listas #

from unicodedata import name


def listas():
    lista1 = []
    lista2 = []


#utilizando el ciclo for#
    listaconelementos = [30, 200 , "jairo rodriguez", "ingeniero de sistemas", True, ["decimo semestre"]  ]
    for i in range(len(listaconelementos)):
            print (listaconelementos[i])
    listaconelementos[1]= listaconelementos[1] + 200000

         
         
    
   #   añadir valor a una posicion de la lista 

    listaconelementos.insert (2,["sede riohacha", "guajira"])
    print("adicionar con posicion 2")
    print(listaconelementos)


    #eliminar elementos de posicion x
    del listaconelementos[2]
    print (listaconelementos)


    #utilizando while#

    #print("mostrando con ciclo while")
    #j=0
    #while j < len(listaconelementos):
    # print(listaconelementos[j])
    #j=j+1
    #(listaconelementos[0:3])




 

def main():
    listas()



if __name__ == "__main__":
 main()

