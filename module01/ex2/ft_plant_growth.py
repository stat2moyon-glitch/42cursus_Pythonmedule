# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/26 19:56:22 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/26 22:56:20 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	name: str
	height: float
	age_days: int
	growth_rate: float

	def grow(self) -> None:
		self.height = (self.height + self.growth_rate, 1)

	def age(self) ->None:
		self.age_days += 1

	def show(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age_days:.1f} days old")

if __name__ == "__main__":
	rose = Plant()
	rose.name = "Rose"
	rose.height = 25.0
	rose.age_days = 30
	rose.growth_rate = 0.8
	starting_height = rose.height

	print("=== Garden Plant Growth ===")
	rose.show()
	for i in range (1 , 8):
		print(f"=== Day {i} ===")
		rose.grow()
		rose.age()
		rose.show()

	weekly_growth = round(rose.height - starting_height, 1)
	print(f"Growth this week: {weekly_growth:.1f}cm")
