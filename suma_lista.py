def suma_lista(list):
    tam = len(list)
    if tam == 1:
        return list[0]
    else:
        return list[0] + suma_lista(list[1:])
    
def main():
    print(suma_lista([1,2,3,4,5,6,7]))
main()
