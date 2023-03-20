def tira_osajonot(merkkijono):
    # t_id = []
    # i_id = []
    # r_id = []
    # a_id = []

    # for i, kirjain in enumerate(merkkijono):
    #     if kirjain == 't':
    #         t_id.append(i)
    #     elif kirjain == 'i':
    #         i_id.append(i)
    #     elif kirjain == 'r':
    #         r_id.append(i)
    #     elif kirjain == 'a':
    #         a_id.append(i)


    # tirat = []
    # tira = []
    # for t in t_id:
    #     (temp:= []).append(t)
        


    # return t_id + ['/'] + i_id + ['/'] + r_id + ['/'] + a_id
    tira = [-1,-1,-1,-1]
    tulosjoukko = []
    tira_found = -1 in tira

    for i, kirjain in enumerate(merkkijono):
        if kirjain=='t':
            tira_found = -1 in tira
            
            if tira[1] != -1 and tira[0] :
                tira[0] = i
            

            if not tira_found:
                tulosjoukko.append(tira)
        elif kirjain=='i':
            tira[1] = i
            tira_found = -1 in tira
            if not tira_found:
                tulosjoukko.append(tira)
        elif kirjain=='r':
            tira[2] = i
            tira_found = -1 in tira
            if not tira_found:
                tulosjoukko.append(tira)
        elif kirjain=='a':
            tira[3] = i
            tira_found = -1 in tira
            if not tira_found:
                tulosjoukko.append(tira)

    return tulosjoukko
    


if __name__ == "__main__":
    testi = tira_osajonot("-tt-ii-t-r-a")
    print(testi)