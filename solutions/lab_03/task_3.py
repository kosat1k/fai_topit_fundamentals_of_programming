submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = set()
labs = set()
attempts_by_student = {}
best = {}
attempts_count = {}
students_by_lab = {}


def add_record(student, lab, result):
    """Добавляет одну запись во все структуры, ничего не строя заново."""
    students.add(student)
    labs.add(lab)

    if student not in attempts_by_student:
        attempts_by_student[student] = []
    attempts_by_student[student].append((lab, result))

    key = (student, lab)
    if key not in best or result > best[key]:
        best[key] = result
    if key in attempts_count:
        attempts_count[key] = attempts_count[key] + 1
    else:
        attempts_count[key] = 1

    if lab not in students_by_lab:
        students_by_lab[lab] = set()
    students_by_lab[lab].add(student)


for record in submissions:
    add_record(record[0], record[1], record[2])

print("Студенты:", sorted(students))
print("Работы:", sorted(labs))
print("Попытки студентов:", attempts_by_student)
print("Лучшие результаты:", best)
print("Количество попыток:", attempts_count)

both = students_by_lab["lab_01"] & students_by_lab["lab_02"]
print("Сдавали обе работы:", sorted(both))

print()
print("Добавляем запись ('daria', 'lab_02', 4)")
add_record("daria", "lab_02", 4)
print("Сдавали обе работы:", sorted(students_by_lab["lab_01"] & students_by_lab["lab_02"]))
print("Попытки daria:", attempts_by_student["daria"])


def run_command(line):
    """Разбирает текстовую команду и возвращает строку-ответ."""
    parts = line.split()
    if len(parts) == 0:
        return "Пустая команда"

    command = parts[0]
    if command == "student" and len(parts) == 2:
        if parts[1] not in attempts_by_student:
            return "Студент не найден"
        return str(attempts_by_student[parts[1]])
    elif command == "best" and len(parts) == 3:
        key = (parts[1], parts[2])
        if key not in best:
            return "Такой записи нет"
        return str(best[key])
    elif command == "attempts" and len(parts) == 3:
        key = (parts[1], parts[2])
        if key not in attempts_count:
            return "Такой записи нет"
        return str(attempts_count[key])
    elif command == "completed" and len(parts) == 2:
        if parts[1] not in students_by_lab:
            return "Работа не найдена"
        return str(sorted(students_by_lab[parts[1]]))
    else:
        return "Неизвестная команда"


print()
print("Запросы:")
queries = [
    "student anna",
    "best anna lab_01",
    "attempts boris lab_02",
    "completed lab_01",
    "best anna lab_09",
    "student petr",
    "completed lab_05",
    "delete anna",
    "best anna",
    "",
]
for q in queries:
    print(">", q)
    print(run_command(q))

assert best[("anna", "lab_01")] == 5
assert attempts_count[("anna", "lab_01")] == 2
assert run_command("hello") == "Неизвестная команда"
