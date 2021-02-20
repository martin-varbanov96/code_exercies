def solve(inp_string):
    is_odd = 1
    for el in inp_string:
        if(is_odd):
            is_odd = 0
            if(ord(el) < 97):
                return False
        else:
            is_odd = 1
            if(ord(el) >= 97):
                return False
    return True
            

inp_string = str(input())
a = "Yes" if solve(inp_string) else "No"
print(a)


