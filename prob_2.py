"""
Find the sum of even Fibonacci numbers whose value doesn't exceed 4M
"""

fib_series = [1,2]

while fib_series[-1] < 4_000_000:
    # j = fib_series[-2]
    k = fib_series[-1] + fib_series[-2]
    fib_series.append(k)

total = 0
for num in fib_series:
    if num % 2 == 0:
        total += num

print(f'Result: {total}')