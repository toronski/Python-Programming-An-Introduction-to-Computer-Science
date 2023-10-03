# Metoda Newtona

import math

def main():

    x = eval(input("Podaj liczbę, której kwadrat chcesz zgadnąć: "))
    improve_times = eval(input("O ile chcesz zwiększyć prawdopodobieństwo dobrej odpowiedzi: "))
    guess = x/2 

    for i in range(1, improve_times+1):
        guess = (guess + (x/guess)) / 2

    sub = math.sqrt(x) - guess
    sub = abs(sub)
    
    print("Oszacowana liczba to: ", round(guess, 3))
    print("Nasze przypuszczenie różni się o ", round(sub, 3), "od pierwiastka liczby.")

main()
