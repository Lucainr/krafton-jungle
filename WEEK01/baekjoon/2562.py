max_list = []

for i in range(9):
    max_list.append(int(input()))

max_val = max_list[0]
max_index = 0

for i in range(9):
    if max_list[i] > max_val:
        max_val = max_list[i]
        max_index = i

print(max_val)
print(max_index + 1)