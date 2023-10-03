# squareEach.py

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return nums

def main():
    lista = [1, 2, 3, 4, 5, 6, 7]

    print(squareEach(lista))

main()
