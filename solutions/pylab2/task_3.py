"""import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

import weakref


class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())"""

import weakref


class Record:
    pass
record1 = Record()
record2 = Record()
records = weakref.WeakValueDictionary()
records["record1"] = record1
records["record2"] = record2
records["record3"] = Record()
del record1
print(list(records.items()))
del record2
print(list(records.items()))