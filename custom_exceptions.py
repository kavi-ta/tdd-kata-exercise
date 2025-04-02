class NegativeNumberException(Exception):
    def __init__(self,numbers):
        message = f"negatives not allowed {','.join(map(str, numbers))}"
        super().__init__(message)
        self.numbers = numbers
