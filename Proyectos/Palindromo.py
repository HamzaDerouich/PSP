def Factorial(a):
    if a == 1:
        return 1
    else :
        return a * Factorial(a-1)

factor = Factorial(5)
print(f"El factorial  es: {factor}") 