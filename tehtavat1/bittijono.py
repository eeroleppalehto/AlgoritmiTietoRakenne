def create(n, k):
    binaryNumber = []
    for i in range(0, n):
        binaryNumber.append("0")
    
    for i in range(0, k): # while???
        for j in range(0, len(binaryNumber)):
            if binaryNumber[j] == "0":
                binaryNumber[j] = "1"
                break
            elif binaryNumber[j] == "1":
                binaryNumber[j] = "0"
    # Generate string to be returned           
    binaryString = ""
    for binary in binaryNumber:
        binaryString += binary
    return binaryString

if __name__ == "__main__":
    print(create(5, 0)) # 00000
    print(create(5, 1)) # 10000
    print(create(5, 2)) # 01000
    print(create(5, 3)) # 11000
    print(create(5, 4)) # 00100
    print(create(5, 31)) # 11111