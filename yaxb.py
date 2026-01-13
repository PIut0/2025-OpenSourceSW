def yaxb(a, b, x):
    for i in range(X+1):
        print(f"{a}x{a}x{i} + {b} = {a*a*i + b}")

a = int(input("a: "))
b = int(input("b: "))
X = int(input("Max: "))

yaxb(a, b, X)