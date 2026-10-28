import tracemalloc
from tracemalloc import *
from sys import getsizeof

scens = {}

def addslov(name, expr):
    start()
    val = eval(expr)
    current, peak = get_traced_memory()
    stop()
    scens[name] = {
        "name": name,
        "count": len(val) if hasattr(val, "__len__") else 1,
        "size": getsizeof(val),
        "current": current,
        "peak": peak,
    }

spis = [
    ("[]", "пустой список"),
    ("list(range(10))", "10 элементов список"),
    ("tuple(range(10))", "10 элементов кортеж"),
    ('"0123456789"', "строка 10 символов"),
    ("10", "целое число"),
    ("None", "None"),
]

for expr, name in spis:
    addslov(name, expr)

print("Сценарий | Элементов | Размер, Б | Текущая, Б | Пик, Б")
print("-" * 70)
for key in scens:
    r = scens[key]
    print(r["name"], "|", r["count"], "|", r["size"], "|", r["current"], "|", r["peak"])