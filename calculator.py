while True:

    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Power")
    print("8. Comparison")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 9:
        print("Calculator closed.")
        break

    if choice < 1 or choice > 9:
        print("Invalid choice!")
        continue

    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))

    if choice == 1:
        answer = a + b
        print("Answer:", answer)

    elif choice == 2:
        answer = a - b
        print("Answer:", answer)

    elif choice == 3:
        answer = a * b
        print("Answer:", answer)

    elif choice == 4:
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            answer = a / b
            print("Answer:", answer)

    elif choice == 5:
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            answer = a // b
            print("Answer:", answer)

    elif choice == 6:
        if b == 0:
            print("Error: Cannot perform modulus with zero.")
        else:
            answer = a % b
            print("Answer:", answer)

    elif choice == 7:
        answer = a ** b
        print("Answer:", answer)

    elif choice == 8:
        print("\nComparison:")
        print("a > b :", a > b)
        print("a < b :", a < b)
        print("a == b:", a == b)
        print("a != b:", a != b)
        print("a >= b:", a >= b)
        print("a <= b:", a <= b)






       
           


    
    
