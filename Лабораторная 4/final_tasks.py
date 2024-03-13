class Door:
    """Базовый класс Дверь."""
    is_open: bool = False

    def __init__(self, height: int, width: int, base_material: str):
        """
        Создание и подготовка к работе объекта Дверь

        @param height: высота двери в мм
        @param width: ширина двери в мм
        @param base_material: основной материал
        """
        self._height = height
        self._width = width
        self._base_material = base_material

    @property
    def height(self) -> int:
        return self._height

    @property
    def width(self) -> int:
        return self._width

    @property
    def base_material(self) -> str:
        return self._base_material

    def open(self) -> None:
        """Открыть дверь."""
        ...

    def close(self) -> None:
        """Закрыть дверь."""
        ...

    def __str__(self):
        return (f'Высота/ширина двери: {self.height, self.width}, сделана из {self.base_material}, '
                f'дверь {"открыта" if self.is_open else "закрыта"}')

    def __repr__(self):
        return (f'{self.__class__.__name__}(height={self.height!r}, width={self.width!r}, '
                f'base_material={self.base_material!r})')


class FrontDoor(Door):
    """Класс Входная дверь."""
    def __init__(self, height: int, width: int, base_material: str, lock: str):
        """
        Создание и подготовка к работе объекта Входная дверь

        @param height: высота двери в мм
        @param width: ширина двери в мм
        @param base_material: основной материал
        @param lock: вид замка
        """
        super().__init__(height, width, base_material)
        self.lock = lock

    @property
    def lock(self) -> str:
        return self._lock

    @lock.setter
    def lock(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError('Lock must be a string.')
        self._lock = value

    def is_key_suitable(self, key: str) -> bool:
        """
        Подходит ли ключ для данной двери?
        @param key: ключ от замка
        @return: ключ подошел/не подошел
        """
        ...

    def open(self) -> bool:
        """
        Открыть дверь.
        Если is_key_suitable -> True, тогда дверь откроется.
        @return: открылась ли дверь или нет.
        """
        ...

    def close(self) -> bool:
        """
        Закрыть дверь.
        Если is_key_suitable -> True, тогда дверь закроется.
        @return: закрылась ли дверь или нет.
        """
        ...

    def __str__(self):
        return f'Высота/ширина двери: {self.height, self.width}, сделана из {self.base_material}, вид замка {self.lock}'

    def __repr__(self):
        return (f'{self.__class__.__name__}(height={self.height!r}, width={self.width!r}, '
                f'base_material={self.base_material!r}, lock={self.lock!r})')


class InnerDoor(Door):
    """Класс Межкомнатная дверь"""
    def __init__(self, height: int, width: int, base_material: str, has_glass: bool, thickness: int):
        """
        Создание и подготовка к работе объекта Дверь

        @param height: высота двери в мм
        @param width: ширина двери в мм
        @param base_material: основной материал
        @param has_glass: стеклянные вставки в двери
        @param thickness: толщина двери в мм
        """
        super().__init__(height, width, base_material)
        self.has_glass = has_glass
        self.thickness = thickness

    @property
    def has_glass(self) -> bool:
        return self._has_glass

    @has_glass.setter
    def has_glass(self, value: bool) -> None:
        """
        Стеклянные вставки в двери
        @param value: получаемое значение
        @raise keyError: если is_glass_base_material True, то has_glass False быть не может
        """
        if not isinstance(value, bool):
            raise TypeError('has_glass must be a bool.')
        self._has_glass = value

    def __repr__(self):
        return (f'{self.__class__.__name__}(height={self.height!r}, width={self.width!r}, '
                f'base_material={self.base_material!r}, has_glass={self.has_glass!r}, thickness={self.thickness!r})')

    def is_glass_base_material(self) -> bool:
        """Является ли дверь стеклянной"""
        ...


if __name__ == '__main__':
    door = Door(3000, 750, 'steel')
    print(door, '\n')
    front_door = FrontDoor(2000, 500, 'wood', 'Deadbolt Locks')
    inner_door = InnerDoor(2100, 550, 'glass', False, 50)
    print(front_door, inner_door, sep='\n')
