# zad 14; sum square.py

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums

def sumList(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total

def main():
    file1 = open('liczbyLista.txt', 'r')
    liczby = file1.readlines()

    file2 = open('liczbyListaResult.txt', 'w')
    
    result = sumList(squareEach(toNumbers(liczby)))
    print(result, file = file2)

    file1.close()
    file2.close()
    

main()
