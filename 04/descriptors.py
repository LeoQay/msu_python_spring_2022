class Integer:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Wrong integer value')
        instance.__dict__[self.name] = value

    def __init__(self):
        self.name = 'name'

    def __set_name__(self, owner, name):
        self.name = name


class String:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Wrong string value')
        instance.__dict__[self.name] = value

    def __init__(self):
        self.name = 'name'

    def __set_name__(self, owner, name):
        self.name = name


class PositiveInteger:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if (not isinstance(value, int)) or value <= 0:
            raise ValueError('Wrong positive integer value')
        instance.__dict__[self.name] = value

    def __init__(self):
        self.name = 'name'

    def __set_name__(self, owner, name):
        self.name = name
