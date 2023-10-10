class SpacePort:
    # Создание космодрома, в котором size штук доков.
    # Доки нумеруются от 0 до size-1.
    # В момент создания все доки свободны.
    # Попытка создать космодром с неположительным числом доков должна приводить к исключению.
    def __init__(self, size) -> None:
        if size <= 0:
            raise ValueError
        else:
            self.docs = [0] * size

    # Запросить посадку в док с номером dock_number.
    # Если такого номера дока нет - выбросить exception.
    # Если док есть, но занят - вернуть false (запрет посадки).
    # Если док есть и свободен - вернуть true (разрешение посадки) и док становится занят.
    def request_landing(self, dock_number):
        if dock_number > len(self.docs):
            raise ValueError
        else:
            if self.docs[dock_number] == 1:
                return False
            else:
                self.docs[dock_number] = 1
                return True
    # Запросить взлёт из дока с номером dock_number.
    # Если такого номера дока нет - выбросить exception.
    # Если док есть, но там пусто - выбросить exception.
    # Если док есть и в нём кто-то стоит - вернуть true (разрешение взлёта) и док становится свободен.
    def request_takeoff(self, dock_number):
        if dock_number > len(self.docs):
            raise ValueError
        elif self.docs[dock_number] == 0:
            raise ValueError
        else:
            self.docs[dock_number] = 0
            return True

s = SpacePort(5)
print(s.request_landing(0))
print(s.request_landing(4))
try:
    print(s.request_landing(5))
except:
    print("Ooops")

print(s.request_takeoff(0))
print(s.request_takeoff(4))
try:
    print(s.request_takeoff(5))
except:
    print("Ooops")