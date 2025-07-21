""" 
Teste 1:
5
101 Carro
102 Viagem
103 Celular
104 Notebook
105 Relógio
3
3 5 2

Saída esperada: 103-Celular 102-Viagem 104-Notebook

Teste 2:
8
201 TV
202 Bicicleta
203 Moto
204 Tablet
205 Headphone
206 Smartwatch
207 TV
208 Bicicleta
4
12 14 14 16

Saída esperada: 204-Tablet 202-Bicicleta 208-Bicicleta 207-TV

Teste 3:
6
301 Computador
302 Impressora
303 Teclado
304 Mouse
305 Teclado
306 Teclado
2
1 3

Saída esperada: 301-Computador 304-Mouse
"""

n = int(input())

premios = []
for i in range(n):
    id, nome = input(f'{i}. ID Nome: ').split()
    premios.append({'id': int(id), 'nome': nome})

k = int(input())
forcas = list(map(int, input().split()))

if k > n:
    print('Não foi possível realizar o sorteio.')
else:
    sorteados = set()
    p = -1
    for f in forcas:
        while True:
            p = (p+f) % n
            pId = premios[p]['id']
            if pId not in sorteados:
                sorteados.add(pId)
                print(f'{pId}-{premios[p]['nome']}', end=' ')
                break
            elif f > 1:
                f -= 1
            else:
                while premios[p]['id'] in sorteados:
                    p = (p+1)%n
                sorteados.add(pId)
                print(f'{pId} {premios[p]['nome']}', end=' ')
                break