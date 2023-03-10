def yksi_merkki(merkkijono):
    laskuri = 0
    osajono = ""
    for i, kirjain in enumerate(merkkijono):
        if i == 0:
            osajono = kirjain
        elif kirjain == osajono[len(osajono)-1]:
            osajono += kirjain
        else:
            pituus = len(osajono)
            laskuri += summa(pituus)
            osajono = kirjain

    pituus = len(osajono)
    laskuri += summa(pituus)    

    return laskuri

def summa(n):
    tulos = int(n*(n + 1)/2)
    return tulos

if __name__ == "__main__":
    testi = yksi_merkki("aaabbb")
    print(testi)