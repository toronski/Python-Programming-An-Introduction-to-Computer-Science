# funkcje Metoda Newtona

import math

def nextGuess(guess, x):
    return (guess + x / guess) / 2
      
def main():

    num = eval(input("Enter the number whose square you want to guess: "))
    times = eval(input("How much you want to increase the probability of a good answer: "))

    sq_root = num / 2
    for i in range(times):
        sq_root = nextGuess(sq_root, num)

    error = abs(math.sqrt(num) - sq_root)
    
    print("The estimated number is: ", sq_root)
    print("Our guess differs by ", error, " from the square root of the number.")

main()
