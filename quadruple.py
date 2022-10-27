from semantic_cube import operations

quadruple_operations = operations | {
    'print': 13,
    'read': 14,
    'write': 15,
    'goto': 16,
    'gotot': 17,
    'gotof': 18
}

class Quadruple():
    # Note that operators and result are memory addresses
    # -1 on operator2 is for operators such as assignment
    # None on result is for quadruples that may be generated with a pending result
    def __init__(self, operation: str, operator1: int, operator2: int = -1, result: int = None) -> None:
        if operation not in quadruple_operations:
            raise Exception('Unkown operation on quadruple')
        self.op_code = quadruple_operations[operation]
        self.operator1 = operator1
        self.operator2 = operator2
        self.result = result

    def __str__(self) -> str:
        return f'{self.op_code} {self.operator1} {self.operator2} {self.result}'

    def __repr__(self) -> str:
        return f'{self.op_code} {self.operator1} {self.operator2} {self.result}'

    def fill_result(self, result: int) -> None:
        self.result = result
    