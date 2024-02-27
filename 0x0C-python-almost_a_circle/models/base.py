#!/usr/bin/python3
"""
Defines a base model class

"""


class Base:
    """
    Represents the base model

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string
            ([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise valueError("Unsupported class")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary
                        in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                instances = []
                for line in file:
                    data = line.strip().split(",")
                    if cls.__name__ == 'Rectangle':
                        instance = cls(int(data[1]), int(data[2]),
                                    int(data[3]), int(data[4]), int(data[0]))
                    elif cls.__name__ == 'Square':
                        instance = cls(int(data[1]), int(data[2]),
                                    int(data[3]), int(data[0]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
