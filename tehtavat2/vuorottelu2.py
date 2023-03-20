import math

def vuorottelu(lista):
    tulosJoukko = []
    tulosJoukko.append(lista[0])
    for i in range(1,lista):
        tulosJoukko.append(lista[1])
        nykyErotus = int(math.copysign(1, lista[i] - lista[i-1]))
        tulosJoukko.append((lista[i-1],lista[i]))
        # Do rest

        pass

if __name__ == "__main__":
    pass