from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    # Brute-force approach
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return li[i], li[j]

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    # Efficient approach using a set
    num_set = set()
    for num in li:
        complement = target - num
        if complement in num_set:
            return complement, num
        num_set.add(num)


target_value = 5
list_of_numbers = [1, 2, 3, 4, 5]

result_bruteforce = find_sum(target_value, list_of_numbers)
result_efficient = find_sum_fast(target_value, list_of_numbers)

print(f"Brute-force result: {result_bruteforce}")
print(f"Efficient result: {result_efficient}")
