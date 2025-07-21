def max_tesouros(mapa, m, n, p):

    if p % 2 != 0:
        p -= 1
    max_tesouros = 0

    prefix = [[0]*(n+1) for _ in range(m+1)]
    # https://en.wikipedia.org/wiki/Summed-area_table
    # https://blog.demofox.org/2018/04/16/prefix-sums-and-summed-area-tables/
    for i in range(m): # soma todos tesouros de cada submatriz possível -> matriz de prefixo bidimensional
        for j in range(n):
            # I(x,y)=i(x,y)+I(x,y-1)+I(x-1,y)-I(x-1,y-1)
            prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + (1 if mapa[i][j] == 'X' else 0)
            
    # print(prefix)

    for h in range(1, m+1):
        for w in range(1, n+1):

            perimetro = 2*(h + w)
                
            if perimetro > p:
                continue

            for i in range(m-h+1):
                for j in range(n-w+1):
                    x1, y1 = i, j
                    x2, y2 = i+h, j+w
                    tesouros = prefix[x2][y2] - prefix[x2][y1] - prefix[x1][y2] + prefix[x1][y1]
                    if tesouros > max_tesouros:
                        max_tesouros = tesouros
    return max_tesouros

if __name__ == "__main__":
    mn = input().split()
    m, n = int(mn[0]), int(mn[1])
    mapa = []

    for _ in range(m):
        mapa.append(input().split())

    p = int(input())

    print(max_tesouros(mapa, m, n, p))