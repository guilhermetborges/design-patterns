class Thing(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Thing, cls).__new__(cls)
            print('Initializing %s' % cls.instance)
        return cls.instance

f_I = Thing()
print(id(f_I))

S_I = Thing()
print(id(S_I))

T_I = Thing()
print(id(T_I))
