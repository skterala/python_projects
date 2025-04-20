'''
Import Python Random module to generate the random integer and random floating numbers.
https://docs.python.org/3/library/random.html

Functions:
-----------
Random floating number generators:
        1. random():  Returns a random float between 0.0 (inclusive) and 1.0 (exclusive).
                      If you want to extend this from 0 to 10, then multiply random() module with 10.
        2. uniform(a, b) : Returns a random float N such that a <= N <= b.
3. randint(a, b) : Returns a random integer N such that a <= N <= b. Inclusive.
4. randrange(start, stop[, step]) : Returns a randomly selected element from range(start, stop, step).
5. choice(seq) : Returns a randomly selected element from a non-empty sequence.
6. choices(population, weights=None, *, cum_weights=None, k=1) : Returns a list of k elements chosen with replacement.
                                                                 Allows weighted random selection.
7. sample(population, k) : Returns a list of k unique elements chosen without replacement.
8. shuffle(x) : Shuffles the sequence in place (only works on mutable sequences like lists).
9. seed(a=None) : Initializes the random number generator. Useful for reproducibility.
10. getstate() : Returns an object representing the internal state of the generator.
11. setstate(state) : Restores the internal state of the generator to a state from getstate().
12. betavariate(alpha, beta) : Returns a float from a Beta distribution.
13. expovariate(lambd) : Returns a float from an exponential distribution with parameter lambd (1/mean).
14. gammavariate(alpha, beta) : Returns a float from a Gamma distribution.
15. gauss(mu, sigma) : Returns a float from a Gaussian distribution with mean mu and std. dev. sigma.
16. lognormvariate(mu, sigma) : Returns a float from a log-normal distribution.
17. normalvariate(mu, sigma) : Returns a float from a normal (Gaussian) distribution.
18. triangular(low, high, mode): Returns a float from a triangular distribution.
19. vonmisesvariate(mu, kappa) : Returns a float from a von Mises distribution (circular analog of normal distribution).
20. weibullvariate(alpha, beta) : Returns a float from a Weibull distribution.
'''

import random
random_float_number_0_1 = random.random()
random_float_number_10_100 = random.uniform(10, 100)
random_int_25_50 = random.randint(25,50)
random_range = random.randrange(10, 50, 3)
choice = random.choice([1,2,3,4,5,6,7,8])
sample = random.sample([1,2,3,4,5,6,7,8], 5)

print(f"random_float_number_0_1: {random_float_number_0_1}")
print(f"random_float_number_10_100: {random_float_number_10_100}")
print(f"random_int_25_50: {random_int_25_50}")
print(f"random_range: {random_range}")
print(f"Choice Number from the list: {choice}")
print(f"Sample from the give population: {sample}")