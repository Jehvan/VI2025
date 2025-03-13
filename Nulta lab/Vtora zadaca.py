import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

if __name__ == "__main__":
    lista = []
    linija = []
    a = int(input())
    for i in range(a):
        vlez = input()
        lista.append(vlez.split())
    for i in range(a):
        for j in range(a):
            if lista[i][j] == '-':
                lista[i][j] = 0
    for i in range(a):
        for j in range(a):
            if lista[i][j] == "#":
                if i - 1 >= 0:
                    if j - 1 >= 0 and lista[i - 1][j - 1] != '#':
                        lista[i - 1][j - 1] += 1
                    if lista[i - 1][j] != '#':
                        lista[i - 1][j] += 1
                    if j + 1 < a and lista[i - 1][j + 1] != '#':
                        lista[i - 1][j + 1] += 1
                if j - 1 >= 0 and lista[i][j - 1] != '#':
                    lista[i][j - 1] += 1
                if j + 1 < a and lista[i][j + 1] != '#':
                    lista[i][j + 1] += 1
                if i + 1 < a:
                    if j - 1 >= 0 and lista[i + 1][j - 1] != '#':
                        lista[i + 1][j - 1] += 1
                    if lista[i + 1][j] != '#':
                        lista[i + 1][j] += 1
                    if j + 1 < a and lista[i + 1][j + 1] != '#':
                        lista[i + 1][j + 1] += 1

    for i in lista:
        for j in i:
            print(j, end='   ')
        print("")
