import random

def generate_lotto_numbers():
    numbers = sorted(random.sample(range(1, 51),6))
    return ','.joint(str(number) for num in numbers)
