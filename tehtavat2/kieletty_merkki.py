def laske(merkkijono, kielletty_merkki):
    laskuri = 0
    osajono = ""
    for kirjain in merkkijono:
        if kirjain != kielletty_merkki:
            osajono += kirjain
        else:
            pituus = len(osajono)
            laskuri += summa(pituus)
            osajono = ""

    pituus = len(osajono)
    laskuri += summa(pituus)    

    return laskuri

def summa(n):
    tulos = int(n*(n + 1)/2)
    return tulos


if __name__ == "__main__":
    testi = laske("aaabaac", "b")
    print(testi)