#Random Numbers branch

import random

arr = [random.randint(1, 100) for _ in range(20)]
target = random.choice(arr) if random.random() < 0.5 else 999 # 50% chance of failure