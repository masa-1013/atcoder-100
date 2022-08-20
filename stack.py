import sys

data = sys.stdin.readlines()
items = [line.rstrip() for line in data][0].split(' ')

stack = []

for i in items:
  if (i == '+'):
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b) + int(a))
  elif(i == '-'):
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b) - int(a))
  elif(i == '*'):
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b) * int(a))
  else:
    stack.append(i)

print(stack.pop())