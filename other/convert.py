# ZADANKA

"""
print("Witaj. \nPrzed tobą prosty program do zamiany stopni Celsiusa na Fahrenheita.")
def main():
    for i in range(0, 101, 10):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print(str(celsius) + " - " + str(fahrenheit))

main()
"""

def main():
    for i in range(0, 101, 10):
        fahrenheit = 9/5 * i + 32
        print(i, int(fahrenheit))

main()
