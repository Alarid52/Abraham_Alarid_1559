from listas import *

def main():
    
    lista = Linked_list()
    print(f"Esta vacía?: {lista.is_empty()}")
    lista.append(10)
    lista.append(20)
    lista.append(30)
    lista.append(40)
    lista.append(50)
    lista.transversal()
    print(lista.get_tail().data)
    lista.prepend(5)
    lista.transversal()
    lista.remove(5)
    lista.transversal()
    lista.pop()
    lista.transversal()
    lista.add_after(40,60)
    lista.transversal()
    lista.add_before(30,90)
    lista.transversal()
    lista.pop()
    lista.transversal()
   
main()