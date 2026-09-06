class Plant:

    @staticmethod
    def is_alder_than_year(age_day: int) -> bool:
        return age_day > 365

    def __init__(self, name: str, height: float, age_days: int, color: str) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, height: float):
        if height < 0:
            print("")



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
