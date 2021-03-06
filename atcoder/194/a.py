# https://atcoder.jp/contests/abc194
# a.py


# an ice cream type product with at least 
# 15
#  percent milk solids and at least 
# 8
#  percent milk fat is called an ice cream;
# an ice cream type product with at least 
# 10
#  percent milk solids and at least 
# 3
#  percent milk fat that is not an ice cream is called an ice milk;
# an ice cream type product with at least 
# 3
#  percent milk solids that is not an ice cream or an ice milk is called a lacto ice;
# an ice cream type product that is not an ice cream, an ice milk, or a lacto ice is called a flavored ice.


A, B = tuple(map(int, input().split(" ")))
milk_fats = A+B
if(milk_fats >= 15 and B >= 8):
    print(1)
elif(milk_fats >= 10 and B >= 3):
    print(2)
elif(milk_fats >= 3):
    print(3)
else:
    print(4)