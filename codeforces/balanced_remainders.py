# https://codeforces.com/contest/1490/problem/B

import pdb

def solve(a, n):
    mod_0 = []
    mod_1 = []
    mod_2 = []
    count = 0
    for i in range(n):
        curr_mod = a[i] % 3
        if(curr_mod == 0):
            mod_0.append(a[i])
        elif(curr_mod == 1):
            mod_1.append(a[i])
        elif(curr_mod == 2):
            mod_2.append(a[i])
    mod_0_size = len(mod_0)
    mod_1_size = len(mod_1)
    mod_2_size = len(mod_2)
    mods = [mod_0, mod_1, mod_2]
    while(mod_0_size != mod_1_size or mod_1_size != mod_2_size):
        count += 1
        max_mod_size = 0
        max_mod_index = 0
        for i in range(3):
            if len(mods[i]) > max_mod_size:
                max_mod_size = len(mods[i])
                max_mod_index = i
        increased_el = mods[max_mod_index].pop() + 1
        curr_mod = increased_el % 3
        if(curr_mod == 0):
            mod_0.append(increased_el)
        elif(curr_mod == 1):
            mod_1.append(increased_el)
        elif(curr_mod == 2):
            mod_2.append(increased_el)
        mod_0_size = len(mod_0)
        mod_1_size = len(mod_1)
        mod_2_size = len(mod_2)
        mods = [mod_0, mod_1, mod_2]
        

    
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    print(solve(a, n))

# solve([0 ,2 ,5 ,5 ,4, 8], 6)