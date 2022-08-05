from bisect import bisect_left, bisect_right

a = [1,10,20,30]
print(bisect_left(a, 5))
print(bisect_right(a, 5))
