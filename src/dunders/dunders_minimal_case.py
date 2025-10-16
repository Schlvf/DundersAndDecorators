"""Minimal example for dunders."""


class MyObject:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, right_obj):
        return MyObject(self.value + str(right_obj))


if __name__ == "__main__":
    left_obj = MyObject(1)
    print(left_obj)
    right_obj = MyObject(2)
    print(left_obj)
    print(right_obj)
    print(left_obj + right_obj)
