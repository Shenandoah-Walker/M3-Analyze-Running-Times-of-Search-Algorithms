#Random Numbers branch
from search_algorithms import sequential_search, binary_search, interpolation_search
import random

arr = [random.randint(1, 100) for _ in range(20)]
arr = sorted([random.randint(1, 1000000) for _ in range(N)])
target = random.choice(arr) if random.random() < 0.5 else 999 # 50% chance of failure


#Recursive Binary Search
index = recursive_binary_search(arr, target, 0, len(arr) - 1)
print(f"{target} found at index {index}" if index != -1 else
f"{target} not found")





