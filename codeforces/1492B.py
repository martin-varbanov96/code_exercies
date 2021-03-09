# https://codeforces.com/problemset/problem/1492/B
# 1492B.py
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))

    index_dict = {}

    for i in range(len(a)):
        index_dict[a[i]] = i

    count = n
    global_list = []
    while(count != 0):
        max_index = index_dict[count]
        current_list = a[max_index:]
        del a[max_index:]
        count -= 1
        # count -= count - max_index
        global_list.extend(current_list)

    print(*global_list, sep=' ')
