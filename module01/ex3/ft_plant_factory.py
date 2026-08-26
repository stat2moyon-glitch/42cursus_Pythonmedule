# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/26 21:40:16 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/26 22:56:24 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name: str, height: float, age_days: int) -> None:
		self.name = name
		self.height = height
		self.age_days = age_days

	def grow(self, amout: float = 1.0) -> None:
		self.height = round(self.height + amount, 1)

	def age(self, days: int = 1) -> None:
		self.age_days +=days

	def show(self) -> None:
		print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

if __name__ == "__main__":
	plants = [
		Plant("Rose", 25.0, 30),
		Plant("Oak", 200.0, 365),
		Plant("Cactus", 5.0, 90),
		Plant("Sunflower", 80.0, 45),
		Plant("Fern", 15.0, 120),
	]

	print("=== Plant Factory Output ===")
	for plant in plants:
		print("Created: ", end="")
		plant.show()
