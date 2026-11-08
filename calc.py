def add(a, b):
    return a + b


def divide(a, b):
    return a / b


class Calc:
    def __init__(self, start):
        self.value = start

    def apply(self, op, operand):
        if op == "add":
            self.value = add(self.value, operand)
        elif op == "div":
            self.value = divide(self.value, operand)
        return self.value
