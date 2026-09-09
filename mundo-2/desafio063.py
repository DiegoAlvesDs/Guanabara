# EX063 - Fibonacci (minha versao com lista)
n = int(input('Quantos termos de Fibonacci? '))
fib = [0, 1]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
print(' -> '.join(str(x) for x in fib[:n]))