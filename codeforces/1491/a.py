n, q = tuple(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
zero_index = a.count(1)
 
for _ in range(q):
    t, x = tuple(map(int, input().split(" ")))
    x -= 1
    if(t == 1):
        current_val = a[x]
        a[x] = 1- a[x]
        if(current_val == 0):
            zero_index += 1
        else:
            zero_index -= 1
        
    elif(t == 2):
        # print xth element
        print(1 if x < zero_index else 0)

