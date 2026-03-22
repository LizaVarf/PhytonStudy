class Car:
    """
    Базовый класс: Автомобиль.

    Атрибуты:
        brand: Марка автомобиля.
        max_speed: Максимальная скорость (км/ч).
        fuel: Количество топлива (л).

    Приватный атрибут:
        _engine_on: состояние двигателя (инкапсулирован,
        чтобы нельзя было менять напрямую).
    """

    def __init__(self, brand: str, max_speed: float, fuel: float) -> None:
        if not brand.strip():
            raise ValueError("brand must be non-empty")

        if max_speed <= 0:
            raise ValueError("max_speed must be > 0")

        if fuel < 0:
            raise ValueError("fuel must be >= 0")

        self.brand: str = brand
        self.max_speed: float = max_speed
        self.fuel: float = fuel
        self._engine_on: bool = False  # инкапсуляция состояния двигателя

    def __str__(self) -> str:
        return f"{self.brand} (max_speed={self.max_speed}, fuel={self.fuel})"

    def __repr__(self) -> str:
        return (
            f"Car(brand={self.brand!r}, max_speed={self.max_speed}, "
            f"fuel={self.fuel})"
        )

    def start_engine(self) -> None:
        """
        Запустить двигатель.

        :return: None
        """
        self._engine_on = True

    def stop_engine(self) -> None:
        """
        Остановить двигатель.

        :return: None
        """
        self._engine_on = False

    def drive(self, distance: float) -> float:
        """
        Проехать расстояние.

        :param distance: расстояние (км), > 0
        :return: расход топлива
        """
        if distance <= 0:
            raise ValueError("distance must be > 0")

        if not self._engine_on:
            raise RuntimeError("engine is off")

        fuel_used = distance * 0.1
        self.fuel -= fuel_used
        return fuel_used


class PassengerCar(Car):
    """
    Дочерний класс: Легковой автомобиль.

    Дополнительные атрибуты:
        seats: количество мест.
    """

    def __init__(self, brand: str, max_speed: float, fuel: float, seats: int) -> None:
        super().__init__(brand, max_speed, fuel)

        if seats <= 0:
            raise ValueError("seats must be > 0")

        self.seats: int = seats

    def __str__(self) -> str:
        return f"{self.brand} (passenger, seats={self.seats})"

    def __repr__(self) -> str:
        return (
            f"PassengerCar(brand={self.brand!r}, max_speed={self.max_speed}, "
            f"fuel={self.fuel}, seats={self.seats})"
        )

    def drive(self, distance: float) -> float:
        """
        Переопределённый метод движения.

        Причина переопределения:
        Легковые автомобили легче, поэтому расход топлива ниже.

        :param distance: расстояние (км), > 0
        :return: расход топлива
        """
        if distance <= 0:
            raise ValueError("distance must be > 0")

        if not self._engine_on:
            raise RuntimeError("engine is off")

        fuel_used = distance * 0.07
        self.fuel -= fuel_used
        return fuel_used


class Truck(Car):
    """
    Дочерний класс: Грузовой автомобиль.

    Дополнительные атрибуты:
        load_capacity: грузоподъёмность (кг).
    """

    def __init__(self, brand: str, max_speed: float, fuel: float, load_capacity: float) -> None:
        super().__init__(brand, max_speed, fuel)

        if load_capacity <= 0:
            raise ValueError("load_capacity must be > 0")

        self.load_capacity: float = load_capacity

    def __str__(self) -> str:
        return f"{self.brand} (truck, capacity={self.load_capacity} kg)"

    def __repr__(self) -> str:
        return (
            f"Truck(brand={self.brand!r}, max_speed={self.max_speed}, "
            f"fuel={self.fuel}, load_capacity={self.load_capacity})"
        )

    def drive(self, distance: float) -> float:
        """
        Переопределённый метод движения.

        Причина переопределения:
        Грузовые автомобили тяжелее, поэтому расход топлива выше.

        :param distance: расстояние (км), > 0
        :return: расход топлива
        """
        if distance <= 0:
            raise ValueError("distance must be > 0")

        if not self._engine_on:
            raise RuntimeError("engine is off")

        fuel_used = distance * 0.2
        self.fuel -= fuel_used
        return fuel_used

    def load_cargo(self, weight: float) -> bool:
        """
        Загрузить груз.

        :param weight: вес груза (кг), > 0
        :return: True если груз помещается
        """
        if weight <= 0:
            raise ValueError("weight must be > 0")

        return weight <= self.load_capacity


if __name__ == "__main__":
    # Создание экземпляров
    car = Car("Generic", 180, 50)
    passenger = PassengerCar("Toyota", 200, 60, 5)
    truck = Truck("Volvo", 120, 150, 10000)

    # Выводим информацию о машинах
    print(car)
    print(passenger)
    print(truck)

    # Запуск двигателя
    passenger.start_engine()
    truck.start_engine()

    # Движение
    print("Passenger car fuel used:", passenger.drive(100))
    print("Truck fuel used:", truck.drive(100))

    # Грузоподъемность
    print("Can load 5000 kg:", truck.load_cargo(5000))
    print("Can load 15000 kg:", truck.load_cargo(15000))

