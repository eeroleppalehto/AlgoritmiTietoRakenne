def count(string):
    # tira = [-1,-1,-1,-1]
    # tulosjoukko = []

    # for i, chara in enumerate(string):

    #     if tira[0] == -1 and chara != 't':
    #         continue
        
    #     elif chara == 't':
    #         if tira[1] == -1:
    #             tira[0] = i
    #     elif chara == 'i':
    #         if tira[2] == -1:
    #             tira[1] = i
    #     elif chara == 'r':
    #         if tira[3] == -1:
    #             tira[2] = i
    #     elif chara == 'a':
    #         tira[3] = i
    #         tulosjoukko.append(tira)
    #         tira = [-1,-1,-1,-1]
    
    # return tulosjoukko


    tila = 0
    tira = [-1,-1,-1,-1]

    for i, kirjain in enumerate(string):
        if tila == 0 and kirjain == 't':
            tira[0] = i
            tila += 1
        elif tila == 1 and kirjain == 'i':
            tira[1] = i
            tila += 1
        elif tila == 2 and kirjain == 'r':
            tira[2] = i
            tila += 1
        elif tila == 3 and kirjain == 'a':
            tira[3] = i
            tila += 1

    pituus = len(string) - (tira[3] - tira[0] + 1)
    print('pituus', pituus)
    osajonot = pituus*(pituus + 1)//2
    print("osajonot", osajonot)

    return osajonot

    # TODO: Looppaa merkkijono ja tallenna t-kirjaimet ja pyri muodostaa 'tira' jokaiselle arvolle. reverse? erilliset ja sisäkkäiset tirat?


if __name__ == "__main__":
    testi = count("--t-ii-r-a--")