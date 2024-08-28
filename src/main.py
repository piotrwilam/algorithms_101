from .karatsuba import karatsuba

if __name__ == "__main__":
    number1 = int(input("Enter the first number for the multiplication: "))
    number2 = int(input("Enter the second number for the multiplication: "))
    print (karatsuba (number1, number2))