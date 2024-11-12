n = int(input("Digite um número: "))

x1 = 5 * n**2 + 4
x2 = 5 * n**2 - 4
s1 = int(x1 ** 0.5)
s2 = int(x2 ** 0.5)

if s1 * s1 == x1 or s2 * s2 == x2:
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")
