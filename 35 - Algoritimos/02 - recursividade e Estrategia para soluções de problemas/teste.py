n = 0
t = 5
for i  in range(t):
    n = n + i
    print(n)



def fibonacci_iter(n):
    sequence = [0, 1]
    if n >= 2:
        for x in range(2, n+1):
            next = sequence[-1] + sequence[-2]
            sequence.append(next)
    return sequence[n]

print(fibonacci_iter(7))