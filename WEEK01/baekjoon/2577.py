a = int(input())
b = int(input())
c = int(input())

result = a*b*c

result_str = str(result)

for i in range(10):
    num_count = result_str.count(str(i))
    print(num_count)