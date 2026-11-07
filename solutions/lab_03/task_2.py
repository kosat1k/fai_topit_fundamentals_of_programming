measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

total = 0
smallest = measurements[0]
biggest = measurements[0]
even_count = 0

for x in measurements:
    total = total + x
    if x < smallest:
        smallest = x
    if x > biggest:
        biggest = x
    if x % 2 == 0:
        even_count = even_count + 1

average = total / len(measurements)
above_average = 0
for x in measurements:
    if x > average:
        above_average = above_average + 1

print("Сумма:", total)
print("Минимум:", smallest)
print("Максимум:", biggest)
print("Четных значений:", even_count)
print("Среднее:", average)
print("Больше среднего:", above_average)


def linear_search(values, target):
    """Индекс первого вхождения или -1. Второй результат - число сравнений."""
    comparisons = 0
    for i in range(len(values)):
        comparisons = comparisons + 1
        if values[i] == target:
            return i, comparisons
    return -1, comparisons


number = int(input("Какое число искать? "))
index, _ = linear_search(measurements, number)
print("Индекс первого вхождения:", index)


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


print()
for n in [1, 2, 3, 4, 17, 25, 49, 97, 100]:
    print(n, is_prime(n))
assert is_prime(2) and is_prime(17) and is_prime(97)
assert not is_prime(1) and not is_prime(49) and not is_prime(100)


def selection_sort(values):
    """Возвращает новый отсортированный список, исходный не меняется."""
    result = values[:]
    for i in range(len(result) - 1):
        min_index = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result


def binary_search(values, target):
    """Поиск в отсортированном списке. Считаем по одному сравнению на шаг."""
    left = 0
    right = len(values) - 1
    comparisons = 0
    while left <= right:
        middle = (left + right) // 2
        comparisons = comparisons + 1
        if values[middle] == target:
            return middle, comparisons
        elif values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, comparisons


print()
print("Сортировка:", selection_sort(measurements))
print("Исходный список не изменился:", measurements)
assert selection_sort([3, 1, 2]) == [1, 2, 3]
assert binary_search([1, 3, 5, 7], 7)[0] == 3
assert binary_search([1, 3, 5, 7], 4)[0] == -1

print()
print("Размер | Искомое | Линейный | Бинарный")
for n in [10, 100, 1000]:
    data = []
    for i in range(n):
        data.append((i * 17) % n)
    data = selection_sort(data)

    for target in [n - 1, n // 2, -5]:
        i1, c1 = linear_search(data, target)
        i2, c2 = binary_search(data, target)
        assert i1 == i2
        print(n, "|", target, "|", c1, "|", c2)
