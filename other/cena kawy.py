# Program liczący łączny koszt zamówienia kawy.

def main():
    print("Obliczę za Ciebie koszt zamówienia na kawę.")

    coffee = eval(input("Ile kilogramów kawy zamawiasz: "))
    coffee_price = coffee * 10.50
    shipping_price = coffee * 0.86
    price_sum = coffee_price + shipping_price +1.50

    print("Łącznie zamówienia kosztować będzie: ", price_sum, "złotych.")

main()
