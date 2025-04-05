try:
    r = float(input("Please enter the radius of the circle: "))
    
    if r <= 0:
        print(" It is an invalid input. Radius must be greater than 0.")
    else:
        c = 2 * (22/7) * r
        print(" The circumference is:", c)

except ValueError:
    print("Invalid input. Please enter a numeric value.")
