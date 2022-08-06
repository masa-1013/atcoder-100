from bisect import bisect_left, bisect_right

a = [1,10,20,30]
print(bisect_left(a, 0))
print(bisect_right(a, 5))
