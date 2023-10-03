# toList.py

def toList(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

def main():

    lista = ['1', '2', '3', '4', '5', '6', '7']

    inLista = toList(lista)
    
    print(inLista)
    print(type(inLista[1]))
    
main()
