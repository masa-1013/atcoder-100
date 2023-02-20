import math

ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
dx, dy = list(map(int, input().split()))

def pointToPointLength(x1, y1, x2, y2):
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def calcAngle(x1, x2, y1):
  return calcCos((x1 ** 2 + x2 ** 2 - y1 ** 2) / (2 * x1 * x2))

def calcCos(cosX):
  return math.degrees(math.acos(cosX))

ab = pointToPointLength(ax, ay, bx, by)
bc = pointToPointLength(bx, by, cx, cy)
cd = pointToPointLength(cx, cy, dx, dy)
ad = pointToPointLength(ax, ay, dx, dy)
ac = pointToPointLength(ax, ay, cx, cy)

A1 = calcAngle(ab, ac, bc)
A2 = calcAngle(ad, ac, cd)
B = calcAngle(ab, bc, ac)
C1 = calcAngle(ac, bc, ab)
C2 = calcAngle(cd, ac, ad)
D = calcAngle(ad, cd, ac)

if (A1 + A2 >= 180 or B >= 180 or C1 + C2 >= 180 or D >= 180):
  print("No")
else:
  print("Yes")
