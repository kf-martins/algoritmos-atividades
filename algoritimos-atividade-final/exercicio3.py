def input_influenciadores():
    c = float(input())
    n = int(input())
    influenciadores = []
    while n:
        partes = input().split(',')
        custo = float(partes[0])
        seguidores = set(map(int, partes[1:]))
        influenciadores.append({'custo': custo, 'seguidores': seguidores})
        n -= 1
    return c, influenciadores

def estrategia_ingenua(c, influenciadores: list[dict]):
    contratados = []
    seguidores = set()
    custo_total = 0

    restantes = sorted(influenciadores, key=lambda x: (x['custo']))
    for inf in restantes:
        if custo_total + inf['custo'] <= c:
            contratados.append(inf)
            custo_total += inf['custo']

    for inf in contratados:
        # seguidores.add(inf['seguidores'])
        seguidores.update(inf['seguidores'])

    return custo_total, len(seguidores)

def estrategia_atual(c, influenciadores: list[dict]):
    contratados = []
    custo_total = 0
    seguidores = set()

    restantes = sorted(influenciadores, key=lambda x: (x['custo']/len(x['seguidores'])))
    for inf in restantes:
        if custo_total + inf['custo'] <= c:
            contratados.append(inf)
            custo_total += inf['custo']

    for inf in contratados:
        seguidores.update(inf['seguidores'])

    return custo_total, len(seguidores)

def estrategia_nova(c, influenciadores: list[dict]):
    contratados = []
    custo_total = 0
    seguidores_alcancados = set()
    restantes = influenciadores[:]

    while True:
        melhores = []

        for inf in restantes:
            novos = inf['seguidores'] - seguidores_alcancados
            if novos:
                custo_residual = inf['custo'] / len(novos)
                melhores.append((custo_residual, inf, novos))
        
        if not melhores:
            break

        melhores.sort()
        custo_residual, escolhido, novos = melhores[0]
        if custo_total + escolhido['custo'] > c:
            restantes.remove(escolhido)
            continue
        
        contratados.append(escolhido)
        custo_total += escolhido['custo']
        seguidores_alcancados.update(escolhido['seguidores'])
        restantes.remove(escolhido)

    return custo_total, len(seguidores_alcancados)

if __name__ == "__main__":
    c, influenciadores = input_influenciadores()

    custo1, seg1 = estrategia_ingenua(c, influenciadores)
    custo2, seg2 = estrategia_atual(c, influenciadores)
    custo3, seg3 = estrategia_nova(c, influenciadores)
    
    print(f'Estratégia Ingênua: {custo1:.1f}, {seg1}')
    print(f'Estratégia Atual: {custo2:.1f}, {seg2}')
    print(f'Estratégia Nova: {custo3:.1f}, {seg3}')
