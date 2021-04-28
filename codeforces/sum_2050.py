# https://codeforces.com/contest/1517/problem/A

n = int(input())

for _ in range(n):
    el = int(input())
    number_count = 0
    if(el % 2050 != 0 ):
        print(-1)
        continue

    current_multiplicators = int(el / 2050)
    while(current_multiplicators >= 10):
        number_count += current_multiplicators % 10
        current_multiplicators = current_multiplicators // 10
    number_count += current_multiplicators
    print(number_count)


