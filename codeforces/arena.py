# arena.py

t = int(input())
for i in range(t):
    n = int(input())
    players_level = input().split(" ")
    players_level = [int(el) for el in players_level]
    players_level.sort()

    min_level = players_level[0]
    min_level_count = 1
    solvable_flag= False
    for i in range(1, len(players_level)):
        if(players_level[i] != min_level):
            print(n-min_level_count)
            break
        min_level_count += 1
    else:
        print(0)
        
        
