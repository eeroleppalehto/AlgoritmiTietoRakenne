def poistot(merkkijono, k):
    abc_dict = dict( # vai lista?
        a = 0,
        b = 0,
        c = 0
    )

    ehto = True
    laskuri = 0
    while ehto:
        # Try popping from the start of str
        merkkijono[0] 
        # Try popping from the end
        merkkijono[-1]


def apufunktio(dic, k):
    boolList = [False, False, False]

    i = 0
    for key in dic:
        if dic[key] == k:
            boolList[i] = True
        i += 1
    
    if False in boolList:
        return False
    else:
        return True
