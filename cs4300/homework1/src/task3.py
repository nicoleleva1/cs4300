# checks if a number is positive, negative, or zero
def check_sign(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

# uses a for loop to find and return the first n prime numbers
def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        # check if candidate is divisible by any prime found so far
        is_prime = all(candidate % p != 0 for p in primes)
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

# uses a while loop to add up all numbers from 1 to 100
def sum_1_to_100():
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total