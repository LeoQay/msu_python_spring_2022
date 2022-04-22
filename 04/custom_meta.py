def is_magic(name: str) -> bool:
    if len(name) < 5:
        return False
    return name[:2] == '__' and name[-2:] == '__'


class CustomMeta(type):
    def __new__(mcs, name, bases, classdict, **kwargs):
        new_dict = {}
        for key in classdict.keys():
            value = classdict[key]
            if is_magic(key):
                new_dict[key] = value
            else:
                new_dict['custom_' + key] = value
        classdict = new_dict

        def setter(self, nam, val):
            self.__dict__["custom_" + nam] = val

        classdict['__setattr__'] = setter
        cls = super().__new__(mcs, name, bases, classdict)

        return cls

    def __init__(cls, name, bases, classdict, **kwargs):
        super().__init__(name, bases, classdict, **kwargs)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return {}
