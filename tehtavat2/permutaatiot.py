def permutaatiot(lista1, lista2):
    # erotukset: []
    laskuri = 0
    for i in range(len(lista1)):
        erotus = lista1[i]- lista2[i]
        if erotus<0:
            laskuri += 1
    return laskuri

if __name__ == "__main__":
    testi = permutaatiot([1,2,3,4,5],[5,4,3,2,1])
    print(testi)

    testi2 = permutaatiot([1,2,3,4],[1,2,4,3])
    print(testi2)