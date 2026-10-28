import tracemalloc
from sys import getsizeof
"""
print(getsizeof([]))
print(getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(getsizeof((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(getsizeof("1"*10))
print(getsizeof(10))
print(getsizeof(None))"""
"""spis = []
l = getsizeof(spis)
for x in range(100):
    spis.append(x)
    if l!= getsizeof(spis):
        print(spis, len(spis))
        l = getsizeof(spis)"""

tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"list: текущий {current/1024:.1f} КиБ, пик {peak/1024:.1f} КиБ")

tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"range: текущий {current/1024:.1f} КиБ, пик {peak/1024:.1f} КиБ")
