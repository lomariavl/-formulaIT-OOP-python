import doctest


class RoadSign:
    def __init__(self, sign_type: str, size: int):
        """
       Создание и подготовка к работе объекта "Дорожный знак"

       :param sign_type: Категория дорожного знака
       :param size: Физический размер в см

       Примеры:
       >>> sign = RoadSign('Warning signs', 10)  # Инициализация экземпляра класса
       """
        if not isinstance(sign_type, str):
            raise TypeError("")
        self.sign_type = sign_type
        if not isinstance(size, int):
            raise TypeError
        self.size = size

    def set_position(self, coordinates: list[float, float]) -> bool:
        """
        Функция которая установит знак по координате
        :param coordinates: Координаты расположения

        :return: Получилось/не получилось установить дорожный знак

        Примеры:
        >>> sign = RoadSign('speed', 23)
        >>> sign.set_position([23.54, 56.45])
        """
        ...

    def remove_sign(self) -> None:
        """
        Функция которая убирает дорожный знак

        Примеры:
        >>> sign = RoadSign('walker', 23)
        >>> sign.set_position([23.54, 56.45])
        >>> sign.remove_sign()
        """
        ...


class Transport:
    def __init__(self, transport_type: str, brand: str):
        """
        Создание и подготовка к работе объекта "Транспорт"

        :param transport_type: Вид транспорта
        :param brand: Модель транспорта

        Примеры:
        >>> car = Transport('Car', 'Volkswagen')  # Инициализация экземпляра класса
        """
        if not isinstance(transport_type, str):
            raise TypeError("Вид транспорта должен быть строкой")
        self.transport_type = transport_type

        if not isinstance(brand, str):
            raise TypeError("Модель транспорта должна быть строкой")
        self.brand = brand

    def increase_speed(self, speed: float) -> float:
        """
        Функция которая увеличивает скорость
        :param speed: Скорость транспорта
        :raise ValueError: Скорость не может быть <= 0

        :return: Увеличенная скорость

        Примеры:
        >>> truck = Transport('truck', 'W')
        >>> truck.increase_speed(80.5)
        """
        ...

    def decrease_speed(self, speed: float) -> float:
        """
        Функция которая уменьшает скорость
        :param speed: Скорость транспорта
        :raise ValueError: Скорость не может быть <= 0

        :return: Уменьшенная скорость
        Примеры:
        >>> truck = Transport('truck', 'W')
        >>> truck.decrease_speed(80.5)
        """
        ...


class Headlights:
    def __init__(self, location: str, brightness: int):
        """
        Создание и подготовка к работе объекта "Фары"

        :param location: Расположение на транспорте
        :param brightness: Яркость света

        Примеры:
        >>> car = Headlights('Передние', 250)  # Инициализация экземпляра класса
        """
        if not isinstance(location, str):
            raise TypeError("Расположение фар должно быть строкой")
        self.location = location

        if not isinstance(brightness, int):
            raise TypeError("Яркость света должна быть int")
        self.brightness = brightness

    def turn_on(self) -> None:
        """
        Функция которая включает фары

        Примеры:
        >>> headlights = Headlights('Задние', 123)
        >>> headlights.turn_on()
        """
        ...

    def turn_off(self) -> None:
        """
        Функция которая выключает фары

        Примеры:
        >>> headlights = Headlights('Передние', 123)
        >>> headlights.turn_off()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
