"""import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)   # True
print("second ссылается на first:", second[0] is first)   # True
print()

print("Автосборка включена:", gc.isenabled())
print("Текущие счетчики поколений:", gc.get_count())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:", gc.get_stats())
print()

id_first = id(first)
id_second = id(second)
print(f"id(first) = {id_first}")
print(f"id(second) = {id_second}")
print()

del first
del second

collected = gc.collect()
print(f"gc.collect() вернул: {collected} (уничтожено объектов)")
print()

print("=== Дополнительный эксперимент ===")
gc.disable()
print("Автосборка выключена:", gc.isenabled())

cycles = []
for i in range(100):
    a = []
    b = []
    a.append(b)
    b.append(a)
    cycles.append((a, b))

del cycles
print("Внешние ссылки удалены, но автосборка выключена => циклы пока в памяти")

before = gc.collect()
print(f"gc.collect() уничтожил: {before} объектов")


gc.enable()
print("Автосборка снова включена:", gc.isenabled())"""

import gc

before = gc.collect()

a = {"name": "A", "neighbors": []}
b = {"name": "B", "neighbors": []}
c = {"name": "C", "neighbors": []}
d = {"name": "D", "neighbors": []}

a["neighbors"].append(b)
b["neighbors"].append(c)
c["neighbors"].append(a)

print("A ->", [n["name"] for n in a["neighbors"]])
print("B ->", [n["name"] for n in b["neighbors"]])
print("C ->", [n["name"] for n in c["neighbors"]])
print("D ->", [n["name"] for n in d["neighbors"]])

id_d = id(d)

del a, b, c

after = gc.collect()
print(f"Собрано до: {before}, после: {after}")

assert d is not None
assert id(d) == id_d
print("Узел D доступен:", d)