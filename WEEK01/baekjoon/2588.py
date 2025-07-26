a = int(input())
b = int(input())

b1 = b//100
b2 = (b-b1*100)//10
b3 = b-((b1*100)+(b2*10))

c = [b1, b2, b3]

print(a*c[2], a*c[1], a*c[0], a*b)