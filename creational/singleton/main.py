class Singleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

obj = Singleton()
obj2 = Singleton()

print("obj  =>",obj)
print("obj2 =>",obj2)