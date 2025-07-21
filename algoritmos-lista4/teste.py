# a = [1, 4, 3]
# b = [2, 5, 2]
# c = [3, 6, 1]
# lista = []
# for i,j,k in zip(a,b,c):
#     lista.append(i)
#     lista.append(j)
#     lista.append(k)
# print(lista)

# m = [
#     [4,2,6],
#     [5,7,1],
#     [3,9,9]
# ]
# print(m[0][1:2])  

sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
# n = len(sudoku)
# quadrados = []
# for i in range(0, n, 3):
#     for j in range(0, n, 3):
#         bloco = []
#         for bi in range(3):
#             for bj in range(3):
#                 bloco.append(sudoku[i+bi][j + bj])
#         quadrados.append(bloco)
# for q in quadrados:
#     print(q)

# blocos = [[num for linha in sudoku[i:i+3] for num in linha[j:j+3]] 
#         for i in range(0, 9, 3)
#         for j in range(0, 9, 3)
#         ]
blocos = []
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        blocos = [k for lin in sudoku[i:i+3] for k in lin[j:j+3]]
