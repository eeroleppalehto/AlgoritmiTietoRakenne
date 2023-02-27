def find(s):
    tekijat = [1]
    for i in range(2,len(s)+1):
        if len(s)%i == 0:
            tekijat.append(i)
    
    for tekija in tekijat:
        x = slice(tekija)
        tempString = s[x]
        while len(tempString)<len(s):
            tempString += s[x]
        if tempString == s:
            return tekija

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7