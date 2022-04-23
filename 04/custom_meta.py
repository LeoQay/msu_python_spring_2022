def is_magic(name: str) -> bool:
    if len(name) < 5:
        return False
    return name[:2] == '__' and name[-2:] == '__'


class CustomMeta(type):
    def __new__(mcs, name, bases, class_dict, **kwargs):
        new_dict = {}
        for key in class_dict.keys():
            value = class_dict[key]
            if is_magic(key):
                new_dict[key] = value
            else:
                new_dict['custom_' + key] = value
        class_dict = new_dict

        def setter(self, nam, val):
            if nam in self.__dict__:
                self.__dict__[nam] = val
            else:
                self.__dict__["custom_" + nam] = val

        class_dict['__setattr__'] = setter
        cls = super().__new__(mcs, name, bases, class_dict)

        return cls

    def __init__(cls, name, bases, class_dict, **kwargs):
        super().__init__(name, bases, class_dict, **kwargs)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)
