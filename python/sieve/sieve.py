import math
class Sieve:
    def __init__(self) -> None:
        self.prime_array = [] # save array to object attributes for easy referencing
        self.max_number = 200000000
        self.pa = self.get_prime()

    def nth_prime(self, n: int) -> int:
        prime_array = self.pa
        print(prime_array[n])
        return prime_array[n]

    def get_prime(self) -> list:

        # list of bools setting each number to true for every number up to max number+1
        # boolean lists tend to use less memory than integer lists
        prime_bool_list = [True for i in range(self.max_number+1)]

        p = 2 # start at 2, 2 is the first prime number
        # n * n has to be lt or eq max number
        # We do this to mark each prime number that is divisible by n and gt or eq the square of n
        while (p*p <= self.max_number):
            if (prime_bool_list[p]):
                for i in range(p*p, self.max_number+1, p):
                    prime_bool_list[i] = False
            p += 1

        # loop over the potential prime numbers in the max number
        # to determine prime numbers and append to list.
        for p in range(2, self.max_number+1):
            if prime_bool_list[p]:
                self.prime_array.append(p)
        return self.prime_array
