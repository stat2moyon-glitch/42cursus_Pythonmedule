# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/30 21:28:35 by ttatsuno          #+#    #+#              #
#    Updated: 2026/09/02 22:14:13 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name: str, height: float, age_days: int) -> None:
		self._name = name
		self._height = 0.0
		self._age_days = 0
		self.set_height(height)
		self.set_age(age_days)

	def set_height(self, height: float) -> bool:
		if height < 0:
			print(f"{self._name}: Error, height can't be negative")
			return False
		self._height = float(height)
		return True

	def set_age(self, age_days: int) -> bool:
		if age_days < 0:
			print(f"{self._name}: Error, height can't be negative")
			return False
		self._age_days = age_days
		return True

	def get_height(self) -> float:
		return self._height

	def get_age(self) -> int:
		return self._age_days

	def grow(self, amount: float = 1.0) -> None:
		self.set_height(round(self._height + amount, 1))

	def age(self, days: int = 1) -> None:
		self.set_age(self._age_days + days)

	def show(self) -> None:
		print(
            f"{self._name}: {self._height:.1f}cm, "
            f"{self._age_days} days old"
        )

class Flower(Plant):
	def __init__(self, name: str, height: float, age_days:int, color: str) -> None:
		super().__init__(name, height, age_days)
		self._color = color
		self._is_blooming = False

	def bloom(self) -> None:
		self._is_blooming = True

	def show(self) -> None:
		super().show()
		print(f" Color: {self._color}")
		if self._is_blooming:
			print(f" {self._name} is blooming beautifully!")
		else:
			print(f" {self._name} has not bloomed yet")

class Tree(Plant):
	def __init__()
	class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount: float = 1.0) -> None:
        super().grow(amount)
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
