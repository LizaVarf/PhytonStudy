from abc import ABC, abstractmethod


class Tree(ABC):
    """
    Дерево.

    Атрибуты:
        species: Вид дерева (непустая строка).
        height_m: Высота (м), > 0.
        age_years: Возраст (лет), >= 0.

    Doctest:

    >>> class _Oak(Tree):
    ...     def grow(self, meters: float) -> None: ...
    ...     def absorb_water(self, liters: float) -> None: ...
    ...     def describe(self) -> str: ...
    ...
    >>> t = _Oak("Oak", 2.5, 5)
    >>> (t.species, t.height_m, t.age_years)
    ('Oak', 2.5, 5)

    >>> _Oak("", 2.5, 5)
    Traceback (most recent call last):
    ...
    ValueError: species must be a non-empty string
    """

    def __init__(self, species: str, height_m: float, age_years: int) -> None:
        if not isinstance(species, str) or not species.strip():
            raise ValueError("species must be a non-empty string")

        if height_m <= 0:
            raise ValueError("height_m must be > 0")

        if age_years < 0:
            raise ValueError("age_years must be >= 0")

        self.species: str = species
        self.height_m: float = height_m
        self.age_years: int = age_years

    @abstractmethod
    def grow(self, meters: float) -> None:
        """
        Увеличить высоту дерева.

        :param meters: Насколько метров вырастет дерево (> 0)
        :return: None
        """
        ...

    @abstractmethod
    def absorb_water(self, liters: float) -> None:
        """
        Поглотить воду.

        :param liters: Количество воды в литрах (> 0)
        :return: None
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Вернуть текстовое описание дерева.

        :return: Строка с описанием дерева
        """

class Car(ABC):
    """
    Машина.

    Атрибуты:
        brand: Марка автомобиля (непустая строка).
        max_speed: Максимальная скорость (км/ч), > 0.
        mileage: Пробег (км), >= 0.

    Doctest:

    >>> class _Audi(Car):
    ...     def drive(self, distance: float) -> None: ...
    ...     def refuel(self, liters: float) -> None: ...
    ...     def describe(self) -> str: ...
    ...
    >>> c = _Audi("Audi", 240, 10000)
    >>> (c.brand, c.max_speed, c.mileage)
    ('Audi', 240, 10000)

    >>> _Audi("", 240, 10000)
    Traceback (most recent call last):
    ...
    ValueError: brand must be a non-empty string
    """

    def __init__(self, brand: str, max_speed: float, mileage: float) -> None:
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("brand must be a non-empty string")

        if max_speed <= 0:
            raise ValueError("max_speed must be > 0")

        if mileage < 0:
            raise ValueError("mileage must be >= 0")

        self.brand: str = brand
        self.max_speed: float = max_speed
        self.mileage: float = mileage

    @abstractmethod
    def drive(self, distance: float) -> None:
        """
        Проехать определённое расстояние.

        :param distance: Расстояние в км (> 0)
        :return: None
        """
        ...

    @abstractmethod
    def refuel(self, liters: float) -> None:
        """
        Заправить автомобиль.

        :param liters: Количество топлива (> 0)
        :return: None
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Вернуть описание автомобиля.

        :return: Строка с описанием
        """
        ...


class Book(ABC):
    """
    Книга.

    Атрибуты:
        title: Название книги (непустая строка).
        pages: Количество страниц (> 0).
        author: Автор книги (непустая строка).

    Doctest:

    >>> class _Novel(Book):
    ...     def read(self, pages: int) -> None: ...
    ...     def bookmark(self, page: int) -> None: ...
    ...     def describe(self) -> str: ...
    ...
    >>> b = _Novel("1984", 328, "Orwell")
    >>> (b.title, b.pages, b.author)
    ('1984', 328, 'Orwell')

    >>> _Novel("", 328, "Orwell")
    Traceback (most recent call last):
    ...
    ValueError: title must be a non-empty string
    """

    def __init__(self, title: str, pages: int, author: str) -> None:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")

        if pages <= 0:
            raise ValueError("pages must be > 0")

        if not isinstance(author, str) or not author.strip():
            raise ValueError("author must be a non-empty string")

        self.title: str = title
        self.pages: int = pages
        self.author: str = author

    @abstractmethod
    def read(self, pages: int) -> None:
        """
        Прочитать указанное количество страниц.

        :param pages: Количество страниц (> 0)
        :return: None
        """
        ...

    @abstractmethod
    def bookmark(self, page: int) -> None:
        """
        Поставить закладку.

        :param page: Номер страницы (>= 1)
        :return: None
        """
        ...

    @abstractmethod
    def describe(self) -> str:
        """
        Вернуть описание книги.

        :return: Строка с описанием
        """