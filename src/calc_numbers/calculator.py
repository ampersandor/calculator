class Calculator:
    """A simple calculator class for basic arithmetic operations.
    
    Notes:
        hello this is notes
        
    Attributes:
        value (int): The current value stored in the calculator.

    """

    def __init__(self):
        """Initialize a new Calculator with an initial value of 0."""
        self.value = 0


    def add(self, a, b=None):
        """
        Add two numbers to the calculator's current value or add a single number to the current value.

        Args:
            a (int): The first number to add.
            b (int, optional): The second number to add. If not provided, 'a' will be added to the current value.
        
        Returns:
            (int): a + b or value + a depends on the input
        """
        if b:
            self.value = a + b
        else:
            self.value += a

        print(f"the result is {self.value}")

        return self.value


    def minus(self, a, b=None):
        """
        Subtract two numbers from the calculator's current value or subtract a single number from the current value.

        Args:
            a (int): The first number to subtract.
            b (int, optional): The second number to subtract. If not provided, 'a' will be subtracted from the current value.
        
        Returns:
            (int): a - b or value - a depends on the input

        """
        if b:
            self.value = a - b
        else:
            self.value -= a
        
        print(f"the result is {self.value}")
        
        return self.value
