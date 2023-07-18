# Hyperoperations Calculator, Version 1.0

# based on Goodstein's notation for hyperoperations
# G(n, a, b) = x
# n = degree, a = first operand, b = second operand, x = product

def Hypop(n, a, b):
    # "common" degrees as initial conditions (succession, addition, multiplication, exponentiation)
    if n == 1:
        x = a + b
    elif n == 2:
        x = a * b
    elif n == 3:
        x = a ** b
    else:
        x = a
        for i in range(b-1):
            x = Hypop(n-1, x, a)
    
    return x

if __name__ == "__main__":
    print("Hyperoperation Calculator")
    print("Details and instructions can be found in the README file")
    runagain = "Y"
    while runagain == "Y":
        deg = int(input("Please input the integer corresponding to the degree of your calculation (n): "))
        op1 = int(input("Please input your first operand (a): "))
        op2 = int(input("Please input your second operand (b): "))
        print(Hypop(deg, op1, op2))
        runagain = input("Would you like to calculate a new value? (Y/N): ").upper()


    # test examples
    # print(Hypop(1, 2, 4))
    # print(Hypop(2, 3, 3))
    # print(Hypop(3, 2, 3))
    # print(Hypop(4, 2, 3))
    # print(Hypop(4, 3, 4))