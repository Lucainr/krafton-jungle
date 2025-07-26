import sys

t = int(sys.stdin.readline())

for _ in range(t):
    ps = sys.stdin.readline().strip()
    stack = []

    for i in ps:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                stack.append(")")
                break
    if not stack:
        print("YES")
    else:
        print("NO")