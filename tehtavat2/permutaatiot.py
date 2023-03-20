def permutaatiot(lista1, lista2):
    # erotukset: []
    laskuri = 0
    indexList = []
    for i in range(len(lista1)):
        indexList.append([-1,-1])

    for j in range(len(lista1)):
        indexList[lista1[j]-1][0] = j
        indexList[lista2[j]-1][1] = j
    
    for item in indexList:
        erotus = item[0] - item[1]
        if erotus<0:
            laskuri += 1

    return laskuri

if __name__ == "__main__":
    # testi = permutaatiot([1,2,3,4,5],[5,4,3,2,1])
    # print(testi)

    # testi2 = permutaatiot([1,2,3,4],[1,2,4,3])
    # print(testi2)

    testi3 = permutaatiot([1,3,5,2,4],[2,4,1,3,5])
    print(testi3)