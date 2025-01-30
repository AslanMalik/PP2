class Prime:
    def __init__ (self, arr):
        self.arr = arr

    def define_prime(self, x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True


    def filter_prime_number(self):
        return sorted(list(filter(lambda x: self.define_prime(x), self.arr)))



numbers = [int(x) for x in input().split()] 

number = Prime(numbers)

print(number.filter_prime_number())