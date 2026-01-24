def celsiusToFahrenheit(C):
    return (C * 9/5) + 32

C = float(input("Enter the temperature in Celsius : "))

print(f"The temperature in Fahrenheit is : {celsiusToFahrenheit(C)}")