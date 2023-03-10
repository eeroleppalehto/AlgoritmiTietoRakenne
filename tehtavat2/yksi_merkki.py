def yksi_merkki(merkkijono):
    laskuri = 0
    osajono = merkkijono[0]
    osajonot = []
    for i, kirjain in enumerate(merkkijono):
        if i == 0:
            continue
        elif kirjain == osajono[len(osajono)-1]:
            osajono += kirjain
        else:
            osajonot.append(osajono)
            osajono = kirjain
    
    osajonot.append(osajono)

    for item in osajonot:
        pituus = len(item)
        laskuri += int(pituus*(pituus + 1)/2)

    return laskuri

if __name__ == "__main__":
    testi = yksi_merkki("aaabaa")
    print(testi)