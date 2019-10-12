def suma_lista(list):
    tam = len(list)
    if tam == 1:
        return list[0]
    else:
        return list[0] + suma_lista(list[1:])
    
def main():
    print(suma_lista([3,5,2,4]))
main()
