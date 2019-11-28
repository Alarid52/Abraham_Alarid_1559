class NodoArbol:
    def __init__(self, value, izquierdo = None, derecho = None, centro = None ):
        self.data = value
        self.left = izquierdo
        self.right = derecho
        self.middle = centro

def main():
    #Arbol en una linea
    root = NodoArbol('¿Cual es tu ingreso?',NodoArbol('No puedes tener el credito'),NodoArbol('¿Historial en buro de credito (v/r)?',NodoArbol('¿Tienes infonavit(si/no)?',NodoArbol('Si puedes tener el credito'),NodoArbol('¿Cantidad de ahorro?',NodoArbol('No puedes tener el credito'),NodoArbol('¿Cual es tu de edad?',NodoArbol('No puedes tener el credito'),NodoArbol('No puedes tener el credito'),NodoArbol('Si puedes tener el credito')),NodoArbol('Si puedes tener el credito'))),NodoArbol('No puedes tener el credito'),None),NodoArbol('¿Cual es tu edad?',NodoArbol('No puedes tener el credito'),NodoArbol('No puedes tener el credito'),NodoArbol('¿Tienes infonavit(si/no)?',NodoArbol('Si puedes tener el credito'),NodoArbol('No puedes tener el credito'),None)))
    #Comienzo ejecución del programa
    print(root.data)
    rango = int(input(''))
    #Subarbol izquierdo
    if rango < 8000: 
        print(root.left.data)
    #Subarbol central
    elif rango >= 8000 and rango <= 28000:
        print(root.middle.data)
        edad = int(input(''))
        if edad < 24 or edad > 64:
            print(root.middle.left.data)
        elif edad >= 24 and edad <= 44:
            print(root.middle.middle.data)
            infonavit = input('')
            if infonavit == 'si':
                print(root.middle.middle.left.data)
            elif infonavit == 'no':
                print(root.middle.middle.right.data)
            else:
                print('No ingresaste un dato válido, empieza de nuevo')
        else:
            print(root.middle.right.data)
    #Subarbol derecho        
    else:
        print(root.right.data)
        buro = input('')
        if buro == 'v':
            print(root.right.left.data)                 
            infonavit = input('')
            if infonavit == 'si':
                print(root.right.left.left.data)
            elif infonavit == 'no':
                print(root.right.left.right.data)
                ahorro = int(input(''))
                if ahorro < 50000:
                    print(root.right.left.right.left.data)
                elif ahorro >= 50000 and ahorro <= 150000:
                    print(root.right.left.right.middle.data)
                else:
                    print(root.right.left.right.right.data)
                    edad = int(input(''))
                    if edad < 24 or edad > 64:
                        print(root.right.left.right.right.left.data)
                    elif edad >= 24 and edad <= 44:
                        print(root.right.left.right.right.middle.data)
                    else:
                        print(root.right.left.right.right.right.data)
            else:
                print('No ingresaste un dato válido, empieza de nuevo')

        elif buro == 'r':
            print(root.right.right.data)

        else:
            print('No ingresaste un dato válido, empieza de nuevo')
main()