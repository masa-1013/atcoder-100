import itertools

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

per = itertools.permutations(range(1, n+1), n)

p_number = 0
q_mumber = 0

if (p == q):
  print(0)
  exit()

for index, i in enumerate(per):
  if (list(i) == p):
    p_number = index + 1
    continue
  if (list(i) == q):
    q_mumber = index + 1

print(abs(p_number - q_mumber))