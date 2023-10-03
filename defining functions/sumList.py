# sumList.py

def sumList(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

def main():
    lista = [1, 2, 3, 4, 5, 6, 7]

    print(sumList(lista))

main()
