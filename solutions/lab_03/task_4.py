def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if len(values) == 0:
        return 0.0
    total = 0
    for v in values:
        total = total + v
    return total / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    parts = name.split()
    result = []
    for p in parts:
        result.append(p[0].upper() + p[1:].lower())
    return " ".join(result)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    if len(results) == 0:
        return f"{prefix}: у студента {student} нет результатов"
    mean = arithmetic_mean(results)
    return f"{prefix}: {student}, средний балл {mean:.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    result = []
    for tag in tags:
        tag = tag.strip()
        if lowercase:
            tag = tag.lower()
        if tag == "":
            continue
        if tag not in result:
            result.append(tag)
    return tuple(result)


assert arithmetic_mean([1, 2, 3]) == 2
assert arithmetic_mean([5]) == 5
assert arithmetic_mean([]) == 0.0

assert normalize_name("  иВАН   петров ") == "Иван Петров"
assert normalize_name("anna") == "Anna"
assert normalize_name("") == ""

assert build_report("Anna", [5, 4]) == "Результат: Anna, средний балл 4.50"
assert build_report("Anna", [5, 4], precision=0) == "Результат: Anna, средний балл 4"
assert build_report("Anna", [], prefix="Итог") == "Итог: у студента Anna нет результатов"

assert collect_tags("Python", " python ", "", "Code") == ("python", "code")
assert collect_tags("A", "a", lowercase=False) == ("A", "a")
assert collect_tags() == ()
print("Все assert пройдены")

print()
print(build_report("Anna", [5, 4, 5]))
print(build_report("Boris", [3, 4], precision=1, prefix="Итог"))
print(collect_tags("Python", "ALGO", "python"))
print(collect_tags("Python", "ALGO", lowercase=False))

numbers = [4, 5, 5, 3]
print(arithmetic_mean(numbers))
tag_list = ["a", "b", "a"]
print(collect_tags(*tag_list))
settings = {"precision": 3, "prefix": "Отчет"}
print(build_report("Daria", numbers, **settings))

copy_before = numbers[:]
arithmetic_mean(numbers)
build_report("Daria", numbers)
assert numbers == copy_before

course = "Программирование"


def outer():
    semester = 1

    def inner():
        nonlocal semester
        semester = semester + 1
        print("inner видит course:", course)
        print("inner изменил semester:", semester)

    inner()
    print("outer после inner, semester:", semester)


print()
outer()
print("Глобальное course не изменилось:", course)


def add_result(value, results=[]):
    results.append(value)
    return results


print()
print("Ошибочная версия:")
print(add_result(1))
print(add_result(2))
print(add_result(3))


def add_result_fixed(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


print("Исправленная версия:")
print(add_result_fixed(1))
print(add_result_fixed(2))
assert add_result_fixed(2) == [2]


def apply_to_results(operation, values):
    """Применяет функцию к каждому результату, возвращает новый список."""
    result = []
    for v in values:
        result.append(operation(v))
    return result


def double(x):
    return x * 2


print()
print(apply_to_results(double, [1, 2, 3]))
print(apply_to_results(lambda x: x + 10, [1, 2, 3]))


def make_threshold_checker(threshold):
    def check(score):
        return score >= threshold
    return check


check_pass = make_threshold_checker(60)
check_good = make_threshold_checker(75)
print(check_pass(65), check_good(65))
print(check_pass(80), check_good(80))
assert check_pass(60) and not check_good(60)
