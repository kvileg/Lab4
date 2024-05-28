class Calculator:
    """
    Простой калькулятор для выполнения арифметических операций.

    Attributes:
        name (str): Имя калькулятора.

    Пример использования:
        >>> calc = Calculator("Мой калькулятор")
        >>> calc.add(2, 3)
        5
        >>> calc.subtract(5, 3)
        2
        >>> calc.multiply(2, 3)
        6
        >>> calc.divide(10, 2)
        5.0
        >>> calc.power(2, 3)
        8
        >>> calc.square_root(25)
        5.0
    """

    def __init__(self, name):
        """
        Создает новый экземпляр калькулятора.

        Args:
            name (str): Имя калькулятора.
        """
        self.name = name

    def add(self, a, b):
        """
        Вычисляет сумму двух чисел.

        Args:
            a (int): Первое число.
            b (int): Второе число.

        Returns:
            int: Сумма двух чисел.
        """
        return a + b

    def subtract(self, a, b):
        """
        Вычисляет разность двух чисел.

        Args:
            a (int): Первое число.
            b (int): Второе число.

        Returns:
            int: Разность двух чисел.
        """
        return a - b

    def multiply(self, a, b):
        """
        Вычисляет произведение двух чисел.

        Args:
            a (int): Первое число.
            b (int): Второе число.

        Returns:
            int: Произведение двух чисел.
        """
        return a * b

    def divide(self, a, b):
        """
        Выполняет деление одного числа на другое.

        Args:
            a (int): Делимое.
            b (int): Делитель.

        Returns:
            float: Результат деления.
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    def power(self, base, exponent):
        """
        Вычисляет степень числа.

        Args:
            base (int): Основание.
            exponent (int): Показатель степени.

        Returns:
            int: Результат возведения в степень.
        """
        return base ** exponent

    def square_root(self, num):
        """
        Вычисляет квадратный корень числа.

        Args:
            num (int): Число, из которого нужно извлечь квадратный корень.

        Returns:
            float: Квадратный корень числа.
        """
        if num < 0:
            raise ValueError("Квадратный корень из отрицательного числа невозможен")
        return num ** 0.5
