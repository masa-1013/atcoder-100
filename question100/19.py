all_length = int(input())
shop_numbers = int(input())
order_numbers = int(input())
shop_position = [int(input()) for _ in range(shop_numbers-1)]
delivery_position = [int(input()) for _ in range(order_numbers)]

shop_position.append(all_length)
shop_position.append(0)
shop_position.sort()

def search_distance_neary_shop(target, left, right):
  if right - left == 1:
    left_distance = abs(shop_position[left] - target)
    right_distance = abs(shop_position[right] - target)
    return min([left_distance, right_distance])
  
  index = (left + right) // 2

  if (target >= shop_position[index]):
    return search_distance_neary_shop(target, index, right)
  else:
    return search_distance_neary_shop(target, left, index)

ans = 0
for i in delivery_position:
  ans += search_distance_neary_shop(i, 0, shop_numbers + 2)

print(ans)