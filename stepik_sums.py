def calculate(n):
    sums = []
    i = 0
    while 1:
        i += 1
        if i * 2 < n:
            sums.append(i)
            n -= i
        else:
            sums.append(n)
            break
    print(len(sums))
    print(*sums)


if __name__ == "__main__":
    calculate(int(input()))
