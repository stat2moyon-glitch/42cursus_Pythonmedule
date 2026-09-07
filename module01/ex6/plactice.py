class Plant:
    class Statistics:
        def __init__(self) -> None:
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def record_grow(self) -> None:
            self.__grow_calls += 1

        def record_age(self) -> None:
            self.__age_calls += 1

        def record_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_calls} grow, "
                f"{self.__age_calls} age, "
                f"{self.__show_calls} show"
            )

    @staticmethod
    def is_alder_than_year(age_day: int) -> bool:
        return age_day > 365

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        #やっぱ↓わからん
        self._statistics = self.Statistics()
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = float(height)
        return True

    def show(self) -> None:
        self._statistics.record_show()
        print(
            f"{self._name}: {self._height:.1f}cm, "
            f"{self.age_days} days old"
        )

    def display_statistics(self) -> None:
        self._statistics.display()

class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
    )-> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


def display_statistics(plant: Plant) -> None:
    plant.display_statistics()

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )
    print()

    print("=== Flower")
    rose = Plant("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
