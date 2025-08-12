class Monostate:
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        return obj
    

m1 = Monostate()
m1.name = 'John'
m1.age = 30
print(id(m1))
print(m1.__dict__)

m2 = Monostate()
print(id(m2))
print(m2.__dict__)
