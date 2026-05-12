temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

sala_mais_critica = 0
max_criticos = 0

num_sala = 1
for sala in temperaturas:
    soma = 0
    criticos = 0

    for temp in sala:
        soma += temp
        if temp >= 33:
            criticos += 1

    media = soma / len(temperaturas)
    print(f'Sala: {num_sala}')
    print(media)
    print(criticos)

    if criticos > max_criticos:
        max_criticos = criticos
        sala_mais_critica = num_sala

    num_sala += 1
    print()

print(sala_mais_critica)


















