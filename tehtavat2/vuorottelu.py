import math

def vuorottelu(lista):
    pituusLista = len(lista)

    aloitus = 0
    joukkojenAlut = []
    joukkojenAlut.append(aloitus)
    aloitus = 1
    edellinenErotus = 0
    for i in range(1, pituusLista):
        nykyErotus = int(math.copysign(1, lista[i] - lista[i-1]))
        if i == 1:
            edellinenErotus = nykyErotus
        elif nykyErotus == edellinenErotus:
            joukkojenAlut.append(aloitus)
            aloitus = i
    
    # print(joukkojenAlut)

    valiPituudet = []
    for j in range(1,len(joukkojenAlut)):
        pituus = joukkojenAlut[j] - joukkojenAlut[j-1] + 1
        valiPituudet.append(pituus)


    viimeinenPituus = pituusLista - joukkojenAlut[-1]
    valiPituudet.append(viimeinenPituus)
    print(valiPituudet)

    tulos = 0

    for vali in valiPituudet:
        tulos += int(vali*(vali + 1)/2)

    print(tulos)




if __name__ == "__main__":
    testi = vuorottelu([1,2,3,4])
    # print(testi)

    testi2 = vuorottelu([1,2,4,3])
    # print(testi2)