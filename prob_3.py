"""Find the largest prime factor of a number"""

def largest_prime_factor(n: int) -> int:
    """Find the largest prime factor of a number"""
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(f'Result: {largest_prime_factor(600851475143)}')