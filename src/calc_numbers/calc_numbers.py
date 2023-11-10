from calc_numbers.calculator import Calculator
from custom_logger.custom_logger import get_logger, my_logger

@my_logger
def main():
    calc = Calculator()

    calc.add(3)
    calc.minus(5)

    calc.add(3+5)
    calc.add(8)

    calc.minus(11)


if __name__ == "__main__":
    main()

