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