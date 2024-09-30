import math


def count_awesome_numbers(A, B):
    count = 0
    for N in range(A, B + 1):
        candidate_square = 2 * N - 1
        M = int(math.sqrt(candidate_square))
        if M * M == candidate_square:
            count += 1
    return count

# Пример использования
A = int(input())
B = int(input())
result = count_awesome_numbers(A, B)
print(result)