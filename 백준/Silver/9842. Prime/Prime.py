def nth_prime(n):
  # Initialize a list to store prime numbers
  primes = []

  # Start with the first prime number, which is 2
  num = 2

  # Keep generating prime numbers until we have n of them
  while len(primes) < n:
    # Assume that the number is prime
    is_prime = True

    # Check if the number is prime by checking if it is divisible by any of the prime numbers we have found so far
    for prime in primes:
      # If the number is divisible by a prime number, it is not prime
      if num % prime == 0:
        is_prime = False
        break

    # If the number is prime, add it to the list of prime numbers
    if is_prime:
      primes.append(num)

    # Move on to the next number
    num += 1

  # Return the last prime number in the list, which is the nth prime number
  return primes[-1]

print(nth_prime(int(input())))