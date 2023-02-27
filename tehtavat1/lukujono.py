def generate(n):
    # TODO
    # numbers = ["0","1","2","3","4","5","6","7","8","9"]
    numbers = "0123456789"
    items = []
    for i in range (11, 10_000):
        numberString = str(i)
        for number in numbers:
            if numberString.count(number) > 1:
                items.append(i)
                break
    return items[n-1]

if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505