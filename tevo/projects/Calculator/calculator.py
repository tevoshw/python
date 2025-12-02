def calculator(*args):
    
    soma_total = 0
    for item in args:
        soma_total += item
    print(f"A soma total é de: {soma_total}")

    media = soma_total / len(args)
    print(f"A média de números é de: {media}")

    maior_numero = max(args)
    menor_numero = min(args)
    print(f"O maior número é de: {maior_numero} e seu menor número é de: {menor_numero}")



calculator(10, 20, 30, 40)