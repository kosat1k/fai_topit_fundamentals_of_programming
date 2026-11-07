students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

CATEGORIES = ["отличный", "хороший", "удовлетворительный", "недостаточный", "нет данных"]


def mean(values):
    """Среднее списка чисел. Для пустого списка возвращает 0.0."""
    if len(values) == 0:
        return 0.0
    total = 0
    for v in values:
        total = total + v
    return total / len(values)


def minimum(values):
    """Минимум непустого списка. Для пустого возвращает None."""
    if len(values) == 0:
        return None
    result = values[0]
    for v in values:
        if v < result:
            result = v
    return result


def maximum(values):
    """Максимум непустого списка. Для пустого возвращает None."""
    if len(values) == 0:
        return None
    result = values[0]
    for v in values:
        if v > result:
            result = v
    return result


def classify(score):
    """Категория по числу от 0 до 100."""
    if score >= 90:
        return "отличный"
    elif score >= 75:
        return "хороший"
    elif score >= 60:
        return "удовлетворительный"
    else:
        return "недостаточный"


def student_summary(name, results):
    """Словарь с итогами одного студента. Если результатов нет, категория 'нет данных'."""
    if len(results) == 0:
        return {"name": name, "count": 0, "mean": None, "min": None, "max": None,
                "category": "нет данных"}
    avg = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": avg,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(avg),
    }


def find_top_students(students):
    """Список имен студентов с наибольшим средним. Студенты без результатов не учитываются."""
    top = []
    best_mean = None
    for name in students:
        if len(students[name]) == 0:
            continue
        avg = mean(students[name])
        if best_mean is None or avg > best_mean:
            best_mean = avg
            top = [name]
        elif avg == best_mean:
            top.append(name)
    return top


def make_ranking(students):
    """Список пар (имя, среднее) по убыванию среднего. Исходный словарь не меняется."""
    ranking = []
    for name in students:
        if len(students[name]) > 0:
            ranking.append((name, mean(students[name])))
    for i in range(1, len(ranking)):
        j = i
        while j > 0 and ranking[j][1] > ranking[j - 1][1]:
            ranking[j], ranking[j - 1] = ranking[j - 1], ranking[j]
            j = j - 1
    return ranking


def group_summary(students):
    """Общая статистика группы."""
    counts = {}
    for c in CATEGORIES:
        counts[c] = 0

    all_results = []
    for name in students:
        info = student_summary(name, students[name])
        counts[info["category"]] = counts[info["category"]] + 1
        for r in students[name]:
            all_results.append(r)

    return {
        "students": len(students),
        "group_mean": mean(all_results),
        "categories": counts,
        "leaders": find_top_students(students),
        "ranking": make_ranking(students),
    }


def format_report(student_data, group_data):
    """Итоговый отчет. student_data - список словарей из student_summary."""
    lines = []
    lines.append("Результаты студентов:")
    for s in student_data:
        if s["count"] == 0:
            lines.append(f"{s['name']}: нет результатов")
        else:
            lines.append(f"{s['name']}: среднее {s['mean']:.2f}, минимум {s['min']}, "
                         f"максимум {s['max']}, категория {s['category']}")
    lines.append("")
    lines.append(f"Студентов в группе: {group_data['students']}")
    if group_data["students"] > 0:
        lines.append(f"Общий средний результат: {group_data['group_mean']:.2f}")
    if len(group_data["leaders"]) > 0:
        lines.append("Лидеры: " + ", ".join(group_data["leaders"]))
    lines.append("Рейтинг:")
    place = 1
    for pair in group_data["ranking"]:
        lines.append(f"{place}. {pair[0]} - {pair[1]:.2f}")
        place = place + 1
    lines.append("Количество по категориям:")
    for c in CATEGORIES:
        if group_data["categories"][c] > 0:
            lines.append(f"{c}: {group_data['categories'][c]}")
    return "\n".join(lines)


def make_report(students):
    student_data = []
    for name in students:
        student_data.append(student_summary(name, students[name]))
    return format_report(student_data, group_summary(students))


before = {k: v[:] for k, v in students.items()}
print("Сценарий 1: обычный набор")
print(make_report(students))
assert students == before
assert find_top_students(students) == ["Дарья"]

print()
print("Сценарий 2: один студент")
one = {"Петр": [80, 90]}
print(make_report(one))
assert find_top_students(one) == ["Петр"]

print()
print("Сценарий 3: несколько лидеров")
same = {"Ася": [80, 90], "Боря": [85, 85], "Вера": [70]}
print(make_report(same))
assert find_top_students(same) == ["Ася", "Боря"]

print()
print("Сценарий 4: пустая группа")
print(make_report({}))
assert find_top_students({}) == []
assert group_summary({})["students"] == 0

print()
print("Сценарий 5: студент без результатов")
empty_one = {"Гоша": [], "Дима": [70]}
print(make_report(empty_one))
assert student_summary("Гоша", [])["category"] == "нет данных"
assert find_top_students(empty_one) == ["Дима"]

print()
print("Сценарий 6: границы категорий")
for score in [0, 59, 60, 74, 75, 89, 90, 100]:
    print(score, classify(score))
assert classify(59) == "недостаточный"
assert classify(60) == "удовлетворительный"
assert classify(74) == "удовлетворительный"
assert classify(75) == "хороший"
assert classify(89) == "хороший"
assert classify(90) == "отличный"

assert minimum([3, 1, 2]) == 1
assert maximum([3, 1, 2]) == 3
assert mean([1, 2]) == 1.5
assert minimum([]) is None
print()
print("Все проверки пройдены")
