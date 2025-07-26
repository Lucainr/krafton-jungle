x, y, w, h = map(int, input().split())
zero_point = 0
min_point = 0

hansoo_x = abs(x-w)
hansoo_y = abs(y-h)

if x<y or x==y:
    zero_point = x
else:
    zero_point = y
    
if hansoo_x < hansoo_y:
    min_point = hansoo_x
else:
    min_point = hansoo_y
    
if zero_point < min_point:
    print(zero_point)
else:
    print(min_point)
    
# x, y, w, h = map(int, input().split())
# print(min(x, w - x, y, h - y))

