# EX077 - Vogais em tupla (minha versao)
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'FUTURO')
for palavra in palavras:
    vogais = [letra.lower() for letra in palavra if letra.lower() in 'aeiou']
    print(f'{palavra:<12} -> {" ".join(vogais)}')