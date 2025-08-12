class Singleton():
    _Instance = None

    def __init__(self):
        if not Singleton._Instance:
            print('Initializing Singleton')
        else:
             print(f'Singleton already created {Singleton.getInstance()}')

    
    @classmethod
    def getInstance(cls):
        if not cls._Instance:
            cls._Instance = Singleton()
        return cls._Instance


s1 = Singleton()
print(Singleton.getInstance())
s1.name = 'John'

s2 = Singleton()
print(s1.__dict__)
print(s2.__dict__)
