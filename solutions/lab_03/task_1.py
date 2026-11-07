LEVELS = ["недостаточный", "удовлетворительный", "хороший", "отличный"]


def get_level_number(score):
    """Номер уровня по результату: 0 - недостаточный, 3 - отличный."""
    if score >= 90:
        return 3
    elif score >= 75:
        return 2
    elif score >= 60:
        return 1
    else:
        return 0


def describe_work(work_type):
    match work_type:
        case "exam":
            return "экзаменационная работа"
        case "project":
            return "проектная работа"
        case "practice":
            return "практическая работа"
        case _:
            return "неизвестный тип работы"


def process_student(score, work_type, absences):
    """Возвращает строку с итогом по одному студенту."""
    if score < 0 or score > 100:
        return "Ошибка: результат должен быть от 0 до 100"
    elif absences < 0 or absences > 5:
        return "Ошибка: пропусков должно быть от 0 до 5"

    number = get_level_number(score)
    if absences > 3 and number > 0:
        number = number - 1

    return f"Баллы: {score}, {describe_work(work_type)}, пропусков {absences}: {LEVELS[number]}"


def get_level_name(score, absences):
    """Только название уровня (нужно для подсчета в сводке)."""
    number = get_level_number(score)
    if absences > 3 and number > 0:
        number = number - 1
    return LEVELS[number]


score = int(input("Результат (0-100): "))
work_type = input("Тип работы (exam, project, practice): ")
absences = int(input("Пропусков (0-5): "))
print(process_student(score, work_type, absences))

tests = [
    (0, "exam", 0, "Баллы: 0, экзаменационная работа, пропусков 0: недостаточный"),
    (59, "project", 0, "Баллы: 59, проектная работа, пропусков 0: недостаточный"),
    (60, "practice", 0, "Баллы: 60, практическая работа, пропусков 0: удовлетворительный"),
    (74, "exam", 3, "Баллы: 74, экзаменационная работа, пропусков 3: удовлетворительный"),
    (75, "project", 0, "Баллы: 75, проектная работа, пропусков 0: хороший"),
    (89, "practice", 4, "Баллы: 89, практическая работа, пропусков 4: удовлетворительный"),
    (90, "exam", 5, "Баллы: 90, экзаменационная работа, пропусков 5: хороший"),
    (100, "project", 0, "Баллы: 100, проектная работа, пропусков 0: отличный"),
    (30, "test", 5, "Баллы: 30, неизвестный тип работы, пропусков 5: недостаточный"),
    (101, "exam", 0, "Ошибка: результат должен быть от 0 до 100"),
    (50, "exam", 6, "Ошибка: пропусков должно быть от 0 до 5"),
]

print()
print("Тесты:")
for t in tests:
    result = process_student(t[0], t[1], t[2])
    print(result)
    assert result == t[3]
print("Все тесты пройдены")

students = [
    (95, "exam", 0),
    (88, "project", 1),
    (74, "practice", 4),
    (60, "exam", 2),
    (59, "project", 0),
    (91, "practice", 5),
    (75, "exam", 3),
    (20, "practice", 5),
    (82, "project", 4),
    (66, "exam", 0),
]

print()
print("Результаты студентов:")
counts = {}
for level in LEVELS:
    counts[level] = 0

for s in students:
    print(process_student(s[0], s[1], s[2]))
    level = get_level_name(s[0], s[2])
    counts[level] = counts[level] + 1

print()
print("Сводка:")
for level in LEVELS:
    print(level + ":", counts[level])
