# EX067 - Tabuada v3.0 (minha versao)
while True:
    n = int(input('Tabuada de qual valor? (negativo sai) '))
    if n < 0:
        print('Ate logo!')
        break
    for i in range(1, 11):
        print(f'{n:>2} x {i:>2} = {n * i:>3}')