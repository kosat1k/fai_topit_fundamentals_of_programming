import copy
"""
original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

original.append(["Databases", 5])
original[0][1] = 3
print(original, alias, shallow, deep, sep="\n") """
# Неправильное создание матрицы
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print(wrong_matrix[0] is wrong_matrix[1] is wrong_matrix[2])
print(wrong_matrix)
# Правильное
correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print(correct_matrix[0] is correct_matrix[1] is correct_matrix[2])
print(correct_matrix)

