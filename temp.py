while True:
    choice = input("Please enter: \n(1) for C to F \n(2) for F to C \n (3) to quit: ")
    if choice == '1':
        c = float(input("Enter the temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C is {f}°F")
        break
    elif choice == '2':
        f = float(input("Enter the temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F is {c}°C")
        break
    elif choice == '3':
        break
    else:
        print("Invalid input. Please try again.")
