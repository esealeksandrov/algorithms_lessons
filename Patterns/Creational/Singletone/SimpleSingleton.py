"""
Singleton - Класс, экземпляр которого может существовать только в единственном числе.
При создании нового синглтона возвращается ссылка на уже созданный обхект.
"""


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonRootUser(metaclass=SingletonMeta):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"{self._name}: {self._age}"

class SingletoneRootDir(metaclass=SingletonMeta):
    def __init__(self, path):
        self._path = path

    def __str__(self):
        return self._path



if __name__ == "__main__":
    u1 = SingletonRootUser("John", 23)
    u2 = SingletonRootUser("Rebecca", 24)
    p1 = SingletoneRootDir("/")

    print(u1, u2, u1, p1, u1)