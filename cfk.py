Temperature = input("Scale? ")


if (Temperature == "celsius"):
    c = float(input("celsius=? "))
    f = ((9*c)/5) + 32
    k = c + 273
    print("Fahrenheit:", f)
    print("Kelvin:", k)

elif (Temperature == "fahrenheit"):
    f = float(input("fahrenheit=? "))
    c = 5*(f-32)/9
    k = ((5*(f-32)/9)+273)
    print("Celsius:", c)
    print("Kelvin:", k)

elif (Temperature == "kelvin"):
    k = float(input("kelvin=? "))
    c = k - 273
    f = ((9*(k-273)/5) + 32)
    print("Celsius:", c)
    print("Fahrenheit:", f)
else:
    print("Invalid input.")
