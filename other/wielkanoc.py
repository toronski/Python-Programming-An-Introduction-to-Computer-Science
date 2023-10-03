# Program do obliczania daty wielkanocy na podstawie roku.

def main():
    print("Ten program oblicza dni od ostatniego nowiu do pierwszego stycznia:")
    rok = eval(input("Podaj rok i wciśnic enter: "))
    C = rok // 100
    epact = (8 + (C//4) - C + ((8 * C + 13)//25) + 11 * (rok%19)) % 30

    print("Nów wypada", epact, "dni przed pierwszym stycznia.")

main()
