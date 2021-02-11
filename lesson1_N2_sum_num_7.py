i = 1
while i <= 1000:
    if i % 2 != 0:
        number = i ** 3
        k = 1
        sum_dig = 0
        while k <= 1000 ** 3:
            dig = number // k % 10
            sum_dig = sum_dig + dig
            k *= 10
        if sum_dig % 7 == 0:
            print(f"число: {number}, sum: {sum_dig}")
    i += 1



