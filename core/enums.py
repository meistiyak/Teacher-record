from enum import Enum, IntEnum


class BaseEnum(Enum):
    @classmethod
    def get_choices(cls):
        return [(item.value, item.name) for item in cls]

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class BaseIntEnum(IntEnum):
    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def get_name(cls, value):
        return cls(value).name

    @classmethod
    def list(cls):
        """

        :return: list of value in enum class
        """
        return list(map(int, cls))
