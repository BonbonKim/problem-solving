import sys

stack = []
ans = []
n = int(input())

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command == 'pop':
        if stack:
            ans.append(stack[-1])
            stack = stack[:-1]
        else:
            ans.append(-1)
    elif command == 'size':
        ans.append(len(stack))
    elif command == 'empty':
        ans.append(0 if stack else 1)
    elif command == 'top':
        ans.append(stack[-1] if stack else -1)
    else: # push
        stack.append(command.split(' ')[1])

print("\n".join(map(str, ans)))