x, y, n = list(map(int, input().split()))

if (x * 3 >= y and n >= 3):
  y_apple = n // 3
  x_apple = n - y_apple * 3
  print(y_apple * y + x_apple * x)
else:
  print(x * n)